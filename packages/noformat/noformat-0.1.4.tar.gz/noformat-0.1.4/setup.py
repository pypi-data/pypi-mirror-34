from setuptools import setup

import subprocess

try:  # Try to create an rst long_description from README.md
    args = "pandoc", "--to", "rst", "README.md"
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    print("README.md conversion to reStructuredText failed. Error:\n",
          error, "Setting long_description to None.")
    long_description = None

setup(
    name='noformat',
    version='0.1.4',
    packages=['noformat'],
    url='https://github.com/Palpatineli/noformat',
    download_url='https://github.com/Palpatineli/noformat/archive/0.1.4.tar.gz',
    license='GPLv3',
    author='Keji Li',
    author_email='mail@keji.li',
    description='save and load a structured collection of data as folder',
    long_description=long_description,
    extras_require={'pd': ['pandas']},
    install_requires=['numpy'],
    classifiers=["Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"]
)
