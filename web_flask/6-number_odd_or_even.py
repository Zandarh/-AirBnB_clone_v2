#!/usr/bin/python3
"""Web frameworke task 0"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def hello(n):
    """Says HBNB"""
    return render_template("6-number_odd_or_even", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
