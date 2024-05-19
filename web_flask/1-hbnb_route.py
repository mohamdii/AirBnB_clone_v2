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

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
