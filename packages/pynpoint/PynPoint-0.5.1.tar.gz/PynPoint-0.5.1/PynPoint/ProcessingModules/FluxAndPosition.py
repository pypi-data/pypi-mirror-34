"""
Modules for photometric and astrometric measurements of a planet.
"""

import math
import sys
import warnings

import numpy as np
import emcee

from scipy.ndimage import shift, fourier_shift, rotate
from scipy.ndimage.filters import gaussian_filter
from scipy.optimize import minimize
from scipy.stats import t
from sklearn.decomposition import PCA
from skimage.feature import hessian_matrix
from astropy.nddata import Cutout2D
from photutils import aperture_photometry, CircularAperture

from PynPoint.Core.Processing import ProcessingModule
from PynPoint.ProcessingModules.PSFpreparation import PSFpreparationModule
from PynPoint.ProcessingModules.PSFSubtractionPCA import PcaPsfSubtractionModule
from PynPoint.Util.ModuleTools import progress, memory_frames, image_size, image_size_port, \
                                      number_images_port, create_mask, crop_image
from PynPoint.Util.AnalysisTools import false_alarm


class FakePlanetModule(ProcessingModule):
    """
    Module to inject a positive or negative fake companion into a stack of images.
    """

    def __init__(self,
                 position,
                 magnitude,
                 psf_scaling=1.,
                 interpolation="spline",
                 name_in="fake_planet",
                 image_in_tag="im_arr",
                 psf_in_tag="im_psf",
                 image_out_tag="im_fake",
                 **kwargs):
        """
        Constructor of FakePlanetModule.

        :param position: Angular separation (arcsec) and position angle (deg) of the fake planet.
                         Angle is measured in counterclockwise direction with respect to the
                         upward direction (i.e., East of North).
        :type position: tuple
        :param magnitude: Magnitude of the fake planet with respect to the star.
        :type magnitude: float
        :param psf_scaling: Additional scaling factor of the planet flux (e.g., to correct for a
                            neutral density filter). A negative value will inject a negative
                            planet signal.
        :type psf_scaling: float
        :param interpolation: Type of interpolation that is used for shifting the images (spline,
                              bilinear, or fft).
        :type interpolation: str
        :param name_in: Unique name of the module instance.
        :type name_in: str
        :param image_in_tag: Tag of the database entry with images that are read as input.
        :type image_in_tag: str
        :param psf_in_tag: Tag of the database entry that contains the reference PSF that is used
                           as fake planet. Can be either a single image (2D) or a cube (3D) with
                           the dimensions equal to *image_in_tag*.
        :type psf_in_tag: str
        :param image_out_tag: Tag of the database entry with images that are written as output.
        :type image_out_tag: str
        :param \**kwargs:
            See below.

        :Keyword arguments:
             * **verbose** (*bool*) -- Print progress.

        :return: None
        """

        if "verbose" in kwargs:
            self.m_verbose = kwargs["verbose"]
        else:
            self.m_verbose = True

        super(FakePlanetModule, self).__init__(name_in)

        self.m_image_in_port = self.add_input_port(image_in_tag)
        if psf_in_tag == image_in_tag:
            self.m_psf_in_port = self.m_image_in_port
        else:
            self.m_psf_in_port = self.add_input_port(psf_in_tag)
        self.m_image_out_port = self.add_output_port(image_out_tag)

        self.m_position = position
        self.m_magnitude = magnitude
        self.m_psf_scaling = psf_scaling
        self.m_interpolation = interpolation

    def _images_init(self):
        memory = self._m_config_port.get_attribute("MEMORY")

        ndim_image = self.m_image_in_port.get_ndim()
        ndim_psf = self.m_psf_in_port.get_ndim()

        if ndim_image != 3:
            raise ValueError("The image_in_tag should contain a cube of images.")

        nimages = number_images_port(self.m_image_in_port)
        im_size = image_size_port(self.m_image_in_port)
        frames = memory_frames(memory, nimages)

        npsf = number_images_port(self.m_psf_in_port)
        psf_size = image_size_port(self.m_psf_in_port)

        if psf_size != im_size:
            raise ValueError("The images in '"+self.m_image_in_port.tag+"' should have the same "
                             "dimensions as the images images in '"+self.m_psf_in_port.tag+"'.")

        if ndim_psf == 3 and npsf == 1:
            psf = np.squeeze(self.m_psf_in_port.get_all(), axis=0)
            ndim_psf = psf.ndim

        elif ndim_psf == 2:
            psf = self.m_psf_in_port.get_all()

        elif ndim_psf == 3 and nimages != npsf:
            psf = np.zeros((self.m_psf_in_port.get_shape()[1],
                            self.m_psf_in_port.get_shape()[2]))

            frames_psf = memory_frames(memory, npsf)

            for i, _ in enumerate(frames_psf[:-1]):
                psf += np.sum(self.m_psf_in_port[frames_psf[i]:frames_psf[i+1]], axis=0)

            psf /= float(npsf)

            ndim_psf = psf.ndim

        elif ndim_psf == 3 and nimages == npsf:
            psf = None

        return frames, psf, ndim_psf

    def _shift_psf(self, psf, parang):
        pixscale = self.m_image_in_port.get_attribute("PIXSCALE")

        radial = self.m_position[0]/pixscale
        theta = self.m_position[1]*math.pi/180. + math.pi/2.

        x_shift = radial*math.cos(theta-parang)
        y_shift = radial*math.sin(theta-parang)

        if self.m_interpolation == "spline":
            psf_shift = shift(psf, (y_shift, x_shift), order=5, mode='reflect')

        elif self.m_interpolation == "bilinear":
            psf_shift = shift(psf, (y_shift, x_shift), order=1, mode='reflect')

        elif self.m_interpolation == "fft":
            psf_fft = fourier_shift(np.fft.fftn(psf), (y_shift, x_shift))
            psf_shift = np.fft.ifftn(psf_fft).real

        else:
            raise ValueError("Interpolation should be fft, spline, or bilinear.")

        return psf_shift

    def run(self):
        """
        Run method of the module. Shifts the reference PSF to the location of the fake planet
        with an additional correction for the parallactic angle and writes the stack with images
        with the injected planet signal.

        :return: None
        """

        self.m_image_out_port.del_all_data()
        self.m_image_out_port.del_all_attributes()

        parang = self.m_image_in_port.get_attribute("PARANG")
        parang *= math.pi/180.

        flux_ratio = 10.**(-self.m_magnitude/2.5)

        frames, psf, ndim_psf = self._images_init()

        for j, _ in enumerate(frames[:-1]):
            if self.m_verbose:
                progress(j, len(frames[:-1]), "Running FakePlanetModule...")

            image = np.copy(self.m_image_in_port[frames[j]:frames[j+1]])

            for i in range(image.shape[0]):
                if ndim_psf == 2:
                    psf_tmp = np.copy(psf)

                elif ndim_psf == 3:
                    psf_tmp = self.m_psf_in_port[frames[j]+i, ]

                psf_shift = self._shift_psf(psf_tmp, parang[frames[j]+i])
                image[i, ] += self.m_psf_scaling*flux_ratio*psf_shift

            self.m_image_out_port.append(image)

        if self.m_verbose:
            sys.stdout.write("Running FakePlanetModule... [DONE]\n")
            sys.stdout.flush()

        self.m_image_out_port.copy_attributes_from_input_port(self.m_image_in_port)

        self.m_image_out_port.add_history_information("Fake planet",
                                                      "(sep, angle, mag) = " + "(" + \
                                                      "{0:.2f}".format(self.m_position[0])+", "+ \
                                                      "{0:.2f}".format(self.m_position[1])+", "+ \
                                                      "{0:.2f}".format(self.m_magnitude)+")")

        self.m_image_out_port.close_port()


