#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_async_main.py
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
        $ uvicorn main:app --reload
            ...
        $ pytest -v test_async_main.py
"""
import json
import pytest
from httpx import AsyncClient

pytest.mark.asyncio
async def test_root():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/items/foo", params={"item_id": "1"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "foo",
            "title": "Foo",
            "description": "There goes my hero",
        }


@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post(
            "/items/",
            content=json.dumps(
                {
                    "id": "foobar",
                    "title": "Foo Bar",
                    "description": "The Foo Barters",
                }
            ),
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": "foobar",
            "title": "Foo Bar",
            "description": "The Foo Barters",
        }
