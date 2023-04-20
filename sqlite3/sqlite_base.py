#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: sqlite_base.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python sqlite_base.py
"""
import sqlite3
import os

HOME_PATH = '/Users/kang-air'
JOB_PATH = os.sep.join([HOME_PATH, 'KANG/_GIT_HUB/python/github/KieaKSFC_pytest', 'sqlite3'])
DB_PATH = f'{JOB_PATH}/db'

# -------------------------------------------------------------------
def db_connect(db_name: str) -> sqlite3.Connection:
    ''' db_connect '''
    return sqlite3.connect(':memory:')
    # return sqlite3.connect(f'{DB_PATH}/{db_name}.db')
'''
'''
# -------------------------------------------------------------------
def db_create_table(cursor: sqlite3.Cursor) -> None:
    ''' db_create_table '''
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            address TEXT
        )
    ''')
'''
'''
# -------------------------------------------------------------------
def db_insert_one(cursor: sqlite3.Cursor) -> None:
    ''' db_insert_one '''
    cursor.execute('''
        INSERT INTO test (name, age, address) VALUES ('kang', 50, 'seoul')
    ''')
'''
'''
# -------------------------------------------------------------------
def db_insert_multi(cursor: sqlite3.Cursor) -> None:
    ''' db_insert_multi '''
    lstMany = [
        ('kim', 40, 'busan'),
        ('lee', 30, 'incheon'),
        ('park', 20, 'gwangju'),
    ]
    cursor.executemany('''
        INSERT INTO test (name, age, address) VALUES (?, ?, ?)
    ''', lstMany)
'''
'''
# -------------------------------------------------------------------
def db_commit(connect: sqlite3.Connection) -> None:
    ''' db_commit '''
    connect.commit()
'''
'''
# -------------------------------------------------------------------
def db_select(cursor: sqlite3.Cursor) -> None:
    ''' db_select '''
    cursor.execute('''
        SELECT * FROM test
    ''')
'''
'''
# -------------------------------------------------------------------
def db_fetchone(cursor: sqlite3.Cursor) -> None:
    ''' db_fetchone '''
    row = cursor.fetchone()
    print('fetchone>', row)
'''
'''
# -------------------------------------------------------------------
def db_fetchall(cursor: sqlite3.Cursor) -> None:
    ''' db_fetchall '''
    rows = cursor.fetchall()
    for row in rows:
        print('fetchall>', row)
'''
'''
# -------------------------------------------------------------------
def db_close(connect: sqlite3.Connection) -> None:
    ''' db_close '''
    connect.close()
'''
'''
# -------------------------------------------------------------------
def main() -> None:
    ''' main '''
    connect = db_connect('test')
    cursor = connect.cursor()
    if True: db_create_table(cursor)

    if True: db_insert_one(cursor)
    if True: db_insert_multi(cursor)
    if True: db_commit(connect)

    if True: db_select(cursor)
    if True: db_fetchone(cursor)
    if True: db_fetchall(cursor)

    if True: db_close(connect)
    pass
'''
'''
# -------------------------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''