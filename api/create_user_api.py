from flask import Blueprint, request, jsonify
from constants.constants import UserKeys, QuestionKeys
from constants.error_lib import InternalException
from service import game_service

CREATE_USER_API = Blueprint('create_user_api', __name__)

@CREATE_USER_API.route('/create_user', methods=['POST'])
def create_user():
    '''
    : creates a user client based on the given user dict
    '''
    user_dict = request.get_json().get(UserKeys.USER)
    user_name = user_dict.get(UserKeys.NAME)
    room = user_dict.get(UserKeys.ROOM)
    return jsonify(user_dict)

@CREATE_USER_API.route('/check_answer', methods=['POST'])
def check_answer():
    '''
    : compare the answer the user submitted to the answer key. return if the answer is correct
    '''
    user_answer = request.get_json().get(QuestionKeys.QUESTION)
    if user_answer is None:
        raise InternalException('User question not found', 400)
    return jsonify(game_service.check_answer(user_answer))

