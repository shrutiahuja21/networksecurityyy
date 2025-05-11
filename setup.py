from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()  # Corrected "files" to "file"
            for line in lines:
                requirement = line.strip()  # Corrected "reqiuirement" to "requirement"
                if requirement and requirement != '-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst  # Corrected "requirement.lst" to "requirements_lst"

print(get_requirements())

