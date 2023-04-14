# FlaskAPI

- *[Flask source](https://github.com/pallets/flask)*
- [Github: flask_minimal](https://github.com/taptorestart/python-backend-examples/blob/main/flask/flask_minimal/app.py)
- [Flask 설치하기](https://flask-docs-kr.readthedocs.io/ko/latest/ko/installation.html#installation)
- [Flask 빠르게 시작하기](https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html)
- [Python Flask Example 플라스크 예제 !! 정복하기(1)](https://edudeveloper.tistory.com/135)
- []()
- []()


---
### pip install
``` shell
$ pip install Flask
```

### First
- hello.py
``` python
# file: hello.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return { "message" : 'Hello World!' }

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # debug=True: autoreload
    # host="0.0.0.0": connect from external client
    # port="5000": using port
    app.run()
```

- 실행
``` shell
$ python hello.py
    * Serving Flask app 'hello'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 744-399-690
    127.0.0.1 - - [02/Apr/2023 17:39:50] "GET / HTTP/1.1" 200 -
```
- 브라우저 확인: http://127.0.0.1:5000/

---
### with Ngrok
- [[Flask.3] pyngrok로 외부에서 Flask 접속하기](https://go-guma.tistory.com/11?category=1080153)
- [Flask-Ngrok API 연동](https://velog.io/@j_aion/iOS-Flask-Ngrok-API-%EC%97%B0%EB%8F%99)
- [app.py를 만들어보자 with ngrok](https://hangjastar.tistory.com/171)

- pip install
``` shell
$ pip install flask-ngrok
$ pip install pyngrok
```