class SimplexMinimizationModule(ProcessingModule):
    """
    Module to measure the flux and position of a planet by injecting negative fake planets and
    minimizing a function of merit.
    """

    def __init__(self,
                 position,
                 magnitude,
                 psf_scaling=-1.,
                 name_in="simplex",
                 image_in_tag="im_arr",
                 psf_in_tag="im_psf",
                 res_out_tag="simplex_res",
                 flux_position_tag="flux_position",
                 merit="hessian",
                 aperture=0.1,
                 sigma=0.027,
                 tolerance=0.1,
                 pca_number=20,
                 cent_size=None,
                 edge_size=None,
                 extra_rot=0.):
        """
        Constructor of SimplexMinimizationModule.

        :param position: Approximate position (x, y) of the planet (pix). This is also the location
                         where the function of merit is calculated with an aperture of radius
                         *aperture*.
        :type position: tuple, int
        :param magnitude: Approximate magnitude of the planet relative to the star.
        :type magnitude: float
        :param psf_scaling: Additional scaling factor of the planet flux (e.g., to correct for a
                            neutral density filter). Should be negative in order to inject
                            negative fake planets.
        :type psf_scaling: float
        :param name_in: Unique name of the module instance.
        :type name_in: str
        :param image_in_tag: Tag of the database entry with images that are read as input.
        :type image_in_tag: str
        :param psf_in_tag: Tag of the database entry with the reference PSF that is used as fake
                           planet. Can be either a single image (2D) or a cube (3D) with the
                           dimensions equal to *image_in_tag*.
        :type psf_in_tag: str
        :param res_out_tag: Tag of the database entry with the image residuals that are written
                            as output. Contains the results from the PSF subtraction during the
                            minimization of the function of merit. The last image is the image
                            with the best-fit residuals.
        :type res_out_tag: str
        :param flux_position_tag: Tag of the database entry with flux and position results that are
                                  written as output. Each step of the minimization saves the
                                  x position (pix), y position (pix), separation (arcsec),
                                  angle (deg), contrast (mag), and the function of merit. The last
                                  row of values contain the best-fit results.
        :type flux_position_tag: str
        :param merit: Function of merit for the minimization. Can be either *hessian*, to minimize
                      the sum of the absolute values of the determinant of the Hessian matrix,
                      or *sum*, to minimize the sum of the absolute pixel values
                      (Wertz et al. 2017).
        :type merit: str
        :param aperture: Aperture radius (arcsec) used for the minimization at *position*.
        :type aperture: float
        :param sigma: Standard deviation (arcsec) of the Gaussian kernel which is used to smooth
                      the images before the function of merit is calculated (in order to reduce
                      small pixel-to-pixel variations). Highest astrometric and photometric
                      precision is achieved when sigma is optimized.
        :type sigma: float
        :param tolerance: Absolute error on the input parameters, position (pix) and
                          contrast (mag), that is used as acceptance level for convergence. Note
                          that only a single value can be specified which is used for both the
                          position and flux so tolerance=0.1 will give a precision of 0.1 mag
                          and 0.1 pix. The tolerance on the output (i.e., function of merit)
                          is set to np.inf so the condition is always met.
        :type tolerance: float
        :param pca_number: Number of principle components used for the PSF subtraction.
        :type pca_number: int
        :param cent_size: Radius of the central mask (arcsec). No mask is used when set to None.
        :type cent_size: float
        :param edge_size: Outer radius (arcsec) beyond which pixels are masked. No outer mask is
                          used when set to None. The radius will be set to half the image size if
                          the *edge_size* value is larger than half the image size.
        :type edge_size: float
        :param extra_rot: Additional rotation angle of the images in clockwise direction (deg).
        :type extra_rot: float

        :return: None
        """

        super(SimplexMinimizationModule, self).__init__(name_in)

        self.m_image_in_port = self.add_input_port(image_in_tag)
        if psf_in_tag == image_in_tag:
            self.m_psf_in_port = self.m_image_in_port
        else:
            self.m_psf_in_port = self.add_input_port(psf_in_tag)
        self.m_res_out_port = self.add_output_port(res_out_tag)
        self.m_flux_position_port = self.add_output_port(flux_position_tag)

        self.m_position = (int(position[0]), int(position[1]))
        self.m_magnitude = magnitude
        self.m_psf_scaling = psf_scaling
        self.m_merit = merit
        self.m_aperture = aperture
        self.m_sigma = sigma
        self.m_tolerance = tolerance
        self.m_pca_number = pca_number
        self.m_cent_size = cent_size
        self.m_edge_size = edge_size
        self.m_extra_rot = extra_rot

        self.m_image_in_tag = image_in_tag
        self.m_psf_in_tag = psf_in_tag

    def run(self):
        """
        Run method of the module. The position and flux of a planet are measured by injecting
        negative fake companions and applying a simplex method (Nelder-Mead) for minimization
        of a function of merit at the planet location. The default function of merit is the
        image curvature which is calculated as the sum of the absolute values of the
        determinant of the Hessian matrix.

        :return: None
        """

        def _rotate(center, position, angle):
            pos_x = (position[0]-center[0])*math.cos(np.radians(angle)) - \
                    (position[1]-center[1])*math.sin(np.radians(angle))

            pos_y = (position[0]-center[0])*math.sin(np.radians(angle)) + \
                    (position[1]-center[1])*math.cos(np.radians(angle))

            return (center[0]+pos_x, center[1]+pos_y)

        def _objective(arg):
            sys.stdout.write('.')
            sys.stdout.flush()

            pos_x = arg[0]
            pos_y = arg[1]
            mag = arg[2]

            sep = math.sqrt((pos_y-center[0])**2+(pos_x-center[1])**2)*pixscale
            ang = math.atan2(pos_y-center[0], pos_x-center[1])*180./math.pi - 90.

            fake_planet = FakePlanetModule(position=(sep, ang),
                                           magnitude=mag,
                                           psf_scaling=self.m_psf_scaling,
                                           interpolation="spline",
                                           name_in="fake_planet",
                                           image_in_tag=self.m_image_in_tag,
                                           psf_in_tag=self.m_psf_in_tag,
                                           image_out_tag="simplex_fake",
                                           verbose=False)

            fake_planet.connect_database(self._m_data_base)
            fake_planet.run()

            prep = PSFpreparationModule(name_in="prep",
                                        image_in_tag="simplex_fake",
                                        image_out_tag="simplex_prep",
                                        image_mask_out_tag=None,
                                        mask_out_tag=None,
                                        norm=False,
                                        cent_size=self.m_cent_size,
                                        edge_size=self.m_edge_size,
                                        verbose=False)

            prep.connect_database(self._m_data_base)
            prep.run()

            psf_sub = PcaPsfSubtractionModule(name_in="pca_simplex",
                                              pca_numbers=self.m_pca_number,
                                              images_in_tag="simplex_prep",
                                              reference_in_tag="simplex_prep",
                                              res_mean_tag="simplex_res_mean",
                                              res_median_tag=None,
                                              res_arr_out_tag=None,
                                              res_rot_mean_clip_tag=None,
                                              extra_rot=self.m_extra_rot,
                                              verbose=False)

            psf_sub.connect_database(self._m_data_base)
            psf_sub.run()

            res_input_port = self.add_input_port("simplex_res_mean")
            im_res = res_input_port.get_all()

            if len(im_res.shape) == 3:
                if im_res.shape[0] == 1:
                    im_res = np.squeeze(im_res, axis=0)
                else:
                    raise ValueError("Multiple residual images found, expecting only one.")

            self.m_res_out_port.append(im_res, data_dim=3)

            im_crop = crop_image(image=im_res,
                                 center=self.m_position,
                                 size=2*int(math.ceil(self.m_aperture)))

            npix = image_size(im_crop)[0]

            if npix%2 == 0:
                raise ValueError("An odd-sized image is expected.")

            if self.m_merit == "hessian":

                x_grid = y_grid = np.linspace(-(npix-1)/2, (npix-1)/2, npix)
                xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
                rr_grid = np.sqrt(xx_grid*xx_grid+yy_grid*yy_grid)

                hessian_rr, hessian_rc, hessian_cc = hessian_matrix(im_crop,
                                                                    sigma=self.m_sigma,
                                                                    mode='constant',
                                                                    cval=0.,
                                                                    order='rc')

                hes_det = (hessian_rr*hessian_cc) - (hessian_rc*hessian_rc)
                hes_det[rr_grid > self.m_aperture] = 0.
                merit = np.sum(np.abs(hes_det))

            elif self.m_merit == "sum":

                if self.m_sigma > 0.:
                    im_crop = gaussian_filter(input=im_crop, sigma=self.m_sigma)

                aperture = CircularAperture((npix/2., npix/2.), self.m_aperture)
                phot_table = aperture_photometry(np.abs(im_crop), aperture, method='exact')
                merit = phot_table['aperture_sum']

            else:
                raise ValueError("Function of merit not recognized.")

            position = _rotate(center, (pos_x, pos_y), -self.m_extra_rot)

            res = np.asarray((position[0],
                              position[1],
                              sep,
                              (ang-self.m_extra_rot)%360.,
                              mag,
                              merit))

            self.m_flux_position_port.append(res, data_dim=2)

            return merit

        self.m_res_out_port.del_all_data()
        self.m_res_out_port.del_all_attributes()

        self.m_flux_position_port.del_all_data()
        self.m_flux_position_port.del_all_attributes()

        pixscale = self.m_image_in_port.get_attribute("PIXSCALE")

        self.m_aperture /= pixscale
        self.m_sigma /= pixscale

        if self.m_image_in_port.get_ndim() != 3:
            raise ValueError("The image_in_tag should contain a cube of images.")

        psf_size = image_size_port(self.m_psf_in_port)
        center = (psf_size[0]/2., psf_size[1]/2.)

        sys.stdout.write("Running SimplexMinimizationModule")
        sys.stdout.flush()

        pos_init = _rotate(center, self.m_position, self.m_extra_rot)
        pos_init = (int(pos_init[0]), int(pos_init[1]))

        minimize(fun=_objective,
                 x0=[pos_init[0], pos_init[1], self.m_magnitude],
                 method="Nelder-Mead",
                 tol=None,
                 options={'xatol': self.m_tolerance, 'fatol': float("inf")})

        sys.stdout.write(" [DONE]\n")
        sys.stdout.flush()

        self.m_res_out_port.add_history_information("Flux and position",
                                                    "Simplex minimization")

        self.m_flux_position_port.add_history_information("Flux and position",
                                                          "Simplex minimization")

        self.m_res_out_port.copy_attributes_from_input_port(self.m_image_in_port)
        self.m_flux_position_port.copy_attributes_from_input_port(self.m_image_in_port)

        self.m_res_out_port.close_port()


