#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: md5_check_password.py
    RUN:
        $ python -V
            Python 3.10.9
        $ python md5_check_password.py
"""
import hashlib

# ------------------------------------------------
# The second part depends on the database you are using
# But your password is hashed in the database, 
# so you get a string like:
def get_db_password() -> str:
    ''' get_db_password '''
    db_password = "d49019c7a78cdaac54250ac56d0eda8a"
    return db_password

# ------------------------------------------------
# The first part depends on the framework you are using
# Let's say you get a password in clear format from the request:
def get_password_md5_encrypt(password: str) -> str:
    ''' get_password_md5_encrypt '''
    # hashlib.md5(password.encode()).hexdigest()
    enc = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    return enc

# ------------------------------------------------
def main() -> None:
    ''' main '''
    password = 'MD5Online'
    enc_password = get_password_md5_encrypt(password)
    db_password = get_db_password()

    # Finally, validate thet the two passwords are the same
    if enc_password == db_password:
        print('Password is correct')
    else:
        print('Password is incorrect')

# ------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''