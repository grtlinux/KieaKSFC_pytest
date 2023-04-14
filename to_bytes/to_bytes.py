#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: hashlib01.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python hashlib01.py
"""

# ------------------------------------------
def test_bytes():
    ''' test_bytes '''
    print('-'*40, 'bytes', '-'*40)
    string = 'Hello, World !!! by 강석'
    bString = bytes(string, 'utf-8')
    print('utf8: ', type(bString), bString)
    bString = bytes(string, 'euc-kr')
    print('euckr:', type(bString), bString)
'''
utf8:  <class 'bytes'> b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d'
euckr: <class 'bytes'> b'Hello, World !!! by \xb0\xad\xbc\xae'
'''
# ------------------------------------------
def test_encode():
    ''' test_bytes '''
    print('-'*40, 'encode', '-'*40)
    string = 'Hello, World !!! by 강석'
    bString = string.encode('utf-8')
    print('utf8: ', type(bString), bString)
    bString = string.encode('euc-kr')
    print('euckr:', type(bString), bString)
'''
utf8:  <class 'bytes'> b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d'
euckr: <class 'bytes'> b'Hello, World !!! by \xb0\xad\xbc\xae'
'''
# ------------------------------------------
def test_decode():
    ''' test_bytes '''
    print('-'*40, 'decode', '-'*40)
    # bString = b'Hello, World !!! by 강석' # 강석 is not ascii
    bString = b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d' # 강석 is converted to hex
    print('orgin:', type(bString), bString)
    string = bString.decode('utf-8')
    print('utf8: ', type(string), string)
    # string = bString.decode('euc-kr')
    # print('euckr:', type(string), string)
'''
orgin: <class 'bytes'> b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d'
utf8:  <class 'str'> Hello, World !!! by 강석
'''
# ------------------------------------------
def test_str():
    ''' test_str '''
    print('-'*40, 'str', '-'*40)
    bString = b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d' # 강석 is converted to hex
    print('orgin:', type(bString), bString)
    string = str(bString, 'utf-8')
    print('utf8: ', type(string), string)
    # string = str(bString, 'euc-kr')
    # print('euckr:', type(string), string)
'''
orgin: <class 'bytes'> b'Hello, World !!! by \xea\xb0\x95\xec\x84\x9d'
utf8:  <class 'str'> Hello, World !!! by 강석
'''
# ------------------------------------------
if __name__ == '__main__':
    ''' main '''
    if True: test_bytes()
    if True: test_encode()
    if True: test_decode()
    if True: test_str()

    pass
