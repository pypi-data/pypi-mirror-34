from setuptools import setup  ,find_packages
import yxspkg
import sys


setup(name='yxspkg',   
      version=yxspkg.__version__,    
      description='My pypi module',    
      author='Blacksong',    
      author_email='blacksong@yeah.net',       
      url='https://github.com/blacksong',
      packages=find_packages(), 
      classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)   
