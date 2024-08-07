# setup.py
from setuptools import setup, find_packages

setup(
    name='GigaMath',
    version='1.0.0',
    packages=find_packages(),
    description='A collection of mathematical functions for various domains',
    author='Nagusame',
    url='https://github.com/NagusameCS/GigaMath',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)