#!/usr/bin/python3
"""Flask task"""
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_nu(n):
    if n % 2 == 0:
        odd = "even"
        return render_template('6-number_odd_or_even.html', n=n, odd=odd)
    else:
        odd = "odd"
        return render_template('6-number_odd_or_even.html',n=n, odd=odd)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
