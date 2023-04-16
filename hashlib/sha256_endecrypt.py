#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: sha256_endecrypt.py
    RUN:
        $ python -V
            Python 3.10.9
        $ python sha256_endecrypt.py
"""
import hashlib

# ------------------------------------------------
def test01_sha256_encrypt(text: str) -> str:
    ''' test01_sha256_encrypt '''
    enc = hashlib.sha256(bytes(text, 'utf-8')).hexdigest()
    return enc

# ------------------------------------------------
def test02_sha256_decrypt(enc: str) -> str:
    ''' test02_sha256_decrypt '''
    enc = '''ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
				2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6'''
    for i in range(123):
        enc = enc.replace(hashlib.sha256(chr(i).encode()).hexdigest(), chr(i))
    return enc

# ------------------------------------------------
def main() -> None:
    ''' main '''
    text = 'Hello, World !!! by 강석'
    enc = test01_sha256_encrypt(text)
    print('enc: ', enc)
    dec = test02_sha256_decrypt(enc)
    print('dec: ', dec)
    pass

# ------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''