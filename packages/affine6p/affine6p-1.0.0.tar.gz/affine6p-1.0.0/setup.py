# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="affine6p",
    version="1.0.0",
    description="The Python affine6p lib to estimate affine transformation parameters between two sets of 2D points",
    long_description=long_description,
    url="https://gitlab.com/yoshimoto/affine6p-py",
    author="Masahiro Yoshimoto",
    author_email="yoshimoto@flab.phys.nagoya-u.ac.jp",
    license="MIT",
    keywords="calculate affine transformation six parameters",
    packages=["affine6p"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        ]
)