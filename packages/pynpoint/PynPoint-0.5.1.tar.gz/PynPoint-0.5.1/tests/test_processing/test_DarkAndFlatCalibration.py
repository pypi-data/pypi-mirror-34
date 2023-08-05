import os
import math
import warnings

import h5py
import numpy as np

from astropy.io import fits

from PynPoint.Core.Pypeline import Pypeline
from PynPoint.Core.DataIO import DataStorage
from PynPoint.IOmodules.FitsReading import FitsReadingModule
from PynPoint.ProcessingModules.DarkAndFlatCalibration import DarkCalibrationModule, FlatCalibrationModule
from PynPoint.Util.TestTools import create_config

warnings.simplefilter("always")

limit = 1e-10

def setup_module():
    file_in = os.path.dirname(__file__) + "/PynPoint_database.hdf5"

    np.random.seed(1)

    images = np.random.normal(loc=0, scale=2e-4, size=(10, 100, 100))
    dark = np.random.normal(loc=0, scale=2e-4, size=(10, 100, 100))
    flat = np.random.normal(loc=0, scale=2e-4, size=(10, 100, 100))

    h5f = h5py.File(file_in, "w")
    h5f.create_dataset("images", data=images)
    h5f.create_dataset("dark", data=dark)
    h5f.create_dataset("flat", data=flat)
    h5f.close()

    filename = os.path.dirname(__file__) + "/PynPoint_config.ini"
    create_config(filename)

def teardown_module():
    file_in = os.path.dirname(__file__) + "/PynPoint_database.hdf5"
    config_file = os.path.dirname(__file__) + "/PynPoint_config.ini"

    os.remove(file_in)
    os.remove(config_file)

class TestDarkAndFlatCalibration(object):

    def setup(self):
        self.test_dir = os.path.dirname(__file__) + "/"
        self.pipeline = Pypeline(self.test_dir, self.test_dir, self.test_dir)

    def test_dark_and_flat_calibration(self):

        dark = DarkCalibrationModule(name_in="dark",
                                     image_in_tag="images",
                                     dark_in_tag="dark",
                                     image_out_tag="dark_cal")

        self.pipeline.add_module(dark)

        flat = FlatCalibrationModule(name_in="flat",
                                     image_in_tag="dark_cal",
                                     flat_in_tag="flat",
                                     image_out_tag="flat_cal")

        self.pipeline.add_module(flat)

        self.pipeline.run()

        storage = DataStorage(self.test_dir+"/PynPoint_database.hdf5")
        storage.open_connection()

        data = storage.m_data_bank["dark"]
        assert np.allclose(data[0, 10, 10], 3.528694163309295e-05, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 7.368663496379876e-07, rtol=limit, atol=0.)

        data = storage.m_data_bank["flat"]
        assert np.allclose(data[0, 10, 10], -0.0004053528990466237, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), -4.056978234798532e-07, rtol=limit, atol=0.)

        storage.close_connection()
