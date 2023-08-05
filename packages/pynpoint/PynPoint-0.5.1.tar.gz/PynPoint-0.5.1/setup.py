#!/usr/bin/env python

import sys
from setuptools import setup

readme = open('README.rst').read()

packages = ['PynPoint',
            'PynPoint.Core',
            'PynPoint.IOmodules',
            'PynPoint.ProcessingModules',
            'PynPoint.Util']

setup(
    name='PynPoint',
    version='0.5.1',
    description='Python package for processing and analysis of high-contrast imaging data',
    long_description=readme,
    author='Tomas Stolker, Markus Bonse, Sascha Quanz, Adam Amara',
    author_email='tomas.stolker@phys.ethz.ch',
    url='http://pynpoint.ethz.ch',
    packages=packages,
    package_dir={'PynPoint': 'PynPoint'},
    include_package_data=True,
    install_requires=['configparser',
                'h5py==2.6.0',
                'numpy',
                'numba==0.37.0',
                'scipy',
                'astropy<3.0.0',
                'photutils',
                'scikit-image',
                'scikit-learn',
                'opencv-python',
                'statsmodels==0.8.0',
                'PyWavelets',
                'matplotlib',
                'emcee',
                'ephem'],
    license='GPLv3',
    zip_safe=False,
    keywords='PynPoint',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=['pytest'],
)
