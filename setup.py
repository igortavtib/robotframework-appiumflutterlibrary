#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup, find_packages

ROOT = dirname(abspath(__file__))

setup(name='robotframework-appiumflutterlibrary',
      version='1.0.0-beta.1',
      description='Robot Framework Mobile flutter app testing library for Appium Client Android & iOS & Web',
      long_description=open(join(ROOT, 'README.rst')).read(),
      author='Igor Augusto',
      author_email='igortavtib@gmail.com',
      url='https://github.com/igortavtib/robotframework-appiumflutterlibrary',
      license='Apache License 2.0',
      keywords='robotframework flutter testing testautomation mobile appium webdriver app android ios',
      platforms='any',
      classifiers=[
          "Development Status :: 1 - Planning",
          "Framework :: Robot Framework :: Library",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          'Topic :: Software Development :: Quality Assurance',
          "Topic :: Software Development :: Testing",
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      install_requires=[
          'decorator >= 3.3.2',
          'robotframework >= 2.6.0',
          'docutils >= 0.8.1',
          'Appium-Python-Client >= 1.1.0',
          'selenium >= 2.47.1',
          'kitchen >= 1.2.4',
          'six >= 1.10.0',
          'Appium-Flutter-Finder >= 0.3.0'
      ],
      packages=find_packages(exclude=["tests"]),
      include_package_data=True,
      )