class FalsePositiveModule(ProcessingModule):
    """
    Module to calculate the signal-to-noise ratio (SNR) and false positive fraction (FPF) at a
    specified location in an image by using the Student's t-test (Mawet et al. 2014).
    """

    def __init__(self,
                 position,
                 aperture=0.1,
                 ignore=False,
                 name_in="snr",
                 image_in_tag="im_arr",
                 snr_out_tag="snr_fpf"):
        """
        Constructor of FalsePositiveModule.

        :param position: The x and y position (pix) where the SNR and FPF is calculated. Note that
                         the bottom left of the image is defined as (0, 0) so there is a -0.5
                         offset with respect to the DS9 coordinate system. Aperture photometry
                         corrects for the partial inclusion of pixels at the boundary.
        :type position: tuple
        :param aperture: Aperture radius (arcsec).
        :type aperture: float
        :param ignore: Ignore the two neighboring apertures that may contain self-subtraction from
                       the planet.
        :type ignore: bool
        :param name_in: Unique name of the module instance.
        :type name_in: str
        :param image_in_tag: Tag of the database entry with images that are read as input.
        :type image_in_tag: str
        :param snr_out_tag: Tag of the database entry that is written as output. The output format
                            is: (x position (pix), y position (pix), separation (arcsec), position
                            angle (deg), SNR, FPF). The position angle is measured in
                            counterclockwise direction with respect to the upward direction (i.e.,
                            East of North).
        :type snr_out_tag: str

        :return: None
        """

        super(FalsePositiveModule, self).__init__(name_in)

        self.m_image_in_port = self.add_input_port(image_in_tag)
        self.m_snr_out_port = self.add_output_port(snr_out_tag)

        self.m_position = position
        self.m_aperture = aperture
        self.m_ignore = ignore

    def run(self):
        """
        Run method of the module. Calculates the SNR and FPF for a specified position in a post-
        processed image with the Student's t-test (Mawet et al. 2014). This approach accounts
        for small sample statistics.

        :return: None
        """

        sys.stdout.write("Running FalsePositiveModule...")
        sys.stdout.flush()

        pixscale = self.m_image_in_port.get_attribute("PIXSCALE")
        self.m_aperture /= pixscale

        image = self.m_image_in_port.get_all()

        if image.ndim == 3:
            if image.shape[0] != 1:
                warnings.warn("Using the first image of %s." % self.m_image_in_port.tag)

            image = image[0, ]

        npix = image.shape[0]
        center = npix/2.

        if image.ndim > 2:
            raise ValueError("The image_in_tag should contain a 2D array.")

        sep = math.sqrt((center-self.m_position[0])**2.+(center-self.m_position[1])**2.)
        ang = (math.atan2(self.m_position[1]-center,
                          self.m_position[0]-center)*180./math.pi - 90.)%360.

        num_ap = int(math.pi*sep/self.m_aperture)
        ap_theta = np.linspace(0, 2.*math.pi, num_ap, endpoint=False)

        if self.m_ignore:
            num_ap -= 2
            ap_theta = np.delete(ap_theta, [1, np.size(ap_theta)-1])

        ap_phot = np.zeros(num_ap)
        for i, theta in enumerate(ap_theta):
            x_tmp = center + (self.m_position[0]-center)*math.cos(theta) - \
                             (self.m_position[1]-center)*math.sin(theta)
            y_tmp = center + (self.m_position[0]-center)*math.sin(theta) + \
                             (self.m_position[1]-center)*math.cos(theta)

            aperture = CircularAperture((x_tmp, y_tmp), self.m_aperture)
            phot_table = aperture_photometry(image, aperture, method='exact')
            ap_phot[i] = phot_table['aperture_sum']

        snr = (ap_phot[0] - np.mean(ap_phot[1:])) / \
              (np.std(ap_phot[1:]) * math.sqrt(1.+1./float(num_ap-1)))

        fpf = 1. - t.cdf(snr, num_ap-2)

        result = np.column_stack((self.m_position[0],
                                  self.m_position[1],
                                  sep*pixscale,
                                  ang,
                                  snr,
                                  fpf))

        self.m_snr_out_port.set_all(result)

        self.m_snr_out_port.add_history_information("Signal-to-noise ratio",
                                                    "Student's t-test")

        self.m_snr_out_port.copy_attributes_from_input_port(self.m_image_in_port)

        self.m_snr_out_port.close_port()

        sys.stdout.write(" [DONE]\n")
        sys.stdout.flush()


