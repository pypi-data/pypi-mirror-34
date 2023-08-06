#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Scripts in ISO-15924.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from .baseitem import BaseItem
from .basecollection import BaseCollection


class Script(BaseItem):
    _fieldnames = ['alpha_4', 'name', 'numeric_code']
    _prettyprintfields = _fieldnames

class ScriptsCollection(BaseCollection):
    _data_class_base = Script

scripts = ScriptsCollection('15924_scripts_golden.csv')
