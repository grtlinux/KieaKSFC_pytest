#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 01_re_simple_match.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 01_re_simple_match.py
"""
import re

paattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(paattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern
    , match.string
    , s, e
    , text[s:e]))
'''
Found "this"
in "Does this text match the pattern?"
from 5 to 9 ("this")
'''
