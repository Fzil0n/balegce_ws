from setuptools import find_packages
from setuptools import setup

setup(
    name='balegce_controller',
    version='0.0.0',
    packages=find_packages(
        include=('balegce_controller', 'balegce_controller.*')),
)
