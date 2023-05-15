#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 16_re_fullmatch.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 16_re_fullmatch.py
"""
import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :', text)
print('Pattern:', pattern)

m = re.search(pattern, text)
print('Search :', m)
s = re.fullmatch(pattern, text)
print('Full match :', s)
'''
Text   : This is some text -- with punctuation.
Pattern: is
Search : <re.Match object; span=(2, 4), match='is'>
Full match : None
'''