# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

about = {}
with open(os.path.join(here, "text_autoencoder", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="text-autoencoder",
    version=about["__version__"],
    description="Yoctol Natural Language Text Autoencoder",
    license="MIT",
    author="Solumilken",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.14.2',
        'tensorflow==1.7.0',
        'bistiming==0.1.1',
        'mkdir-p==0.1.1',
        'pyyaml==3.13',
        'u-msgpack-python==2.5.0',
        'tqdm==4.23.4',
        'serving-utils==0.4.3',
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data=True,
)
