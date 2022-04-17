# -*- coding: utf-8 -*-
import math
import heapq

from flask import request, current_app
from flask.json import jsonify

from Items.helper_api import helper_api_bp
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id

from Items.mongoDB import mongoDB
from Items.mongoDB import train_task, train_match
from Items.mongoDB import test_task

@helper_api_bp.route('/get_user_history/<string:id>', methods=['GET'])
@token_auth.login_required
def get_user_history(id):

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    # print('zheli')
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    print('page', page)
    print('per_page', per_page)

    participated_train_task = user_document['participated_train_task']
    # print('participated_train_taskddd', participated_train_task)
    participated_task = []
    for task_id in participated_train_task:
        train_task_document = train_task.search_train_task_document(task_id=task_id)
        if train_task_document == None:
            continue

        task_name = None
        task_description = None
        if 'task_name' in train_task_document:
            task_name = train_task_document['task_name']
        if 'task_description' in train_task_document:
            task_description = train_task_document['task_description']
        timestamp = train_task_document['_id'].generation_time
        sub_task = {
            'task_id': task_id,
            'timestamp': timestamp,
            'task_name': task_name,
            'task_description': task_description,
            'test_indicator': 'train',
            'test_id': None,
            'test_name': None,
            'test_description': None,
        }
        # print('timestamp', timestamp)
        # if train_task_document != None:
        #     timestamp = timestamp.utcnow().timestamp()
        # print('current_time', timestamp, type(timestamp))
        heapq.heappush(participated_task, (-timestamp, sub_task))

        # print('train_task_document', train_task_document)
        if train_task_document != None:
            test_task_dict = train_task_document['test_task_dict']
            for test_id in test_task_dict:
                test_task_document = test_task.search_test_task_document(test_id=test_id)
                if test_task_document == None:
                    continue
                
                test_name = None
                test_description = None
                if 'test_name' in test_task_document:
                    test_name = test_task_document['test_name']
                if 'test_description' in test_task_document:
                    test_description = test_task_document['test_description']
                # obtain timestamp from ObjectID object
                timestamp = test_task_document['_id'].generation_time
                sub_task = {
                    'task_id': task_id,
                    'timestamp': timestamp,
                    'task_name': None,
                    'task_description': None,
                    'test_indicator': 'test',
                    'test_id': test_id,
                    'test_name': test_name,
                    'test_description': test_description,
                }
                # if test_task_document != None:
                #     timestamp = timestamp.utcnow().timestamp()
                heapq.heappush(participated_task, (-timestamp, sub_task))
    
    # sub_task with larger timestamp indicates the closer task
    # Put the closer task at front position
    participated_sort_task_dict = {}
    while participated_task:
        _, sub_task = heapq.heappop(participated_task)
        if sub_task['test_indicator'] == 'test':
            participated_sort_task_dict[sub_task['test_id']] = sub_task
        elif sub_task['test_id'] == None:
            participated_sort_task_dict[sub_task['task_id']] = sub_task
    
    response = {
        'participated_sort_task_dict': participated_sort_task_dict,
        '_meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': math.ceil(len(participated_sort_task_dict) / per_page),
            'total_items': len(participated_sort_task_dict),
        },
    }
    # print('list1', response)
    return jsonify(response)

@helper_api_bp.route('/check_sponsor/<string:id>', methods=['POST'])
@token_auth.login_required
def check_sponsor(id):

    data = request.get_json()
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
    
    task_match_document = train_match.search_train_match_document(task_id=task_id)
    sponsor_id = task_match_document['sponsor_information']['sponsor_id']

    if sponsor_id == user_id:
        role = "sponsor"
    else:
        role = "assistor"

    response = {
        'role': role
    }
    return jsonify(response)


@helper_api_bp.route('/get_test_task_id_history/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_task_id_history(id):

    """
    return test task ids belong to one train task id.

    Parameters:
        task_id - String.

    Returns:
        data - Dict{
            "test_id_list": List[test_task_id]
        }. 

    Raises:
        KeyError - raises an exception
    """

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
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
    train_task_document = train_task.search_train_task_document(task_id=task_id)
    
    response = {
        "test_task_dict": train_task_document['test_task_dict']
    }    
    return jsonify(response)