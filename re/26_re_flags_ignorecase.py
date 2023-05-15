#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 26_re_flags_ignorecase.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 26_re_flags_ignorecase.py
"""
import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Case-sensitive:')
for match in with_case.findall(text):
    print(' {!r}'.format(match))
print('Case-insensitive:')
for match in without_case.findall(text):
    print(' {!r}'.format(match))
'''
Text:
 'This is some text -- with punctuation.'
Pattern:
 \bT\w+
Case-sensitive:
 'This'
Case-insensitive:
 'This'
 'text'
'''