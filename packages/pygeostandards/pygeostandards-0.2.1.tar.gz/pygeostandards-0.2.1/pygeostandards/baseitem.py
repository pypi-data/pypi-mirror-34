#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:12:10 2018

"""
import json

class BaseItem():
    _fieldnames = []
    _prettyprintfields = []

    def __init__(self, **fields):
        for k in fields.keys():
            if k not in self._fieldnames:
                raise AttributeError('Attribute {} not valid.'.format(k))
        self._fields = fields

    def __getattr__(self, key):
        if key in self._fieldnames:
            return self._fields[key]
        else:
            raise AttributeError

    def __repr__(self):
        cls_name = self.__class__.__name__
        pfields = {k: self._fields[k] for k in self._prettyprintfields}
        fields = ', '.join('%s=%r' % i for i in pfields.items())
        return '%s(%s)' % (cls_name, fields)

    def __dir__(self):
        return dir(self.__class__) + list(self._fields)

    @classmethod
    def fieldnames(cls):
        return cls._fieldnames
    
    @property
    def fields(self):
        return self._fields
    
    @property
    def json(self):
        return json.dumps(self._fields, separators=(',',':'), ensure_ascii=False)
