# -*- coding: utf-8 -*-
import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.helper_api import helper_api_bp

# from Items.models import User, Matched, Pending
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import get_log, log, generate_msg
from Items.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match

@helper_api_bp.route('/get_backend_log/<string:id>', methods=['POST'])
@token_auth.login_required
def get_backend_log(id):

    """
    return log of current task. Must have task_id in data, Might have test_id in data.

    Parameters:
        task_id - String.

    Returns:
        data - Dict[Dict[String, String, List[String]]]. List[String]: ['first log_interval\n', 'second\n', 'third']

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    print('data',data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data['task_id']
    train_match_document = train_match.search_train_match_document(task_id=task_id)
    test_task_dict = train_match_document['test_task_dict']
    
    response = {}
    response[task_id] = {
        'id': task_id,
        'test_indicator': 'train',
        'log_file': get_log(user_id, task_id)
    }
    for test_id in test_task_dict:
        response[test_id] = {
            'id': test_id,
            'test_indicator': 'test',
            'log_file': get_log(user_id, test_id)
        }
        
    return jsonify(response)

