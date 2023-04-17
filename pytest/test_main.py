#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_main.py
    REF:
        https://sehoi.github.io/etc/fastapi-pytest/
        https://kibua20.tistory.com/227
    READY:
        $ pip install fastapi
        $ pip install uvicorn
        $ pip install pytest
        $ pip install pytest-asyncio
        $ pip install httpx
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        < uvicorn main:app --reload 을 실행하지 않는다. >
        $ pytest -v test_main.py
"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

'''
이제 세가지 API 함수에 대해 테스트하는 함수들을 작성하겠습니다.

test_root(): “root“ API 함수에 대해 GET 방식으로 요청하여 테스트하는 함수 입니다.

test_read_item(): “read_item“ API 함수에 대해 item_id가 1인 item을 params 값에 추가하여 GET 방식으로 요청하여 테스트하는 함수 입니다.

test_create_item(): “create_item“ API 함수에 대해 생성할 item을 json 값에 추가하여 POST 방식으로 요청하여 테스트하는 함수 입니다.
'''

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_item():
    response = client.get("/items/foo", params={"item_id": "1"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_create_item():
    response = client.post(
        "/items/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
