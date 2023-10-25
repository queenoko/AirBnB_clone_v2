#!/usr/bin/python3
"""script that starts flask web application
it must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return "Hello HBNB!"

	"""shows "HBNB"."""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
