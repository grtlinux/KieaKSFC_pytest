#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 19_re_groups_match.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 19_re_groups_match.py
"""
import re

text = 'This is some text -- with punctuation.'
print("text: {}".format(text))
print("----------------------------------------")

patterns = [
    (r'^(\w+)', 'word at start of string'),
    (r'(\w+)\S*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
    (r'(\w+t)\b', 'word ending with t'),
]

for pattern, desc in patterns:
    print("'{}' ({})\n".format(pattern, desc))
    regex = re.compile(pattern)
    match = regex.search(text)
    print("match: {}".format(match))
    if match:
        print("  match.groups(): {}".format(match.groups()))
        # print("  match.group(1): {}".format(match.group(1)))
        # print("  match.group(2): {}".format(match.group(2)))
    print('-'*40)
'''
text: This is some text -- with punctuation.
----------------------------------------
'^(\w+)' (word at start of string)

match: <re.Match object; span=(0, 4), match='This'>
  match.groups(): ('This',)
----------------------------------------
'(\w+)\S*$' (word at end, with optional punctuation)

match: <re.Match object; span=(26, 38), match='punctuation.'>
  match.groups(): ('punctuation',)
----------------------------------------
'(\bt\w+)\W+(\w+)' (word starting with t, another word)

match: <re.Match object; span=(13, 25), match='text -- with'>
  match.groups(): ('text', 'with')
----------------------------------------
'(\w+t)\b' (word ending with t)

match: <re.Match object; span=(13, 17), match='text'>
  match.groups(): ('text',)
----------------------------------------
'''