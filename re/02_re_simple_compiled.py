#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 02_re_simple_compiled.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 02_re_simple_compiled.py
"""
import re

# Precompile the patterns
regexes = [ re.compile(p) for p in ['this', 'that'] ]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for pattern in regexes:
    print('Seeking "{}" ->'.format(pattern.pattern), end=' ')

    if pattern.search(text):
        print('match!')
    else:
        print('no match')
'''
Text: 'Does this text match the pattern?'

Seeking "this" -> match!
Seeking "that" -> no match
'''