#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:17:23 2018

@author: mattange
"""

def lazy_load(f):
    def load_if_needed(self, *args, **kw):
        if not self._is_loaded:
            with self._load_lock:
                self._load()
        return f(self, *args, **kw)
    return load_if_needed
