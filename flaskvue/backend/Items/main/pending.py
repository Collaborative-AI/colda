# -*- coding: utf-8 -*-
from cgi import test
import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main import main
from Items.models import User, Matched, Pending
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import log, generate_msg, obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.main.mongoDB import mongoDB, train_mongoDB, test_mongoDB

@main.route('/add_train_pending/<int:id>', methods=['POST'])
@token_auth.login_required
def add_train_pending(id):

    """
    Synspot adds train task to the pending when the assistor operation mode is manual

    Parameters:
        task_id - String. The id of current train task
       
    Returns:
        {"message": "add train pending successfully"}

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data.get('task_id')
    mongoDB.update_pending_document(user_id=user_id, id=task_id, test_indicator='train')
    
    response = {'message': 'add train pending successfully'}
    return jsonify(response)

@main.route('/add_test_pending/<int:id>', methods=['POST'])
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
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    test_id = data.get('test_id')
    mongoDB.update_pending_document(user_id=user_id, id=test_id, test_indicator='test')
    
    response = {'message': 'add test pending successfully'}
    return jsonify(response)


@main.route('/get_all_pending/<int:id>', methods=['GET'])
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
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    pending_document = mongoDB.search_pending_document(user_id=user_id)
    task_dict = pending_document['task_dict']

    response = {}
    response['all_pending_items'] = {}
    for id in task_dict:
        test_indicator = task_dict[id]['test_indicator']
        if test_indicator == 'train':
            train_match_document = train_mongoDB.search_train_match_document(task_id=id)
            response['all_pending_items'][id] = train_match_document
        elif test_indicator == 'test':
            test_match_document = test_mongoDB.search_test_match_document(test_id=id)
            response['all_pending_items'][id] = test_match_document

    return jsonify(response)

@main.route('/delete_pending', methods=['POST'])
@token_auth.login_required
def dalete_pending():
    '''
     Delete the specific task_id or test_id in pending
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data:
        return bad_request('task_id is required.')
    if 'test_id' not in data:
        return bad_request('test_id is required.')
    if 'test_indicator' not in data or not data.get('test_indicator'):
        return bad_request('test_indicator is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data['task_id']
    test_id = data['test_id']
    test_indicator = data['test_indicator']

    print('delete sucess1')
    if test_indicator == 'train':
        id = task_id
    elif test_indicator == 'test':
        id = test_id

    mongoDB.delete_pending_document_field(user_id=user_id, id=id)

    response = {'message': 'delete successfully'}
    return jsonify(response)