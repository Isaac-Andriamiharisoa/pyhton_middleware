from typing import Any
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

print ("  ( •_•)\n( •_•)>⌐■-■\n(⌐■_■)\nDeal with it.")

# Define a pattern using regex
pattern = re.compile(r'ex')

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

@app.route('/endpoint', methods = ['GET'])
def get_endpoint():
    return jsonify({'message': 'got the page'})

@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    data = request.json
    if 'message' in data and re.search(r'ex', data['message']):
        return jsonify({'message': 'Data received successfully', 'data': data})
    else :
        return jsonify({'message': 'Wrong message'})

if __name__ == '__main__':
    app.run(debug=True)
