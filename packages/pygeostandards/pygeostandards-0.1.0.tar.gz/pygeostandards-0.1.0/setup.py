# -*- coding: utf-8 -*-
import setuptools
from sphinx.setup_command import BuildDoc


from pygeostandards.info import VERSION, PACKAGENAME, AUTHOR, AUTHOR_EMAIL

with open("README.rst", "r") as fh:
    long_description = fh.read()

cmdclass = {'build_sphinx': BuildDoc}

setuptools.setup(
    name=PACKAGENAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small package to take care of geographic and other standard information.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mattange/"+PACKAGENAME,
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='ISO country geography nuts currencies',
    
    #documentation aspects
    cmdclass=cmdclass,
    command_options={
            'build_sphinx': {
                'project': ('setup.py', PACKAGENAME),
                'version': ('setup.py', VERSION),
                'release': ('setup.py', VERSION),
                'source_dir': ('setup.py', 'docs/source')
                
                }
        }
)

