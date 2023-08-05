import os
import warnings

import numpy as np

from PynPoint.Core.Pypeline import Pypeline
from PynPoint.IOmodules.FitsReading import FitsReadingModule
from PynPoint.ProcessingModules.PSFpreparation import AngleInterpolationModule
from PynPoint.ProcessingModules.PSFSubtractionPCA import PcaPsfSubtractionModule
from PynPoint.Util.TestTools import create_config, create_fake

warnings.simplefilter("always")

limit = 1e-10

def setup_module():
    create_fake(file_start=os.path.dirname(__file__)+"/image",
                ndit=[20, 20, 20, 20],
                nframes=[20, 20, 20, 20],
                exp_no=[1, 2, 3, 4],
                npix=(100, 100),
                fwhm=3.,
                x0=[50, 50, 50, 50],
                y0=[50, 50, 50, 50],
                angles=[[0., 25.], [25., 50.], [50., 75.], [75., 100.]],
                sep=10.,
                contrast=3e-3)

    create_config(os.path.dirname(__file__)+"/PynPoint_config.ini")

def teardown_module():
    test_dir = os.path.dirname(__file__) + "/"

    for i in range(4):
        os.remove(test_dir + 'image'+str(i+1).zfill(2)+'.fits')

    os.remove(test_dir + 'PynPoint_database.hdf5')
    os.remove(test_dir + 'PynPoint_config.ini')

class TestPSFSubtractionPCA(object):

    def setup(self):
        self.test_dir = os.path.dirname(__file__) + "/"
        self.pipeline = Pypeline(self.test_dir, self.test_dir, self.test_dir)

    def test_psf_subtraction_pca(self):

        read = FitsReadingModule(name_in="read",
                                 image_tag="read")

        self.pipeline.add_module(read)

        angle = AngleInterpolationModule(name_in="angle",
                                         data_tag="read")

        self.pipeline.add_module(angle)

        pca = PcaPsfSubtractionModule(pca_numbers=(5, ),
                                      name_in="pca",
                                      images_in_tag="read",
                                      reference_in_tag="read",
                                      res_mean_tag="res_mean",
                                      res_median_tag="res_median",
                                      res_arr_out_tag="res_arr",
                                      res_rot_mean_clip_tag="res_clip",
                                      basis_out_tag="basis",
                                      extra_rot=-15.,
                                      verbose=True)

        self.pipeline.add_module(pca)

        self.pipeline.run()

        data = self.pipeline.get_data("read")
        assert np.allclose(data[0, 50, 50], 0.09798413502193708, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 0.00010063896953157961, rtol=limit, atol=0.)
        assert data.shape == (80, 100, 100)

        data = self.pipeline.get_data("res_mean")
        assert np.allclose(data[0, 50, 50], 1.947810457180298e-06, rtol=limit, atol=0.)
        assert np.allclose(data[0, 59, 46], 0.00016087655925993273, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 3.184676024912574e-08, rtol=limit, atol=0.)
        assert data.shape == (1, 100, 100)

        data = self.pipeline.get_data("res_median")
        assert np.allclose(data[0, 50, 50], -2.223389676715259e-06, rtol=limit, atol=0.)
        assert np.allclose(data[0, 59, 46], 0.00015493570876347953, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 1.250907785757355e-07, rtol=limit, atol=0.)
        assert data.shape == (1, 100, 100)

        data = self.pipeline.get_data("res_clip")
        assert np.allclose(data[0, 50, 50], 2.2828813434810948e-06, rtol=limit, atol=0.)
        assert np.allclose(data[0, 59, 46], 1.0816254290076103e-05, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 2.052077475694807e-06, rtol=limit, atol=0.)
        assert data.shape == (1, 100, 100)

        data = self.pipeline.get_data("res_arr5")
        assert np.allclose(data[0, 50, 50], -0.00010775091764735749, rtol=limit, atol=0.)
        assert np.allclose(data[0, 59, 46], 0.0001732810184783699, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 3.184676024912564e-08, rtol=limit, atol=0.)
        assert data.shape == (80, 100, 100)

        data = self.pipeline.get_data("basis")
        assert np.allclose(data[0, 50, 50], -0.005866797940467074, rtol=limit, atol=0.)
        assert np.allclose(data[0, 59, 46], 0.0010154680995154122, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), -4.708475279640416e-05, rtol=limit, atol=0.)
        assert data.shape == (5, 100, 100)
