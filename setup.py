from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Read requirements.txt and return list of requirements."""
    with open(file_path, encoding='utf-8-sig') as file_obj:
        # 'utf-8-sig' will automatically remove BOM if present
        requirements = [line.strip() for line in file_obj if line.strip() and not line.startswith('#')]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

# ---------------------------------------------------------------------------------------------------------------------------
# def get_requirements(file_path: str) -> List[str]:
#     # this function will return the list of requirements
#     requirements = []
#     with open(file_path) as file_obj: # as temporary file object
#         requirements = file_obj.readlines()
        
#     requirements = [req.replace("\n", "") for req in requirements]

#     if HYPEN_E_DOT in requirements:
#         requirements.remove(HYPEN_E_DOT)
    
#     return requirements
# ---------------------------------------------------------------------------------------------------------------------------

setup(
    name='student-performance-predictor',
    version='0.0.1',
    description='An end-to-end ML Project',
    author='Dipak Pulami Magar',
    author_email='dpm.it24800@gmail.com',
    packages=find_packages(), # Automatically discover and include all packages
    install_requires=get_requirements('requirements.txt') # install_requires=['pandas', 'numpy', 'seaborn']
    # Other potential arguments: long_description, license, url, entry_points
)