#!/usr/bin/python3
''' a script that runs a flask application '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    new_text = 'C ' + text.replace('_', ' ')
    return new_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=''):
    if text:
        new_text = 'Python ' + text.replace('_', ' ')
        return new_text
    else:
        return 'Python is cool'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
