#this file has been created to enable your project to be installed as a library in any other system
from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_NAME='requirements.txt'
HYPHEN_E='-e .'

def get_requirements()->List(str):
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_list=requirements_file.readlines()
    requirements_list=[req.replace("\n","") for req in requirements_list]
    if HYPHEN_E in requirements_list:
        requirements_list.remove(HYPHEN_E)
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="tuery",
    author_email="tuerydany19@gmail.com",
    packages = find_packages(),     #this function identifies the folders with init.py file and installs them as python package
    install_requires=get_requirements(),
)
