#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 00:01:21 2018

@author: mattange
"""
from pathlib import Path

from .baseitem import BaseItem
from .basecollection import BaseCollection
from .info import DATABASEDIR

class Region(BaseItem):
    _fieldnames = ['name','code']
    _prettyprintfields = _fieldnames
        
    
class RegionsCollection(BaseCollection):
    data_class_base = Region

regions = RegionsCollection(Path(DATABASEDIR) / 'regions_golden.csv')
sub_regions = RegionsCollection(Path(DATABASEDIR) / 'sub_regions_golden.csv')
intermediate_regions = RegionsCollection(Path(DATABASEDIR) / 'intermediate_regions_golden.csv')