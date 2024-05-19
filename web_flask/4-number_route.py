#!/usr/bin/python3
"""Flask task"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    formatted_text = text.replace("_", " ")
    return "C " + formatted_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    formatted_text = text.replace("_", " ")
    return "Python " + formatted_text

@app.route('/number/', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def number(num):
    if isinstance(n, int):
        return "n is a number " + num;
    else:
        return
if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
