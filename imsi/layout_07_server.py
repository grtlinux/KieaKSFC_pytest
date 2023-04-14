#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_07_server.py
    RUN:
        $ uvicorn layout_07_server:app --reload
"""

#end_pymotw_header

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Set, Union
import json

app = FastAPI()

# --- getResJson ---
def getResJson(code):
    f = open('res_{}.json'.format(code), mode='r', encoding='utf')
    data = f.read()
    f.close()
    return data

# --- 001 : GET
@app.get('/get/{id}')
async def getIndex(fld1: str, fld2: int):
    print('REQ >>>', fld1, fld2)
    return json.loads(getResJson('001'))

# --- 002 : POST
class Image(BaseModel):
    url: HttpUrl
    name: str

class Req002Items(BaseModel):
    code: str = 'CD001'
    description: Optional[str] = None
    price: float = 123.12
    count: int = 123
    tags: Union[List[str], None] = None
    images: Union[List[Image], None] = [
        {
            'url': 'http://example.org/images',
            'name': 'example.org'
        },{
            'url': 'http://sample.org/images',
            'name': 'sample.org'
        }
    ]
    dumps: Union[List[str], None] = ['홍','강','김']  # list()
    str00s: List[int] = [1,2,3]
    str01s: List[str] = ['1','2','3','4','5','6','7','8']

@app.post('/post')
async def postIndex(reqItems: Req002Items):
    # print('REQ >>>', reqItems)
    # print('REQ >>>', reqItems.dict())
    print('REQ >>>', json.dumps(reqItems.dict(), ensure_ascii=False, indent=2))
    dic = json.loads(getResJson('002'))
    dic['rsp_code'] = reqItems.code
    return dic




