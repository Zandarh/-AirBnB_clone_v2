#!/usr/bin/python3
"""Web frameworke task 0"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Says Hello HBNB"""
    return "Hello HBNB!"


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Says HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
