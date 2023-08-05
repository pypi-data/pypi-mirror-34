from setuptools import setup, find_packages
import sys, os

version = '1.0.22'

setup(name='pydawn',
      version=version,
      description="some useful tool",
      long_description="""\
            
      """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='palydawn',
      author='palydawn',
      author_email='palydawn@163.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'selenium', 'lxml', 'requests', 'matplotlib', 'numpy', 'burst_detection', 'chardet', 'pypinyin',
            'rsa', 'pycrypto'
            ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
