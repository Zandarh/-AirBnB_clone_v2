#!/usr/bin/python3
"""Web frameworke task 0"""

from flask import Flask

app = Flask(__name__)


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Says c is dash"""
    if text == None:
        text = "is cool"
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
