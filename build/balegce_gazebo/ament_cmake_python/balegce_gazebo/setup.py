from setuptools import find_packages
from setuptools import setup

setup(
    name='balegce_gazebo',
    version='0.0.0',
    packages=find_packages(
        include=('balegce_gazebo', 'balegce_gazebo.*')),
)
