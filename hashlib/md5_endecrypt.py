#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: md5_endecrypt.py
    RUN:
        $ python -V
            Python 3.10.9
        $ python md5_endecrypt.py
"""
import hashlib

# ------------------------------------------------
def test01_md5_encrypt(text: str) -> str:
    ''' test01_md5_encrypt '''
    enc = hashlib.md5(bytes(text, 'utf-8')).hexdigest()
    return enc

# ------------------------------------------------
def test02_md5_decrypt(enc: str) -> str:
    ''' test02_md5_decrypt '''
    enc = '0cc175b9c0f1b6a831c399e269772661 4a8a08f09d37b73795649038408b5f33'
    for i in range(123):
        enc = enc.replace(hashlib.md5(chr(i).encode()).hexdigest(), chr(i))
    return enc

# ------------------------------------------------
def main() -> None:
    ''' main '''
    text = 'Hello, World !!! by 강석'
    enc = test01_md5_encrypt(text)
    print('enc: ', enc)
    dec = test02_md5_decrypt(enc)
    print('dec: ', dec)
    pass

# ------------------------------------------------
def get_client_info() -> None:
    ''' get_client_info '''
    print('client_id:', test01_md5_encrypt('client_id: hanwha'))
    print('client_pw:', test01_md5_encrypt('client_pw: hanwha123!@'))
    pass
'''
client_id: e0fbc3dea4659753f45e7e7c5274743f
client_pw: f9ba0589fe79093e7a50cad49152a4d2
'''

# ------------------------------------------------
if __name__ == '__main__':
    if not True: main()
    if True: get_client_info()
'''
'''