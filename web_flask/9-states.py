#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""


from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """close session after app"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """List All States"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id=None):
    """List state by id"""
    states = storage.all(State)
    state = next(filter(lambda state: state.id == id, states.values()), None)
    cities = None
    if id:
        all_cities = storage.all(City)
        cities = [city for city in all_cities.values() if city.state_id == id]
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
