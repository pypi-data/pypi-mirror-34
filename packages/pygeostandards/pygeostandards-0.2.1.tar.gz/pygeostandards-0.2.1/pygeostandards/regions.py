#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Regions, Subregions and Intermediate 
regions. This is to be used in conjunction with the countries, 
as each country is normally assigned a region (and possibly a 
subregion and intermediate region).

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection

class Region(BaseItem):
    _fieldnames = ['name','code']
    _prettyprintfields = _fieldnames
        
    
class RegionsCollection(BaseCollection):
    _data_class_base = Region

regions = RegionsCollection('regions_golden.csv')
sub_regions = RegionsCollection('sub_regions_golden.csv')
intermediate_regions = RegionsCollection('intermediate_regions_golden.csv')