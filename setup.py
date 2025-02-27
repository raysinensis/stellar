from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='STELLAR',
    version='0.99',
    packages=['.'],
    python_requires='>=3.8*'
)
