from setuptools import setup, find_packages
from typing import List

#Declaring variables for setp functions
PROJECT_NAME = "housing-predictor",
VERSION = "0.0.1",
AUTHOR = "Vishal Selvakumar"
DESCRIPTION = "This is the first end to end ML project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Decription: This function is going to return list f requirement
    mention in requirments.txt file

    return this function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description= DESCRIPTION,
packages = find_packages(), # we get all folders names that contains __init__.py that we wanted use it as library and will install those folders
install_requires = get_requirements_list()
)