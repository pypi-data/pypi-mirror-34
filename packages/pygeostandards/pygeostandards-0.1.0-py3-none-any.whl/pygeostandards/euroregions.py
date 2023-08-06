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

class EuroRegion(BaseItem):
    _fieldnames = ['alpha_code', 'name']
    
class EuroRegionCollection(BaseCollection):
    data_class_base = EuroRegion

euroregions = EuroRegionCollection(Path(DATABASEDIR) / 'euroregions_golden.csv')
