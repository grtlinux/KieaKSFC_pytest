#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: list_bytes.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python list_bytes.py
"""

# ------------------------------------------
def test01() -> None:
    ''' test01 '''
    greeting = '안녕하세요'
    lstBytes = list()
    lstBytes.append(bytes('Hello, World !!! by 안녕', 'utf-8'))
    lstBytes.append(f'{greeting}. 강석입니다.'.encode('utf-8'))

    bGreeting = bytes(greeting, 'utf-8')
    lstBytes.append(bytes(f'{greeting:.<20}', 'utf-8')[:20])

    print('1>', b''.join(lstBytes[::-1]).decode('utf-8'))

    print('-'*40)
    pass
'''
'''

# ------------------------------------------
def test02() -> None:
    ''' test02 '''
    size = 10
    string = '안녕'

    lbString = f"{string: <{size}}".encode('euc-kr')[:size]
    rbString = f"{string: >{size}}".encode('euc-kr')[-size:]
    print('2> {!r} {!r}'.format(lbString.decode('euc-kr'), rbString.decode('euc-kr')))

    print('-'*40)
    pass
'''
2> '안녕      ' '      안녕'
'''

# ------------------------------------------
def test03() -> None:
    ''' test03 '''

    print('-'*40)
    pass
'''
'''

# ------------------------------------------
def main() -> None:
    ''' main '''
    if True: test01()
    if True: test02()
    if True: test03()
    print('-'*40)
    pass
'''
'''

# ------------------------------------------
if __name__ == '__main__':
    ''' main '''
    if True: main()
    pass
'''
'''