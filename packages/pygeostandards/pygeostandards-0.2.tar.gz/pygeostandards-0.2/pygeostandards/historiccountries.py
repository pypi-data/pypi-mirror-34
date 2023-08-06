#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Historic Countries 
no longer in existence in ISO-3166.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection

class HistoricCountry(BaseItem):
    _fieldnames = ['alpha_2', 'alpha_3', 'alpha_4', 'name', 'numeric_code', 
                   'continent_alpha_2', 'withdrawal_date']

class HistoricCountriesCollection(BaseCollection):
    _data_class_base = HistoricCountry
    _no_index = ['numeric_code','withdrawal_date']

historiccountries = HistoricCountriesCollection('3166_3_historiccountries_golden.csv')
