from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MSM_PELE",
    version="1.1.1",
    author="Daniel Soler, Francesc Gilbert",
    author_email="daniel.soler@nostrumbiodiscovery.com",
    description="Monte Carlo Protein Energy Landscape Exploration (PELE) coupled with Markov State Model (MSM) analysis with the aim to calculate absolute free energies",
    long_description=long_description,
    url="https://github.com/danielSoler93/MSM_PELE",
    classifiers=["Programming Language :: Python :: 2",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
        ],
    packages=setuptools.find_packages(),
    install_requires=[
        'prody==1.8.1',
        'mdtraj',
	'future',
	'pyemma',
	'msmtools'
        ],
    )
