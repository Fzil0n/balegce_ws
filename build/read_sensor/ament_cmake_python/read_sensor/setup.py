from setuptools import find_packages
from setuptools import setup

setup(
    name='read_sensor',
    version='0.0.0',
    packages=find_packages(
        include=('read_sensor', 'read_sensor.*')),
)
