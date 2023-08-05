"""
Functions for the test cases.
"""

import os
import math
import fileinput

import h5py
import numpy as np
from scipy.ndimage import shift
from astropy.io import fits


def create_config(filename):
    """
    Create a configuration file.
    """

    file_obj = open(filename, 'w')

    file_obj.write('[header]\n\n')
    file_obj.write('INSTRUMENT: INSTRUME\n')
    file_obj.write('NFRAMES: NAXIS3\n')
    file_obj.write('EXP_NO: ESO DET EXP NO\n')
    file_obj.write('NDIT: ESO DET NDIT\n')
    file_obj.write('PARANG_START: ESO ADA POSANG\n')
    file_obj.write('PARANG_END: ESO ADA POSANG END\n')
    file_obj.write('DITHER_X: ESO SEQ CUMOFFSETX\n')
    file_obj.write('DITHER_Y: ESO SEQ CUMOFFSETY\n')
    file_obj.write('DIT: None\n')
    file_obj.write('LATITUDE: None\n')
    file_obj.write('LONGITUDE: None\n')
    file_obj.write('PUPIL: None\n')
    file_obj.write('DATE: None\n')
    file_obj.write('RA: None\n')
    file_obj.write('DEC: None\n\n')
    file_obj.write('[settings]\n\n')
    file_obj.write('PIXSCALE: 0.027\n')
    file_obj.write('MEMORY: 100\n')
    file_obj.write('CPU: 1\n')

    file_obj.close()

