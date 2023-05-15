#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 24_re_groups_alternative.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 24_re_groups_alternative.py
"""
import re

def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print('  {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print(
                '  {}{!r}{} '.format(prefix,
                                     text[s:e],
                                     ' ' * (len(text) - e)),
                end=' ',
            )
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),
                )
        print()
    return

test_patterns(
    'abbaabbba',
    [
        (r'a((a+)(b+))', 'a followed by 1-n a and 1-n b'),
        (r'a((a|b)+)(b*)', 'a followed by a sequence of b or a and 0-n b'),
    ]
)
'''
'a((a+)(b+))' (a followed by 1-n a and 1-n b)

  'abbaabbba'
     'aabbb'   ('abbb', 'a', 'bbb')

'a((a|b)+)(b*)' (a followed by a sequence of b or a and 0-n b)

  'abbaabbba'
  'abbaabbba'  ('bbaabbba', 'a', '')
'''