#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """List All States"""
    states = storage.all(State)
    # Convert dictionary values to list
    states_list = list(states.values())
    # Sort the list by state name
    sorted_states = sorted(states_list, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def close_app(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
