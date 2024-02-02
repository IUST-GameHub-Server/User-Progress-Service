from ..LogicLayer.UserProgressLogic import UserProgressLogic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/show_person_points')
def show_person_points(string):
    return "Not Implemented"

@app.route('/show_user_level')
def show_user_level(message):
    return "Not Implemented"


@app.route('/show_user_rating')
def show_user_rating():
    return "Not Implemented"

@app.route('/display_allowed_steps')
def display_allowed_steps():
    return "Not Implemented"