def _fake_planet(science,
                 psf,
                 parang,
                 position,
                 magnitude,
                 psf_scaling,
                 pixscale):
    """
    Internal function to inject fake planets into a cube of images. This function is similar to
    FakePlanetModule but does not require access to the PynPoint database.
    """

    radial = position[0]/pixscale
    theta = position[1]*math.pi/180. + math.pi/2.
    flux_ratio = 10.**(-magnitude/2.5)

    psf_size = image_size(psf)

    if psf_size != (science.shape[1], science.shape[2]):
        raise ValueError("The science images should have the same dimensions as the PSF template.")

    if psf.ndim == 3 and psf.shape[0] == 1:
        psf = np.squeeze(psf, axis=0)
    elif psf.ndim == 3 and psf.shape[0] != science.shape[0]:
        psf = np.mean(psf, axis=0)

    fake = np.copy(science)

    for i in range(fake.shape[0]):
        x_shift = radial*math.cos(theta-math.radians(parang[i]))
        y_shift = radial*math.sin(theta-math.radians(parang[i]))

        if psf.ndim == 2:
            psf_tmp = np.copy(psf)
        elif psf.ndim == 3:
            psf_tmp = np.copy(psf[i, ])

        psf_tmp = shift(psf_tmp,
                        (y_shift, x_shift),
                        order=5,
                        mode='reflect')

        fake[i, ] += psf_scaling*flux_ratio*psf_tmp

    return fake


