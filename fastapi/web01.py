#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: web01.py
    RUN:
        $ uvicorn web01:app --reload --port=8080 --host=0.0.0.0
"""

from fastapi import FastAPI
import os
import json

app = FastAPI()

# ---------------------------------------------------------------- index
@app.get('/')
async def index():
    ''' index '''
    return {'message': 'Hello, world!'}

# ---------------------------------------------------------------- GET
JSON_PATH = "../pyksf01/data"
def read_json(id: int):
    ''' read_json '''
    fileName = '/'.join([JSON_PATH, 'res_%03d.json'%(id)])
    if not os.path.exists(fileName):
        return {'message': 'file not found'}
    with open(fileName, 'r') as f:
        dic = json.load(f)
    f.close()
    return dic

@app.get('/get/{id}')
async def get(id: int) -> dict:
    ''' get : http://localhost:8080/get/2'''
    print('GET: id {}'.format(id))
    return read_json(id)

@app.get('/get2/{id}')
async def get(id: int, fld1: str='fld1', fld2: int=123) -> dict:
    ''' get : http://localhost:8080/get2/3?fld1=abc&fld2=123 '''
    print('GET: id {}'.format(id))
    print('GET: fld1={}, fld2={}'.format(fld1, fld2))
    return read_json(id)

# ---------------------------------------------------------------- POST
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Union

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
async def post(req: Req002Items) -> dict:
    ''' post '''
    print('POST-1: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    return read_json(2)

# ---------------------------------------------------------------- POST
class Req003Items(BaseModel):
    param1: str = None
    param2: str = None

@app.post('/v1/post')
async def v1Post(req: Req003Items) -> dict:
    ''' post '''
    # print('hello, world!')
    print('POST-2: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    # print('POST: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    return read_json(3)


# ---------------------------------------------------------------- POST
# no used the below
'''
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
'''
