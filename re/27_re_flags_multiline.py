#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 27_re_flags_multiline.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 27_re_flags_multiline.py
"""
import re

text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Single Line :')
for match in single_line.findall(text):
    print(' {!r}'.format(match))
print('Multline    :')
for match in multiline.findall(text):
    print(' {!r}'.format(match))
'''
Text:
 'This is some text -- with punctuation.\nA second line.'
Pattern:
 (^\w+)|(\w+\S*$)
Single Line :
 ('This', '')
 ('', 'line.')
Multline    :
 ('This', '')
 ('', 'punctuation.')
 ('A', '')
 ('', 'line.')
'''