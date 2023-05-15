#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 28_re_flags_dotall.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 28_re_flags_dotall.py
"""
import re

text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('No newlines :')
for match in no_newlines.findall(text):
    print(' {!r}'.format(match))
print('Dotall      :')
for match in dotall.findall(text):
    print(' {!r}'.format(match))
'''
Text:
 'This is some text -- with punctuation.\nA second line.'
Pattern:
 .+
No newlines :
 'This is some text -- with punctuation.'
 'A second line.'
Dotall      :
 'This is some text -- with punctuation.\nA second line.'
'''