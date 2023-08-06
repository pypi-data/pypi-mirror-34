#!/usr/bin/env python
from os.path import abspath, join as pjoin, dirname
import codecs
import re
import os
import sys

from setuptools import setup, find_packages

# Find the directory for the setup.py file 
setup_dir = abspath(dirname(sys.argv[0]))
def read(*parts):
    '''
    
    '''
    with codecs.open(pjoin(setup_dir, *parts), 'r') as fp:
        return fp.read()
    
def find_version(*file_paths):
    '''
    
    
    '''
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    
    raise RuntimeError("Unable to find version string.")

def setup_packages():
    pkgname = "clusterfunc"
    version = find_version(pkgname, "__init__.py")
    author = "Manodeep Sinha"
    author_email = "manodeep@gmail.com"
    base_url = "https://github.com/clusterfunc/clusterfunc"

    metadata = dict(
        name=pkgname,
        author=author,
        author_email=author_email,
        version=version,
        url=base_url,
        description='Python package for clustering statistics',
        long_description=read("README.rst"),
        license='MIT',
        packages=find_packages(),
        python_requires='>=3.5',
        setup_requires=['setuptools'],
    )

    setup(**metadata)
    

if __name__ == '__main__':
    setup_packages()
