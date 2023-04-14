#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: h2_sample01.py
comment:
    - H2 DBMS
    - pip install jaydebeapi
"""

import jaydebeapi

# JDBC 드라이버 로드
jarfile = "/Users/kang-air/KANG/h2/bin/h2-1.4.200.jar"
driver = "org.h2.Driver"
url = "jdbc:h2:tcp://localhost:9092/queuedb"

# 데이터베이스 연결
conn = jaydebeapi.connect(driver, url, ["sa", ""], jarfile)

# 쿼리 실행
curs = conn.cursor()
curs.execute("SELECT * FROM TBL_CAMP3")

# 결과 출력
rows = curs.fetchall()
for row in rows:
    print(row)

# 연결 종료
curs.close()
conn.close()
