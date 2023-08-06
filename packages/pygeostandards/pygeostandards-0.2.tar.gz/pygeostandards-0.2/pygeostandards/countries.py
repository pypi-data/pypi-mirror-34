#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Countries in ISO-3166.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection


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
    _data_class_base = Country
    _no_index = ['continent_code', 'independent', 'region_code', 
                'sub_region_code', 'intermediate_region_code', 'continent_alpha_2']

countries = CountriesCollection('3166_1_countries_golden.csv')
