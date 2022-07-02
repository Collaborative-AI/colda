# -*- coding: utf-8 -*-
from flask import request
from flask.json import jsonify

# import BluePrint
from Items.main_flow import main_flow_bp
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import log, generate_msg, obtain_user_id_from_token, verify_token_user_id_and_function_caller_id

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_task
from Items.mongoDB import test_match, test_task

@main_flow_bp.route('/get_max_round', methods=['POST'])
@token_auth.login_required
def get_max_round():
    '''
    http get request

    Parameters
    ----------
    train_id : str
    url_prefix : str
    url_root : str
    url_suffix : str
    status_code : int

    Returns
    -------
    max_round : int
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'train_id' not in data or not data.get('train_id'):
        return bad_request('train_id is required.')

    train_id = data['train_id']
    train_task_document = train_task.search_train_task_document(
        train_id=train_id, 
    )

    max_round = train_task_document["max_round"]
    response = {
        'max_round': max_round
    }
    print('responsesss', response)
    return jsonify(response)