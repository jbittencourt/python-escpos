#!/usr/bin/env python

from distutils.core import setup

setup(name='escpos',
      version='1.0',
      description='Support for ESC/POS Thermic Printers',
      author='Juliano Bittencourt',
      author_email='juliano@hardfunstudios.com',
      url='https://github.com/jbittencourt/python-escpos',
      packages=['escpos'],
      install_requires=[
          "pyusb >= 1.0",
          "PIL >= 1.1.7",
      ],
     )