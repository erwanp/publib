from setuptools import setup

setup(name='publib',
      version='0.1.2',
      description='Produce publication-level quality images on top of Matplotlib',
	  long_description='Some predefined styles',
      url='github.com/rainwear/publib',
      author='Erwan Pannier',
      author_email='erwan.pannier@gmail.com',
      license='BSD-3',
      packages=['publib'],
      install_requires=[
          'matplotlib>=1.4.1',
		  ],
	  include_package_data=True,
      zip_safe=False)