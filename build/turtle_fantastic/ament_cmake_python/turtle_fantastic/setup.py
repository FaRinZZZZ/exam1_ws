from setuptools import find_packages
from setuptools import setup

setup(
    name='turtle_fantastic',
    version='0.0.0',
    packages=find_packages(
        include=('turtle_fantastic', 'turtle_fantastic.*')),
)
