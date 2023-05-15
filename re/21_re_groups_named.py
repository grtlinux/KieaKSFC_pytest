#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 21_re_groups_named.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 21_re_groups_named.py
"""
import re

text = 'This is some text -- with punctuation.'
print("text: {}".format(text))
print("----------------------------------------")

patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
]

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "{}"'.format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()
'''
text: This is some text -- with punctuation.
----------------------------------------
Matching "^(?P<first_word>\w+)"
   ('This',)
   {'first_word': 'This'}

Matching "(?P<last_word>\w+)\S*$"
   ('punctuation',)
   {'last_word': 'punctuation'}

Matching "(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)"
   ('text', 'with')
   {'t_word': 'text', 'other_word': 'with'}

Matching "(?P<ends_with_t>\w+t)\b"
   ('text',)
   {'ends_with_t': 'text'}
'''