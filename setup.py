"""Setup script."""
from setuptools import setup, find_packages

setup(
    name='deepSeg',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['Theano==0.8.2'],
    author='ckmarkoh',
    author_email='ckmarkoh@gmail.com',
    description='A deep learning Chinese Word Segmentation toolkit',
    package_data={
        '': ['model/*'],
    }
)
