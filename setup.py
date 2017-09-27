"""Setup script."""
from setuptools import setup, find_packages
from os.path import join, abspath, dirname

from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements(
    join(dirname(abspath(__file__)), 'requirements.txt'),
    session=PipSession()
)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='deepSeg',
    version='0.0.1',
    packages=find_packages(),
    install_requires=reqs,
    author='ckmarkoh',
    author_email='ckmarkoh@gmail.com',
    description='A deep learning Chinese Word Segmentation toolkit',
    package_data={
        '': ['model/*'],
    }
)
