#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: hashlib01.py
    RUN:
        $ python -V
            Python 3.10.9
        $ python hashlib01.py
"""

import hashlib
import datetime

# ------------------------------------------
STRING = 'Hello, World !!! by 강석'
# ------------------------------------------
def get_datetime()-> str:
    ''' get_datetime '''
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ------------------------------------------
def test_sha1():
    ''' test_sha1 '''
    sha = hashlib.sha1()
    # sha = hashlib.new('sha1')
    print('-'*40, 'sha1', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
def test_sha224():
    ''' test_sha224 '''
    sha = hashlib.sha224()
    # sha = hashlib.new('sha224')
    print('-'*40, 'sha224', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
def test_sha256():
    ''' test_sha256 '''
    sha = hashlib.sha256()
    # sha = hashlib.new('sha256')
    print('-'*40, 'sha256', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
def test_sha384():
    ''' test_sha384 '''
    sha = hashlib.sha384()
    # sha = hashlib.new('sha384')
    print('-'*40, 'sha384', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
def test_sha512():
    ''' test_sha512 '''
    sha = hashlib.sha512()
    # sha = hashlib.new('sha512')
    print('-'*40, 'sha512', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
def test_md5():
    ''' test_md5 '''
    sha = hashlib.md5()
    # sha = hashlib.new('md5')
    print('-'*40, 'md5', '-'*40)
    sha.update(bytes(STRING, 'utf-8'))
    print('utf8: ', sha.hexdigest())
    sha.update(bytes(STRING, 'euc-kr'))
    print('euckr:', sha.hexdigest())

# ------------------------------------------
# ------------------------------------------
if __name__ == '__main__':
    ''' main '''
    STRING = get_datetime()
    if True: print('start:', STRING)

    if True: test_sha1()
    if True: test_sha224()
    if True: test_sha256()
    if True: test_sha384()
    if True: test_sha512()
    if True: test_md5()



    pass
