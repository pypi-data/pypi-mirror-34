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

class Continent(BaseItem):
    """Continent
    
    Describes a continent via alpha_2 code and name.
    Provides a list of countries as a CountryCollection 
    in its property countries.
    
    """
    
    _fieldnames = ['alpha_2', 'name']
    _prettyprintfields = _fieldnames
    
    @property
    def countries(self):
        if not hasattr(self, '_countries_coll'):
            from .countries import countries, CountriesCollection
            countries.force_load()
            _countries_coll = CountriesCollection([c for c in countries.objects if c.continent_alpha_2 == self.alpha_2])
            self._countries_coll = _countries_coll
        return self._countries_coll

class ContinentsCollection(BaseCollection):
    """ContinentsCollection
    
    Contains a set of Continents.
    
    """
    
    data_class_base = Continent

continents = ContinentsCollection(Path(DATABASEDIR) / '3166_1_continents_golden.csv')
