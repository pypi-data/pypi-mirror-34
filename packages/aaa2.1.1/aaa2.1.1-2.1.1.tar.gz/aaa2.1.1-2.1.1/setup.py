# -*- coding: utf-8 -*-

from distutils.core import setup
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here,"README.md"),"r") as fh:
    long_description=fh.read()

    
setup(

    name = 'aaa2.1.1',

    version = '2.1.1',

    keywords = ('simple', 'test'),

    description = 'just a simple test of vipkid',
    
    long_description=long_description,
    
    long_description_content_type="text/markdown",

    license = 'MIT',

    author = 'yin',

    author_email = 'yinmengmeng@vipkid.com.cn',

    packages = find_packages(),

    platforms = 'any',

    py_modules=['ROC.conRoc','ROC.roc','transform.txt2xml']

)

