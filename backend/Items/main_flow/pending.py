from __future__ import annotations

# -*- coding: utf-8 -*-
import sys
from flask import request
from flask.json import jsonify

# import BluePrint
from Items.main_flow import main_flow_bp
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import log, generate_msg, obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.utils.api import (
    check_if_data_is_valid,
    input_data_err_msg
)

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_task
from Items.mongoDB import test_match, test_task

from typing import Union


@main_flow_bp.route('/add_train_pending/<string:id>', methods=['POST'])
@token_auth.login_required
def add_train_pending(id):

    """
    Synspot adds train task to the pending when the assistor operation mode is manual

    Parameters:
        train_id - String. The id of current train task
       
    Returns:
        {"message": "add train pending successfully"}

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name, 'You must post JSON data.'))

    expected_data = {
        'train_id': str
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    train_id = data.get('train_id')
    mongoDB.update_pending_document(
        user_id=user_id, 
        task_id=train_id, 
        test_indicator='train'
    )
    
    response = {
        'message': 'add train pending successfully'
    }
    return jsonify(response)

@main_flow_bp.route('/add_test_pending/<string:id>', methods=['POST'])
@token_auth.login_required
def add_test_pending(id):
    """
    Synspot adds test task to the pending when the assistor operation mode is manual

    Parameters:
        test_id - String. The id of current test task
       
    Returns:
        {"message": "add test pending successfully"}

    Raises:
        KeyError - raises an exception
    """
    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name, 'You must post JSON data.'))

    expected_data = {
        'test_id': str
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    test_id = data.get('test_id')
    mongoDB.update_pending_document(
        user_id=user_id, 
        task_id=test_id, 
        test_indicator='test'
    )

    response = {
        'message': 'add test pending successfully'
    }
    return jsonify(response)


@main_flow_bp.route('/get_all_pending/<string:id>', methods=['GET'])
@token_auth.login_required
def get_all_pending(id):
    """
    Synspot adds test task to the pending when the assistor operation mode is manual

    Parameters:
        test_id - String. The id of current test task
       
    Returns:
        {"message": "add test pending successfully"}

    Raises:
        KeyError - raises an exception
    """
    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id, username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    pending_document = mongoDB.search_pending_document(user_id=user_id)

    response = {}
    if pending_document != None:
        response['all_pending_items'] = {}
        task_dict = pending_document['task_dict']

        for task_id in task_dict:
            test_indicator = task_dict[task_id]['test_indicator']
            if test_indicator == 'train':
                train_task_document = train_task.search_train_task_document(train_id=task_id)
                # remove ObjectId object, which cannot be transferred into json format
                del train_task_document['_id']
                response['all_pending_items'][task_id] = train_task_document
            elif test_indicator == 'test':
                test_task_document = test_task.search_test_task_document(test_id=task_id)
                # remove ObjectId object, which cannot be transferred into json format
                del test_task_document['_id']
                response['all_pending_items'][task_id] = test_task_document

    return jsonify(response)

@main_flow_bp.route('/delete_pending/<string:id>', methods=['POST'])
@token_auth.login_required
def dalete_pending(id):
    '''
     Delete the specific train_id or test_id in pending
    '''
    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name, 'You must post JSON data.'))

    expected_data = {
        'train_id': str,
        'test_id': Union[str, None],
        'test_indicator': str
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    train_id = data['train_id']
    if 'test_id' in data:
        test_id = data['test_id']
    test_indicator = data['test_indicator']

    task_id = None
    if test_indicator == 'train':
        task_id = train_id
    elif test_indicator == 'test':
        task_id = test_id
    mongoDB.delete_pending_document_field(user_id=user_id, task_id=task_id)

    response = {
        'message': 'delete successfully'
    }
    return jsonify(response)