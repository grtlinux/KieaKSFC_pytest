#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
# end_pymotw_header
# file: .pylintrc

"""
program: h2_sample01.py
comment:
    - H2 DBMS
    - pip install jaydebeapi
"""

import jaydebeapi
import inspect

# print(inspect.getabsfile(jaydebeapi))

QUERY = '''CREATE TABLE IF NOT EXISTS exoplanets (
          id INT PRIMARY KEY AUTO_INCREMENT,
          name VARCHAR NOT NULL,
          year_discovered SIGNED,
          light_years FLOAT,
          mass FLOAT,
          link VARCHAR)'''

connection  = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:tcp://localhost:9092/queuedb",
    #"jdbc:h2:tcp://localhost:8082/inbodydb",
    ["SA", ""],
    # "/workspaces/KieaPyKsf22-1/h2/h2/bin/h2-1.4.200.jar")
    # "~/KANG/h2/bin/h2-1.4.200.jar")           # this is not working
    "/Users/kang-air/KANG/h2/bin/h2-1.4.200.jar")
cursor = connection.cursor()
RETURN_RESULT = None
cursor.execute(QUERY, RETURN_RESULT)
if RETURN_RESULT:
    #returnResult = _convert_to_schema(cursor)
    print('okay')
cursor.close()
connection.close()
