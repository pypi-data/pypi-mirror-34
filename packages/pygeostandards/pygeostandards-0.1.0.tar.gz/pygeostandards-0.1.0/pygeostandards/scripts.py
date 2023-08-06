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

class Script(BaseItem):
    _fieldnames = ['alpha_4', 'name', 'numeric_code']
    _prettyprintfields = _fieldnames

class ScriptsCollection(BaseCollection):
    data_class_base = Script

scripts = ScriptsCollection(Path(DATABASEDIR) / '15924_scripts_golden.csv')
