#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: main.py
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
"""

from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import ORJSONResponse, HTMLResponse, PlainTextResponse, UJSONResponse
from fastapi.responses import RedirectResponse, StreamingResponse, FileResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}


class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

# --------------------------------------------------
@app.get("/")
async def root():
    return {"msg": "Hello World"}


# --------------------------------------------------
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return fake_db.get(item_id, None)


# --------------------------------------------------
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    fake_db[item.id] = item
    return item

# --------------------------------------------------
@app.get("/items/orjson", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])

# --------------------------------------------------
@app.get("/items/html1", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
# --------------------------------------------------
@app.get("/items/html2")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# --------------------------------------------------
def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/items/html3", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()

# --------------------------------------------------
@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")

# --------------------------------------------------
@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"

# --------------------------------------------------
@app.get("/items/", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]

# --------------------------------------------------
@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")

# --------------------------------------------------
@app.get("/fastapi", response_class=RedirectResponse)
async def redirect_fastapi():
    return "https://fastapi.tiangolo.com"

# --------------------------------------------------
@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"

# --------------------------------------------------
async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"

@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())

# --------------------------------------------------
some_file_path = "large-video-file.mp4"

@app.get("/")
def main():
    def iterfile():  # 
        with open(some_file_path, mode="rb") as file_like:  # 
            yield from file_like  # 

    return StreamingResponse(iterfile(), media_type="video/mp4")

# --------------------------------------------------
@app.get("/")
async def main():
    return FileResponse(some_file_path)

# --------------------------------------------------
@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path

# --------------------------------------------------
from typing import Any
import orjson

class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)

@app.get("/", response_class=CustomORJSONResponse)
async def main():
    return {"message": "Hello World"}

# --------------------------------------------------
# app = FastAPI(default_response_class=ORJSONResponse)

@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------


