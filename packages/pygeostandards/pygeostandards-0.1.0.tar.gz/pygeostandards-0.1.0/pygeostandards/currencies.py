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

class Currency(BaseItem):
    _fieldnames = ['alpha_code', 'name', 'numeric_code',
                   'minor_unit', 'country_alpha_2', 'peg', 'iso']
    _prettyprintfields = ['alpha_code', 'name', 'minor_unit']
   
    @property
    def iso(self):
        if self.fields['iso'] == "TRUE":
            return True
        else:
            return False
    
class CurrenciesCollection(BaseCollection):
    data_class_base = Currency
    no_index = ['minor_unit', 'country_alpha_2', 'peg', 'iso']

currencies = CurrenciesCollection(Path(DATABASEDIR) / '4217_currencies_golden.csv')

