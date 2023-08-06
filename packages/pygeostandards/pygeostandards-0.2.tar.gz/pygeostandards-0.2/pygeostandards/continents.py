#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Continents.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""

from .baseitem import BaseItem
from .basecollection import BaseCollection


class Continent(BaseItem):
    """
    Continent
    
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
    """
    ContinentsCollection
    
    Contains a set of Continents.
    
    """
    _data_class_base = Continent

continents = ContinentsCollection('3166_1_continents_golden.csv')
"""
continents core collection

This is the base continents collection containing 
all 6 continents. Use this to get specific items.

"""


 
