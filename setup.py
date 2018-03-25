import fuzzypy
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='fuzzypy',
    version=fuzzypy.__version__,
    author='Aleksandr Saiapin',
    author_email='alstutor@gmail.com',
    url='https://github.com/alsprogrammer/PythonFuzzyLogic',
    packages=find_packages(),
    test_suite='tests',
    long_description="The library for working with fuzzy logic in python. This library is developed to be used for "
                     "modelling the fuzzy sets and fuzzy controllers. The library cab be used both in production and "
                     "for educational purposes. For example please visit the github repository",
)
