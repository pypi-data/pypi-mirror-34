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

class Language(BaseItem):
    _fieldnames = ['language_family','name','native_name',
                   'alpha_2','alpha_3', 'alpha_3_b', 'alpha_3_639_3',
                   'macrolanguage', 'parent_alpha_3', 'notes']
    _prettyprintfields = ['alpha_2', 'alpha_3', 'name']
    
    
class LanguageCollection(BaseCollection):
    data_class_base = Language
    no_index = ['language_family', 'macrolanguage', 'parent_alpha_3','notes']

languages = LanguageCollection(Path(DATABASEDIR) / '639_languages_golden.csv')