def _psf_subtraction(images,
                     parang,
                     pca_number,
                     extra_rot):
    """
    Internal function for PSF subtraction with PCA.

    :param images: Stack of images, also used as reference images.
    :type images: ndarray
    :param parang: Angles (deg) for derotation of the images.
    :type parang: ndarray
    :param pca_number: Number of PCA components used for the PSF model.
    :type pca_number: int
    :param extra_rot: Additional rotation angle of the images (deg).
    :type extra_rot: float

    :return: Mean residuals of the PSF subtraction.
    :rtype: ndarray
    """

    pca = PCA(n_components=pca_number, svd_solver="arpack")

    images -= np.mean(images, axis=0)
    images_reshape = images.reshape((images.shape[0], images.shape[1]*images.shape[2]))

    pca.fit(images_reshape)

    pca_rep = np.matmul(pca.components_[:pca_number], images_reshape.T)
    pca_rep = np.vstack((pca_rep, np.zeros((0, images.shape[0])))).T

    model = pca.inverse_transform(pca_rep)
    model = model.reshape(images.shape)

    residuals = images - model

    for j, item in enumerate(-1.*parang):
        residuals[j, ] = rotate(residuals[j, ], item+extra_rot, reshape=False)

    return np.mean(residuals, axis=0)


def _lnprob(param,
            bounds,
            images,
            psf,
            mask,
            parang,
            psf_scaling,
            pixscale,
            pca_number,
            extra_rot,
            aperture):
    """
    Internal function for the log posterior function. Should be placed at the highest level of the
    Python module in order to be pickled.

    :param param: Tuple with the separation (arcsec), angle (deg), and contrast
                  (mag). The angle is measured in counterclockwise direction with
                  respect to the upward direction (i.e., East of North).
    :type param: tuple, float
    :param bounds: Tuple with the boundaries of the separation (arcsec), angle (deg),
                   and contrast (mag). Each set of boundaries is specified as a tuple.
    :type bounds: tuple, float
    :param images: Stack with images.
    :type images: ndarray
    :param psf: PSF template, either a single image (2D) or a cube (3D) with the dimensions
                equal to *image_in_tag*.
    :type psf: ndarray
    :param mask: Array with the circular mask (zeros) of the central and outer regions.
    :type mask: ndarray
    :param parang: Array with the angles for derotation.
    :type parang: ndarray
    :param psf_scaling: Additional scaling factor of the planet flux (e.g., to correct for a
                        neutral density filter). Should be negative in order to inject negative
                        fake planets.
    :type psf_scaling: float
    :param pixscale: Additional scaling factor of the planet flux (e.g., to correct for a neutral
                     density filter). Should be negative in order to inject negative fake planets.
    :type pixscale: float
    :param pca_number: Number of principle components used for the PSF subtraction.
    :type pca_number: int
    :param extra_rot: Additional rotation angle of the images (deg).
    :type extra_rot: float
    :param aperture: Circular aperture at the position specified in *param*.
    :type aperture: photutils.CircularAperture

    :return: Log posterior.
    :rtype float
    """

    def _lnprior():
        """
        Internal function for the log prior function.

        :return: Log prior.
        :rtype float
        """

        if bounds[0][0] <= param[0] <= bounds[0][1] and \
           bounds[1][0] <= param[1] <= bounds[1][1] and \
           bounds[2][0] <= param[2] <= bounds[2][1]:

            lnprior = 0.

        else:

            lnprior = -np.inf

        return lnprior

    def _lnlike():
        """
        Internal function for the log likelihood function. Noise of each pixel is assumed to be
        given by photon noise only (see Wertz et al. 2017 for details).

        :return: Log likelihood.
        :rtype float
        """

        sep, ang, mag = param

        fake = _fake_planet(images,
                            psf,
                            parang-extra_rot,
                            (sep, ang),
                            mag,
                            psf_scaling,
                            pixscale)

        fake *= mask

        im_res = _psf_subtraction(fake,
                                  parang,
                                  pca_number,
                                  extra_rot)

        phot_table = aperture_photometry(np.abs(im_res), aperture, method='exact')

        return -0.5*phot_table['aperture_sum'][0]

    lnprior = _lnprior()

    if math.isinf(lnprior):
        lnprob = -np.inf

    else:
        lnprob = lnprior + _lnlike()

    return lnprob


