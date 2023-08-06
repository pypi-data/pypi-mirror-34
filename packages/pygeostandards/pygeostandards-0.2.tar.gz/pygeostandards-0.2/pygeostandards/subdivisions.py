#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Subdivisions in ISO 3166-2.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection

class Subdivision(BaseItem):
    _fieldnames = ['code', 'name', 'parent_code', 'type']
    _prettyprintfields = ['code', 'name', 'type']
    
    @property
    def parent(self):
        if self.parent_code != '':
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
    _data_class_base = Subdivision

subdivisions = SubdivisionsCollection('3166_2_subdivisions_golden.csv')
