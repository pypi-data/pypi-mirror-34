#from numpy.distutils.core import setup
#from numpy.distutils.extension import Extension
from setuptools import setup, Extension

setup(name='rampy',
      version='0.3.6',
      description='A Python module containing functions to treat spectroscopic (XANES, Raman, IR...) data',
      url='https://github.com/charlesll/rampy',
      author='Charles Le Losq',
      author_email='charles.lelosq@anu.edu.au',
      license='GNU-GPLv2',
      packages=['rampy', 'rampy.tests'],
      install_requires=['numpy>=1.12','scipy','sklearn','pandas','cvxpy'],
      zip_safe=False)
