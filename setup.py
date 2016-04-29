import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
requirements = os.path.join(here, 'requirements.txt')

reqs = []
with open(requirements) as f:
    reqs = f.readlines()


setup(name='crasync',
      description='Use Python 3 async methods interactively',
      author='Bagrat Aznauryan',
      author_email='bagrat@aznauryan.org',
      packages=find_packages(),
      install_requires=reqs,
      version='0.0')
