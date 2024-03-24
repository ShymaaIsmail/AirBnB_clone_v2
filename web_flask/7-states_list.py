#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_app(exception=None):
    """close session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """List All States"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
