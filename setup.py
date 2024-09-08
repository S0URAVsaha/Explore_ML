"""
This setup.py will be responsible in creating this ML application as a package
By using this, all the required packages will be installed automatically.
list of required packages will be found in requirement.txt file and use the below command to install packages
pip install -r requirements.txt 
-e . is the indication in requirments.txt file that setup.py need to be executed
"""

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this is a function which will return list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name= 'explore_ml',
    version='0.0.1',
    author = 'sourav',
    author_email= 'sourav.saha@anwargroup.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)