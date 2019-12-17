"""Micro_Weather_Service project."""

from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='micro_weather',
    version='0.1.0',
    license='none',
    description='call weather api and output weather data as a csv file',

    author='u-masato',
    author_email='masato.u20@gmail.com',
    url='https://github.com/u-masato/micro-weather-service',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=_requires_from_file('requirements.txt'),
    extras_require={},

    tests_require=["pytest"]
    ,
)
