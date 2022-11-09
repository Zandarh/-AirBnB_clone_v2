#!/usr/bin/python3
"""Web frameworke task 0"""

from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Says HBNB"""
    if type(n) == int:
        return "{} is a number".format(n)
    else:
        abort()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
