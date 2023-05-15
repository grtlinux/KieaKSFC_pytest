#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 47_re_split_groups.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 47_re_split_groups.py
"""
import re

'''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''

text = '''Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'''

print('With split:')
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(para))
    print()

print(re.split(r'(\n{2,})', text))
print(type(re.split(r'(\n{2,})', text)))
'''
With split:
0 'Paragraph one\non two lines.'

1 '\n\n'

2 'Paragraph two.'

3 '\n\n\n'

4 'Paragraph three.'

['Paragraph one\non two lines.', '\n\n', 'Paragraph two.', '\n\n\n', 'Paragraph three.']
<class 'list'>
'''