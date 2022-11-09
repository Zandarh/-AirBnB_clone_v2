#!/usr/bin/python3
"""Web frameworke task 0"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
