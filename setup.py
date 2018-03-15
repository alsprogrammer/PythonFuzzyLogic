import fuzzpy
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='fuzzpy',
    version=fuzzpy.__version__,
    author='Aleksandr Saiapin',
    author_email='alstutor@gmail.com',
    packages=find_packages(),
    long_description="The library for working with fuzzy logic in python. This library is developed to be used for "
                     "modelling the fuzzy sets and fuzzy controllers. The library cab be used both in production and "
                     "for educational purposes.",
)
