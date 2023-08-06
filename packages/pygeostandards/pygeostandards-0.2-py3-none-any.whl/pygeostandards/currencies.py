#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Currencies in ISO-4217.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection


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
    _data_class_base = Currency
    _no_index = ['minor_unit', 'country_alpha_2', 'peg', 'iso']

currencies = CurrenciesCollection('4217_currencies_golden.csv')

