# -*- coding: utf-8 -*-
import setuptools
#from sphinx.setup_command import BuildDoc

from pygeostandards.info import VERSION, RELEASE, PACKAGENAME, AUTHOR, AUTHOR_EMAIL, DATADIR

with open("README.rst", "r") as fh:
    long_description = fh.read()

#cmdclass = {'build_sphinx': BuildDoc}

setuptools.setup(
    name=PACKAGENAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    
    description="A small package to take care of geographic and other standard information.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    
    url="https://github.com/mattange/" + PACKAGENAME,
    project_urls = {
            'Source': "https://github.com/mattange/" + PACKAGENAME,
            'Bug Reports': "https://github.com/mattange/" + PACKAGENAME + "/issues",
        },
    
    package_data = {
            'sample': [DATADIR + "/15924_scripts_golden.csv",
                       DATADIR + "/3166_1_continents_golden.csv",
                       DATADIR + "/3166_1_countries_golden.csv",
                       DATADIR + "/3166_2_subdivisions_golden.csv",
                       DATADIR + "/3166_3_historiccountries_golden.csv",
                       DATADIR + "/4217_currencies_golden.csv",
                       DATADIR + "/639_languages_golden.csv",
                       DATADIR + "/euroregions_golden.csv",
                       DATADIR + "/intermediate_regions_golden.csv",
                       DATADIR + "/nuts_2016_golden.csv",
                       DATADIR + "/regions_golden.csv",
                       DATADIR + "/sub_regions_golden.csv"
                       ]
        },
    
    
    packages=setuptools.find_packages(exclude=['docs','examples','tests']),
    
    python_requires = '>=3.5',
    
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries"
    ),
    keywords='ISO country geography NUTS currencies languages regions scripts',
    
    #documentation aspects
#    cmdclass=cmdclass,
#    command_options={
#            'build_sphinx': {
#                'project': ('setup.py', PACKAGENAME),
#                'version': ('setup.py', VERSION),
#                'release': ('setup.py', RELEASE),
#                'source_dir': ('setup.py', 'docs/source')               
#                }
#        }
)

