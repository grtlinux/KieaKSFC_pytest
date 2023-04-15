#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: format_str01.py
'''
program: format_str01.py
comment:
    $ python format_str01.py

    format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
        fill        ::=  <any character>
        align       ::=  "<" | ">" | "=" | "^"
        sign        ::=  "+" | "-" | " "
        width       ::=  integer
        precision   ::=  integer
        type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

'''

# ----------------------------------------------
def test01():
    ''' test01 str '''
    print('-' * 80)
    str = '0123456789abcdefghijklmnopqrstuvwxyz'
    print('test01>{!r}'.format(str[:100]))
    print('test01>{!r}'.format(str[:20][:100]))

    str = '0123456789abcdefghijklmnopqrstuvwxyz'
    print('test01>{!r}'.format('{message:{fill}{align}{width}}'.format(message=str[:20], fill=' ', align='<', width=30)))
    str = '0123456789'
    print('test01>{!r}'.format('{message:{fill}{align}{width}}'.format(message=str[:20], fill=' ', align='<', width=30)))
    pass

# ----------------------------------------------
def test02():
    ''' test02 unicode '''
    print('-' * 80)
    str = '0123456789한글입니다.'
    print('test02>{!r}'.format(str[:14]))
    pass

# ----------------------------------------------
def test03():
    ''' test03 bytes '''
    print('-' * 80)
    byStr = bytes('0123456789한글입니다.', encoding='euckr')
    print('test03>{!r}'.format(str(byStr[:14], encoding='euckr')))
    pass

# ----------------------------------------------
def test04():
    ''' test04 bytes '''
    print('-' * 80)
    print('test04>{!r}'.format('123'.zfill(20)))
    print('test04>{!r}'.format('Hi'.ljust(20, '-')))
    print('test04>{!r}'.format('Hi'.center(20, '-')))
    print('test04>{!r}'.format('Hi'.rjust(20, '-')))
    print('test04>{!r}'.format(f'{"Hi":<16} StackOverflow!'))
    print('test04>{!r}'.format('{message: >{fill}} StackOverflow!'.format(message='Hi', fill=16)))
    print('test04>{!r}'.format('{message:{fill}{align}{width}} StackOverflow!'.format(message='Hi', fill=' ', align='>', width=16)))
    pass

# ----------------------------------------------
def test05():
    ''' test05 bytes '''
    print('-' * 80)
    # print('test05>{!r}'.format('{message:{fill}{align}{width}} StackOverflow!'.format(message='Hi', fill=' ', align='>', width=16)))
    indent = ''
    # indent = '    '
    fld = {'fieldName': 'name', 'testValue': '123.45', 'size': 10}
    struct = f'{indent}char {fld["fieldName"]: <40} [{fld["size"]:0>4}];'
    print('test05>{!r}'.format(struct))

    size = fld["size"]
    string = f'{fld["testValue"]: <{size}}'
    print('test05>{!r}'.format(string))
    pass

# ----------------------------------------------
def main():
    ''' main '''
    if True: test01()
    if True: test02()
    if True: test03()
    if True: test04()
    if True: test05()
    pass

# ----------------------------------------------
if __name__ == '__main__':
    main()
'''
'''
