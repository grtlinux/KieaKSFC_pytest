# FastAPI

- [FastAPI](https://fastapi.tiangolo.com/)
- [Github: fastapi_minimal](https://github.com/taptorestart/python-backend-examples/blob/main/fastapi/fastapi_minimal/main.py)
- [01. FastAPI 바로 실행해보기](https://wikidocs.net/162345)
- []()

---
### pip install
``` shell
$ pip install fastapi
$ pip install "uvicorn[standard]"

```

### First
- hello.py
``` python
# file: hello.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    ''' hello '''
    return {"message": "Hello, world!"}
```
- 실행
``` shell
$ uvicorn hello:app --reload
    INFO:     Will watch for changes in these directories: ['.....']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [74127] using WatchFiles
    INFO:     Started server process [74156]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

```
- 브라우저 확인: http://localhost:8000/
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- port 변경: -> 8080
``` shell
$ python -m uvicorn hello:app --reload --port=8080 --host=0.0.0.0
```


