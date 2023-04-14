# file: hello.py
# using fastapi to create an api
# - install
#       $ pip install fastapi
#       $ pip install "uvicorn[standard]"
# - run
#       $ uvicorn hello:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    ''' hello '''
    return {"message": "Hello, world!"}
