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

class Subdivision(BaseItem):
    _fieldnames = ['code', 'name', 'parent_code', 'type']
    _prettyprintfields = ['code', 'name', 'type']
    
    @property
    def parent(self):
        if self.parent_code != '':
            from .subdivisions import subdivisions
            return subdivisions.get(code=self.parent_code)
        else:
            return None
        
    @property
    def country_alpha_2(self):
        return self.code.split('-')[0]
    
    @property
    def country(self):
        from .countries import countries
        return countries.get(alpha_2=self.country_alpha_2)

class SubdivisionsCollection(BaseCollection):
    data_class_base = Subdivision

subdivisions = SubdivisionsCollection(Path(DATABASEDIR) / '3166_2_subdivisions_golden.csv')
