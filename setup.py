import os
from setuptools import setup
import codecs

long_description = 'Convert a Python expression in a LaTeX formula'
if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', encoding="utf-8").read()
        
setup(name='publib',
      version='0.1.9',
      description='Produce publication-level quality images on top of Matplotlib',
    	long_description=long_description,
      url='https://github.com/erwanp/publib',
      author='Erwan Pannier',
      author_email='erwan.pannier@gmail.com',
      license='CeCILL-2.1',
      packages=['publib'],
      install_requires=[
          'matplotlib>=1.4.1',
          'numpy>=1.9.2', # for testing only. Should make this an optional requirement. 
		  ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Operating System :: OS Independent"],
	  include_package_data=True,
      zip_safe=False)