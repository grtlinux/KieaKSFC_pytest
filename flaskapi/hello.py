# file: hello.py
# using flask to create an api
# - install
#       $ pip install flask
# - run
#       $ python hello.py
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return { "message" : 'Hello World!' }

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True)
