#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: h2_sample00.py
comment:
    - PostgreSQL DBMS
    - pip install psycopg2-binary
    - TODO: not working
"""

import psycopg2 as pg2

# 데이터베이스 연결 정보
hostname = 'localhost'
port = '9092'
username = 'sa'
password = ''
database = 'queuedb'

# 데이터베이스 연결
conn = pg2.connect(
    host=hostname,
    port=port,
    user=username,
    password=password,
    database=database
)

print(">>>>> conn: %s" % (conn))

# 쿼리 실행
cur = conn.cursor()
cur.execute("SELECT * FROM TBL_CAMP3")

# 결과 출력
for row in cur.fetchall():
    print(row)

# 연결 종료
conn.close()
