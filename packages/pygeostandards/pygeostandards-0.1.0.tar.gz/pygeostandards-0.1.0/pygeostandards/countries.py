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

class Country(BaseItem):
    _fieldnames = ['alpha_2', 'alpha_3', 'name', 'numeric_code', 'independent', 
                   'official_name', 'continent_alpha_2', 
                   'region_code', 'sub_region_code', 'intermediate_region_code']
    _prettyprintfields = ['alpha_2', 'name', 'numeric_code']
    
    @property
    def independent(self):
        if self.fields['independent'] == "TRUE":
            return True
        else:
            return False
        
    @property
    def continent(self):
        from .continents import continents
        return continents.get(alpha_2=self.continent_alpha_2)

    @property
    def region(self):
        if self.region_code != '':
            from .regions import regions
            return regions.get(code=self.region_code)
        else:
            return None
     
    @property
    def sub_region(self):
        if self.sub_region_code != '':
            from .regions import sub_regions
            return sub_regions.get(code=self.sub_region_code)
        else:
            return None

    @property
    def intermediate_region(self):
        if self.intermediate_region_code != '':
            from .regions import intermediate_regions
            return intermediate_regions.get(code=self.intermediate_region_code)
        else:
            return None
    

class CountriesCollection(BaseCollection):
    data_class_base = Country
    no_index = ['continent_code', 'independent', 'region_code', 
                'sub_region_code', 'intermediate_region_code', 'continent_alpha_2']

countries = CountriesCollection(Path(DATABASEDIR) / '3166_1_countries_golden.csv')
