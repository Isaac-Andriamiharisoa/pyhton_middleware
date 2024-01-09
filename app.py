from typing import Any
from flask import Flask, request

app = Flask(__name__)

class RequesLogger:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print(f"Request received: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return self.app(environ, start_response)


app.wsgi_app = RequesLogger(app.wsgi_app)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/number/<int:id>')
def number(id):
    return f'the number is {id}'

if __name__ == '__main__':
    app.run(debug=True)
