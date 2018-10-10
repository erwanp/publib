import os
from setuptools import setup, find_packages
import codecs
from os.path import join, dirname
from setuptips import yield_sphinx_only_markup

long_description = 'Produce publication-level quality images on top of Matplotlib, '+\
	'with a simple call to a couple functions at the start and end of your script.'
if os.path.exists('README.rst'):
	readme_lines = codecs.open('README.rst', encoding="utf-8").readlines()
	long_description = ''.join(yield_sphinx_only_markup(readme_lines))

# Read version number from file
with open(join(dirname(__file__),'publib', '__version__.txt')) as version_file:
    __version__ = version_file.read().strip()

setup(name='publib',
      version=__version__,
      description='Produce publication-level quality images on top of Matplotlib',
    	long_description=long_description,
      url='https://github.com/erwanp/publib',
      author='Erwan Pannier',
      author_email='erwan.pannier@gmail.com',
      license='MIT License',
      packages=find_packages(),
      keywords=["origin", "styles", "matplotlib"],
      install_requires=[
          #'matplotlib>=1.4.1',
           #'numpy', # for testing only. Should make this an optional requirement. 
          'six', 
		  ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Operating System :: OS Independent"],
	  include_package_data=True,
      zip_safe=False)
