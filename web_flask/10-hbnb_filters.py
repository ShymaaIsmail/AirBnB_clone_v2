#!/usr/bin/python3
""" Hello Route as a Basic usage for flask routing"""


from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """hbnb filters states and cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda am: am.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
