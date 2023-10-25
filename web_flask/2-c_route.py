#!/usr/bin/python3
""" script that starts a Flask web application:
listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """will Return given output"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """will Return given output"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """this displays C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
