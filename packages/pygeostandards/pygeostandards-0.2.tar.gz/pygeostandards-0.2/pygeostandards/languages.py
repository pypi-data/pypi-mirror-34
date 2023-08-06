#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Languages in ISO-639.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection


class Language(BaseItem):
    _fieldnames = ['language_family','name','native_name',
                   'alpha_2','alpha_3', 'alpha_3_b', 'alpha_3_639_3',
                   'macrolanguage', 'parent_alpha_3', 'notes']
    _prettyprintfields = ['alpha_2', 'alpha_3', 'name']
    
    
class LanguageCollection(BaseCollection):
    _data_class_base = Language
    _no_index = ['language_family', 'macrolanguage', 'parent_alpha_3','notes']

languages = LanguageCollection('639_languages_golden.csv')
