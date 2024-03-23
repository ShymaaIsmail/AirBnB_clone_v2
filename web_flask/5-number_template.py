#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello HBNB Message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_only():
    """HBNB Message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text=None):
    """C Text parameter"""
    return f"C {str.replace(text, '_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """python Text parameter"""
    return f"Python {str.replace(text, '_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_only(n):
    """number parameter only"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number_only(n):
    """number template only"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
