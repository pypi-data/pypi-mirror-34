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

class HistoricCountry(BaseItem):
    _fieldnames = ['alpha_2', 'alpha_3', 'alpha_4', 'name', 'numeric_code', 
                   'continent_alpha_2', 'withdrawal_date']

class HistoricCountriesCollection(BaseCollection):
    data_class_base = HistoricCountry
    no_index = ['numeric_code','withdrawal_date']

historiccountries = HistoricCountriesCollection(Path(DATABASEDIR) / '3166_3_historiccountries_golden.csv')
