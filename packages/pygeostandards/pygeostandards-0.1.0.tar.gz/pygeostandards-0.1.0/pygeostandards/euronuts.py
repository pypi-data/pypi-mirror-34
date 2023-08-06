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

class EuroNuts(BaseItem):
    _fieldnames = ['order', 'level', 'numeric_code', 
                   'parent_numeric_code', 'nuts_code', 'name']
    _prettyprintfields = ['nuts_code', 'name']
    
    @property
    def country_alpha_2(self):
        return self.nuts_code[0:2]
        
    @property
    def country(self):
        from .countries import countries
        return countries.get(alpha_2=self.country_alpha_2)
    
    @property
    def parent(self):
        if self.parent_numeric_code != '':
            from .euronuts import euronuts
            return euronuts.get(numeric_code=self.parent_numeric_code)
        else:
            return None
    
class EuroNutsCollection(BaseCollection):
    data_class_base = EuroNuts
    no_index = ['order', 'level', 'parent_numeric_code']

euronuts = EuroNutsCollection(Path(DATABASEDIR) / 'nuts_2016_golden.csv')
