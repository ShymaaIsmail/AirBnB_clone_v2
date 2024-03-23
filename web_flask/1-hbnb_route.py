#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello HBNB Message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_only():
    """HBNB Message"""
    return "HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
