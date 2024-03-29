#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 14_re_anchoring.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 14_re_anchoring.py
"""
import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = substr.count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

test_patterns(
    'This is some text -- with punctuation.',
    [
        (r'^\w+', 'word at start of string'),
        (r'\A\w+', 'word at start of string'),
        (r'\w+\S*$', 'word near end of string, skip punctuation'),
        (r'\w+\S*\Z', 'word near end of string, skip punctuation'),
        (r'\w*t\w*', 'word containing t'),
        (r'\bt\w+', 't at start of word'),
        (r'\w+t\b', 't at end of word'),
        (r'\Bt\B', 't, not start or end of word'),
    ]
)
'''
'^\w+' (word at start of string)

  'This is some text -- with punctuation.'
  'This'

'\A\w+' (word at start of string)

  'This is some text -- with punctuation.'
  'This'

'\w+\S*$' (word near end of string, skip punctuation)

  'This is some text -- with punctuation.'
  ..........................'punctuation.'

'\w+\S*\Z' (word near end of string, skip punctuation)

  'This is some text -- with punctuation.'
  ..........................'punctuation.'

'\w*t\w*' (word containing t)

  'This is some text -- with punctuation.'
  .............'text'
  .....................'with'
  ..........................'punctuation'

'\bt\w+' (t at start of word)

  'This is some text -- with punctuation.'
  .............'text'

'\w+t\b' (t at end of word)

  'This is some text -- with punctuation.'
  .............'text'

'\Bt\B' (t, not start or end of word)

  'This is some text -- with punctuation.'
  .......................'t'
  ..............................'t'
  .................................'t'
'''