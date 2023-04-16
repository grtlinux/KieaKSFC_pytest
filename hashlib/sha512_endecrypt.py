#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: sha512_endecrypt.py
    RUN:
        $ python -V
            Python 3.10.9
        $ python sha512_endecrypt.py
"""
import hashlib

# ------------------------------------------------
def test01_sha512_encrypt(text: str) -> str:
    ''' test01_sha512_encrypt '''
    enc = hashlib.sha512(bytes(text, 'utf-8')).hexdigest()
    return enc

# ------------------------------------------------
def test02_sha512_decrypt(enc: str) -> str:
    ''' test02_sha256_decrypt '''
    enc = '''ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
				2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6'''
    for i in range(123):
        enc = enc.replace(hashlib.sha512(chr(i).encode()).hexdigest(), chr(i))
    return enc

# ------------------------------------------------
def main() -> None:
    ''' main '''
    text = 'Hello, World !!! by 강석'
    enc = test01_sha512_encrypt(text)
    print('enc: ', enc)
    dec = test02_sha512_decrypt(enc)
    print('dec: ', dec)
    pass

# ------------------------------------------------
import datetime

def get_client_info() -> None:
    ''' get_client_info '''
    text = 'Hello, World !!! SHA512 by KANG SEOK' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    enc = test01_sha512_encrypt(text)
    print('token: ', enc)
    pass

# ------------------------------------------------
if __name__ == '__main__':
    if not True: main()
    if True: get_client_info() 
'''
enc:  d4a420131477f7dc4bac3764c3762d6fc21f66773c39f2d3da53e337709d0b16fd29e37a9c995687dda0fcb2774bba129095cce821737fc1c6b85e88aa3a0bc2
'''