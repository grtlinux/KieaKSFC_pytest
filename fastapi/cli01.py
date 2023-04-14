#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: cli01.py
    RUN:
        $ python cli01.py
"""

import requests
import json

DIC = {"name": "new_challenge", "description":"test1", "price":2020, "tax":2021}

URL = 'http://localhost:8080/get/{}'
# URL = 'http://localhost:8080/post/'

RES = requests.get(url=URL.format(2))
# RES = requests.post(url=URL.format(2), data=json.dumps(DIC))

print(RES.text)