class MCMCsamplingModule(ProcessingModule):
    """
    Module to determine the contrast and position of a planet with an affine invariant Markov chain
    Monte Carlo (MCMC) ensemble sampler.
    """

    def __init__(self,
                 param,
                 bounds,
                 name_in="mcmc_sampling",
                 image_in_tag="im_arr",
                 psf_in_tag="im_arr",
                 chain_out_tag="chain",
                 nwalkers=100,
                 nsteps=200,
                 psf_scaling=-1.,
                 pca_number=20,
                 aperture=0.1,
                 mask=None,
                 extra_rot=0.,
                 **kwargs):
        """
        Constructor of MCMCsamplingModule.

        :param param: Tuple with the separation (arcsec), angle (deg), and contrast (mag). The
                      angle is measured in counterclockwise direction with respect to the upward
                      direction (i.e., East of North). The specified separation and angle are also
                      used as fixed position for the aperture.
        :type param: tuple, float
        :param bounds: Tuple with the boundaries of the separation (arcsec), angle (deg), and
                       contrast (mag). Each set of boundaries is specified as a tuple.
        :type bounds: tuple, float
        :param name_in: Unique name of the module instance.
        :type name_in: str
        :param image_in_tag: Tag of the database entry with images that are read as input.
        :type image_in_tag: str
        :param psf_in_tag: Tag of the database entry with the reference PSF that is used as fake
                           planet. Can be either a single image (2D) or a cube (3D) with the
                           dimensions equal to *image_in_tag*.
        :type psf_in_tag: str
        :param chain_out_tag: Tag of the database entry with the Markov chain that is written as
                              output. The shape of the array is (nwalkers*nsteps, 3).
        :type chain_out_tag: str
        :param nwalkers: Number of ensemble members (i.e. chains).
        :type nwalkers: int
        :param nsteps: Number of steps to run per walker.
        :type nsteps: int
        :param psf_scaling: Additional scaling factor of the planet flux (e.g., to correct for a
                            neutral density filter). Should be negative in order to inject
                            negative fake planets.
        :type psf_scaling: float
        :param pca_number: Number of principle components used for the PSF subtraction.
        :type pca_number: int
        :param aperture: Aperture radius (arcsec) at the position specified in *param*.
        :type aperture: float
        :param mask: Inner and outer mask radius (arcsec) for the PSF subtraction. Both elements of
                     the tuple can be set to None.
        :type mask: tuple, float
        :param extra_rot: Additional rotation angle of the images (deg).
        :type extra_rot: float
        :param \**kwargs:
            See below.

        :Keyword arguments:
             * **scale** (*float*) -- The proposal scale parameter (Goodman & Weare 2010).
             * **sigma** (*tuple*) -- Tuple with the standard deviations that randomly initializes
                                      the start positions of the walkers in a small ball around the
                                      a priori preferred position (*param*). The tuple should
                                      contain three values (*float*): the separation (arcsec),
                                      position angle (deg), and contrast (mag).

        :return: None
        """

        if "scale" in kwargs:
            self.m_scale = kwargs["scale"]
        else:
            self.m_scale = 2.

        if "sigma" in kwargs:
            self.m_sigma = kwargs["sigma"]
        else:
            self.m_sigma = (1e-5, 1e-3, 1e-3)

        super(MCMCsamplingModule, self).__init__(name_in)

        self.m_image_in_port = self.add_input_port(image_in_tag)
        if psf_in_tag == image_in_tag:
            self.m_psf_in_port = self.m_image_in_port
        else:
            self.m_psf_in_port = self.add_input_port(psf_in_tag)
        self.m_chain_out_port = self.add_output_port(chain_out_tag)

        self.m_param = param
        self.m_bounds = bounds
        self.m_nwalkers = nwalkers
        self.m_nsteps = nsteps
        self.m_psf_scaling = psf_scaling
        self.m_pca_number = pca_number
        self.m_aperture = aperture
        self.m_extra_rot = extra_rot

        if mask is None:
            self.m_mask = np.asarray((None, None))
        else:
            self.m_mask = np.asarray(mask)

    def run(self):
        """
        Run method of the module. Shifts the reference PSF to the location of the fake planet
        with an additional correction for the parallactic angle and writes the stack with images
        with the injected planet signal.

        :return: None
        """

        if not isinstance(self.m_param, tuple) or len(self.m_param) != 3:
            raise TypeError("The param argument should contain a tuple with the approximate "
                            "separation (arcsec), position angle (deg), and contrast (mag).")

        if not isinstance(self.m_bounds, tuple) or len(self.m_bounds) != 3:
            raise TypeError("The bounds argument should contain a tuple with three tuples for "
                            "the boundaries of the separation (arcsec), position angle (deg), and "
                            "contrast (mag).")

        if not isinstance(self.m_sigma, tuple) or len(self.m_sigma) != 3:
            raise TypeError("The sigma argument should contain a tuple with the standard "
                            "deviation of the separation (arcsec), position angle (deg), "
                            "and contrast (mag) that is used to sample the starting position "
                            "of the walkers.")

        ndim = 3

        cpu = self._m_config_port.get_attribute("CPU")
        pixscale = self.m_image_in_port.get_attribute("PIXSCALE")
        parang = self.m_image_in_port.get_attribute("PARANG")

        self.m_aperture /= pixscale

        images = self.m_image_in_port.get_all()
        psf = self.m_psf_in_port.get_all()

        im_shape = image_size_port(self.m_image_in_port)

        if self.m_mask[0] is not None:
            self.m_mask[0] /= pixscale
        if self.m_mask[1] is not None:
            self.m_mask[1] /= pixscale

        mask = create_mask(im_shape, self.m_mask)

        center = self.m_image_in_port.get_shape()[1]/2.
        x_pos = center+self.m_param[0]*math.cos(math.radians(self.m_param[1]+90.))/pixscale
        y_pos = center+self.m_param[0]*math.sin(math.radians(self.m_param[1]+90.))/pixscale

        circ_ap = CircularAperture((x_pos, y_pos), self.m_aperture)

        initial = np.zeros((self.m_nwalkers, ndim))

        initial[:, 0] = self.m_param[0] + np.random.normal(0, self.m_sigma[0], self.m_nwalkers)
        initial[:, 1] = self.m_param[1] + np.random.normal(0, self.m_sigma[1], self.m_nwalkers)
        initial[:, 2] = self.m_param[2] + np.random.normal(0, self.m_sigma[2], self.m_nwalkers)

        sampler = emcee.EnsembleSampler(nwalkers=self.m_nwalkers,
                                        dim=ndim,
                                        lnpostfn=_lnprob,
                                        a=self.m_scale,
                                        args=([self.m_bounds,
                                               images,
                                               psf,
                                               mask,
                                               parang,
                                               self.m_psf_scaling,
                                               pixscale,
                                               self.m_pca_number,
                                               self.m_extra_rot,
                                               circ_ap]),
                                        threads=cpu)

        for i, _ in enumerate(sampler.sample(p0=initial, iterations=self.m_nsteps)):
            progress(i, self.m_nsteps, "Running MCMCsamplingModule...")

        sys.stdout.write("Running MCMCsamplingModule... [DONE]\n")
        sys.stdout.flush()

        self.m_chain_out_port.set_all(sampler.chain)
        self.m_chain_out_port.add_history_information("Flux and position", "MCMC sampling")
        self.m_chain_out_port.copy_attributes_from_input_port(self.m_image_in_port)
        self.m_chain_out_port.close_port()

        print "Mean acceptance fraction: {0:.3f}".format(np.mean(sampler.acceptance_fraction))

        try:
            autocorr = emcee.autocorr.integrated_time(sampler.flatchain,
                                                      low=10,
                                                      high=None,
                                                      step=1,
                                                      c=10,
                                                      full_output=False,
                                                      axis=0,
                                                      fast=False)

            print "Integrated autocorrelation time =", autocorr

        except emcee.autocorr.AutocorrError:
            print "The chain is too short to reliably estimate the autocorrelation time. [WARNING]"