def prepare_pca_tests(path):
    """
    Create the images and configuration file for the test cases of the PCA PSF subtraction.
    """

    image1 = np.loadtxt(path + "/test_data/image1.dat")
    image2 = np.loadtxt(path + "/test_data/image2.dat")
    image3 = np.loadtxt(path + "/test_data/image3.dat")
    image4 = np.loadtxt(path + "/test_data/image4.dat")

    hdu = fits.PrimaryHDU()
    header = hdu.header
    header['INSTRUME'] = "IMAGER"
    header['HIERARCH ESO DET EXP NO'] = 1
    header['HIERARCH ESO DET NDIT'] = 1
    header['HIERARCH ESO ADA POSANG'] = 1.
    header['HIERARCH ESO ADA POSANG END'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETX'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETY'] = 1.
    header['PARANG'] = -17.3261
    header['PARANG'] = -17.3261
    hdu.data = image1
    hdu.writeto(path+"/test_data/image1.fits")

    hdu = fits.PrimaryHDU()
    header = hdu.header
    header['INSTRUME'] = "IMAGER"
    header['HIERARCH ESO DET EXP NO'] = 2
    header['HIERARCH ESO DET NDIT'] = 1
    header['HIERARCH ESO ADA POSANG'] = 1.
    header['HIERARCH ESO ADA POSANG END'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETX'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETY'] = 1.
    header['PARANG'] = -17.1720
    hdu.data = image2
    hdu.writeto(path+"/test_data/image2.fits")

    hdu = fits.PrimaryHDU()
    header = hdu.header
    header['INSTRUME'] = "IMAGER"
    header['HIERARCH ESO DET EXP NO'] = 3
    header['HIERARCH ESO DET NDIT'] = 1
    header['HIERARCH ESO ADA POSANG'] = 1.
    header['HIERARCH ESO ADA POSANG END'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETX'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETY'] = 1.
    header['PARANG'] = -17.0143
    hdu.data = image3
    hdu.writeto(path+"/test_data/image3.fits")

    hdu = fits.PrimaryHDU()
    header = hdu.header
    header['INSTRUME'] = "IMAGER"
    header['HIERARCH ESO DET EXP NO'] = 4
    header['HIERARCH ESO DET NDIT'] = 1
    header['HIERARCH ESO ADA POSANG'] = 1.
    header['HIERARCH ESO ADA POSANG END'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETX'] = 1.
    header['HIERARCH ESO SEQ CUMOFFSETY'] = 1.
    header['PARANG'] = -16.6004
    hdu.data = image4
    hdu.writeto(path+"/test_data/image4.fits")

    config_file = path+"/test_data/PynPoint_config.ini"
    create_config(config_file)

    for lines in fileinput.FileInput(config_file, inplace=1):
        lines = lines.replace("PIXSCALE: 0.027\n", "PIXSCALE: 0.01\n")
        print lines # writes to file

def remove_psf_test_data(path):
    """
    Remove FITS files that were created for the test cases of the PSF subtraction.
    """

    os.remove(os.path.join(path, "test_data/image1.fits"))
    os.remove(os.path.join(path, "test_data/image2.fits"))
    os.remove(os.path.join(path, "test_data/image3.fits"))
    os.remove(os.path.join(path, "test_data/image4.fits"))
    os.remove(os.path.join(path, "test_data/PynPoint_database.hdf5"))
    os.remove(os.path.join(path, "test_data/PynPoint_config.ini"))

def create_random(path):
    """
    Create a stack of images with Gaussian distributed pixel values.
    """

    file_in = path + "/PynPoint_database.hdf5"

    np.random.seed(1)
    images = np.random.normal(loc=0, scale=2e-4, size=(10, 100, 100))
    parang = np.arange(1, 11, 1)

    h5f = h5py.File(file_in, "w")
    dset = h5f.create_dataset("images", data=images)
    dset.attrs['PIXSCALE'] = 0.01
    h5f.create_dataset("header_images/PARANG", data=parang)
    h5f.close()

def create_fits(filename, image, ndit, exp_no, parang, x0, y0):
    """
    Create a FITS file with images and header information
    """

    hdu = fits.PrimaryHDU()
    header = hdu.header
    header['INSTRUME'] = 'IMAGER'
    header['HIERARCH ESO DET EXP NO'] = 1.
    header['HIERARCH ESO DET NDIT'] = ndit
    header['HIERARCH ESO DET EXP NO'] = exp_no
    header['HIERARCH ESO ADA POSANG'] = parang[0]
    header['HIERARCH ESO ADA POSANG END'] = parang[1]
    header['HIERARCH ESO SEQ CUMOFFSETX'] = x0
    header['HIERARCH ESO SEQ CUMOFFSETY'] = y0
    hdu.data = image
    hdu.writeto(filename)

def create_fake(file_start, ndit, nframes, exp_no, npix, fwhm, x0, y0, angles, sep, contrast):
    """
    Create ADI test data with fake planets.
    """

    parang = []
    for i, item in enumerate(angles):
        for j in range(ndit[i]):
            parang.append(item[0]+float(j)*(item[1]-item[0])/float(ndit[i]))

    if fwhm is not None or contrast is not None:
        sigma = fwhm / (2.*math.sqrt(2.*math.log(2.)))

    x = np.arange(0., npix[0], 1.)
    y = np.arange(0., npix[1], 1.)
    xx, yy = np.meshgrid(x, y)

    np.random.seed(1)

    count = 0
    for j, item in enumerate(nframes):
        image = np.zeros((item, npix[1], npix[0]))

        for i in range(ndit[j]):
            noise = np.random.normal(loc=0, scale=2e-4, size=(npix[1], npix[0]))
            image[i, 0:npix[1], 0:npix[0]] = noise

            if fwhm is not None:
                star = (1./(2.*np.pi*sigma**2))*np.exp(-((xx-x0[j])**2+(yy-y0[j])**2)/(2.*sigma**2))
                image[i, 0:npix[1], 0:npix[0]] += star

            if contrast is not None and sep is not None:
                planet = contrast*(1./(2.*np.pi*sigma**2))*np.exp(-((xx-x0[j])**2+(yy-y0[j])**2)/(2.*sigma**2))
                x_shift = sep*math.cos(parang[count]*math.pi/180.)
                y_shift = sep*math.sin(parang[count]*math.pi/180.)
                planet = shift(planet, (x_shift, y_shift), order=5)
                image[i, 0:npix[1], 0:npix[0]] += planet

            count += 1

        filename = file_start+str(j+1).zfill(2)+'.fits'
        create_fits(filename, image, ndit[j], exp_no[j], angles[j], x0[j]-npix[0]/2., y0[j]-npix[1]/2.)

def create_star_data(path, npix_x, npix_y, x0, y0, parang_start, parang_end):
    """
    Create data with a stellar PSF and Gaussian noise.
    """

    fwhm = 3
    ndit = 10
    naxis3 = ndit
    exp_no = [1, 2, 3, 4]

    np.random.seed(1)

    for j, item in enumerate(exp_no):
        sigma = fwhm / (2. * math.sqrt(2.*math.log(2.)))

        x = y = np.arange(0., npix_x, 1.)
        xx, yy = np.meshgrid(x, y)

        image = np.zeros((naxis3, npix_x, npix_y))

        for i in range(ndit):
            star = (1./(2.*np.pi*sigma**2)) * np.exp(-((xx-x0[j])**2 + (yy-y0[j])**2) / (2.*sigma**2))
            noise = np.random.normal(loc=0, scale=2e-4, size=(npix_x, npix_x))
            image[i, 0:npix_x, 0:npix_x] = star+noise

        hdu = fits.PrimaryHDU()
        header = hdu.header
        header['INSTRUME'] = 'IMAGER'
        header['HIERARCH ESO DET EXP NO'] = item
        header['HIERARCH ESO DET NDIT'] = ndit
        header['HIERARCH ESO ADA POSANG'] = parang_start[j]
        header['HIERARCH ESO ADA POSANG END'] = parang_end[j]
        header['HIERARCH ESO SEQ CUMOFFSETX'] = "None"
        header['HIERARCH ESO SEQ CUMOFFSETY'] = "None"
        hdu.data = image
        hdu.writeto(os.path.join(path, 'image'+str(j+1).zfill(2)+'.fits'))
