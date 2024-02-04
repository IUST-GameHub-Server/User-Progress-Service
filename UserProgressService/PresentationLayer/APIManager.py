from ..LogicLayer.UserProgressLogic import UserProgressLogic
from flask import Flask, request

app = Flask(__name__)

@app.route('/setup_user_progress', methods=['PUT'])
def setup_user_progress():
    return UserProgressLogic.setup_player(request.data)

@app.route('/update_user_progress', methods=['POST'])
def update_user_progress():
    return UserProgressLogic.update_player_progress(request.data)

@app.route('/get_user_progress', methods=['GET'])
def get_user_progress():
    return UserProgressLogic.get_player_progress(request.data)