class AperturePhotometryModule(ProcessingModule):
    """
    Module for calculating the counts within a circular region.
    """

    def __init__(self,
                 radius=0.1,
                 position=None,
                 name_in="aperture_photometry",
                 image_in_tag="im_arr",
                 phot_out_tag="photometry"):
        """
        Constructor of AperturePhotometryModule.

        :param radius: Radius (arcsec) of the circular aperture.
        :type radius: int
        :param position: Center position (pix) of the aperture, (x, y). The center of the image
                         will be used if set to None.
        :type position: tuple, float
        :param name_in: Unique name of the module instance.
        :type name_in: str
        :param image_in_tag: Tag of the database entry that is read as input.
        :type image_in_tag: str
        :param phot_out_tag: Tag of the database entry with the photometry values that are written
                             as output.
        :type phot_out_tag: str

        :return: None
        """

        super(AperturePhotometryModule, self).__init__(name_in)

        self.m_image_in_port = self.add_input_port(image_in_tag)
        self.m_phot_out_port = self.add_output_port(phot_out_tag)

        self.m_radius = radius
        self.m_position = position

    def run(self):
        """
        Run method of the module. Calculates the counts for each frames and saves the values
        in the database.

        :return: None
        """

        def _photometry(image, aperture):
            photo = aperture_photometry(image, aperture, method='exact')
            return photo['aperture_sum']

        self.m_phot_out_port.del_all_data()
        self.m_phot_out_port.del_all_attributes()

        pixscale = self.m_image_in_port.get_attribute("PIXSCALE")
        self.m_radius /= pixscale

        size = self.m_image_in_port.get_shape()[1]

        if self.m_position is None:
            self.m_position = (size/2., size/2.)

        # Position in CircularAperture is defined as (x, y)
        aperture = CircularAperture(self.m_position, self.m_radius)

        self.apply_function_to_images(_photometry,
                                      self.m_image_in_port,
                                      self.m_phot_out_port,
                                      "Running AperturePhotometryModule...",
                                      func_args=(aperture,))

        self.m_phot_out_port.copy_attributes_from_input_port(self.m_image_in_port)
        self.m_phot_out_port.add_history_information("Aperture photometry",
                                                     "radius = "+str(self.m_radius*pixscale))
        self.m_phot_out_port.close_port()
