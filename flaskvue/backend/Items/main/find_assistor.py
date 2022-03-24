# -*- coding: utf-8 -*-
import uuid
import json
import collections

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import pyMongo
from Items.main import main
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import log, generate_msg, add_new_token_to_response
from Items.main.utils import obtain_user_id_from_token, obtain_unique_id
from Items.main.utils import verify_token_user_id_and_function_caller_id
from Items.main.mongoDB import mongoDB, train_match, train_match_identifier, train_task
from Items.main.mongoDB import mongoDB, test_match, test_match_identifier, test_task

@main.route('/create_new_train_task', methods=['GET'])
@token_auth.login_required
def create_new_train_task():

    """
    Generate a new train task id from unique uuid4

    Parameters:
        None

    Returns:
        task_id - String. String task_id

    Raises:
        KeyError - raises an exception
    """

    task_id = obtain_unique_id()

    response = {"task_id": task_id}
    return jsonify(response)

@main.route('/create_new_test_task', methods=['GET'])
@token_auth.login_required
def create_new_test_task():

    """
    Generate a new test task id from unique uuid4

    Parameters:
        None

    Returns:
        test_id - String. String test_id

    Raises:
        KeyError - raises an exception
    """

    test_id = obtain_unique_id()

    response = {"test_id": test_id}
    return jsonify(response)

@main.route('/find_assistor/<string:id>', methods=['POST'])
@token_auth.login_required
def find_assistor(id):

    """
    Add information of current task to matched database.

    Parameters:
        assistor_username_list - List[String]. The username of assistors for this task. 
        id_file - String. The matching id file sent by sponsor
        task_id - String. The id of task
        task_name - String. The name of task, which could be None.
        task_description - String. The description of task, which could be None.

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task }

    Raises:
        KeyError - raises an exception
    """

    # check the data sent by the sponsor
    data = request.get_json()
    # print('data', data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'assistor_username_list' not in data or not data.get('assistor_username_list'):
        return bad_request('assistor_username_list is required.')
    if 'identifier_content' not in data or not data.get('identifier_content'):
        return bad_request('identifier_content is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'task_mode' not in data:
        return bad_request('task_mode is required.')
    if 'model_name' not in data:
        return bad_request('model_name is required.')
    if 'metric_name' not in data:
        return bad_request('metric_name is required.')
    if 'task_name' not in data:
        return bad_request('task_name is required.')
    if 'task_description' not in data:
        return bad_request('task_description is required.')
    print('find_assistor----------------')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    assistor_username_list = data['assistor_username_list']
    identifier_content = data['identifier_content']
    task_id = data['task_id']
    task_name = data['task_name']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    task_description = data['task_description']

    assistor_id_list = []
    for username in assistor_username_list:
        user_document = mongoDB.search_user_document(user_id=None, username=username, 
                                                     email=None, key_indicator='username')
        if user_document is None:
            return jsonify("wrong username")
        assistor_user_id = user_document['user_id']
        assistor_id_list.append(assistor_user_id)

    log(generate_msg('Sponsor training stage'), user_id, task_id)
    log(generate_msg('---- find_assistor begins'), user_id, task_id)
    log(generate_msg('1.1', 'sponsor find_assistor'), user_id, task_id)

    # sponsor_random_id is unique in each task    
    sponsor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()
    print('identifier_id_1', identifier_id)
    sponsor_id = user_id
    # add new train_match document to Train_Match Table
    train_match.create_train_match_document(task_id=task_id, total_assistor_num=len(assistor_id_list), sponsor_id=sponsor_id, 
                                     sponsor_random_id=sponsor_random_id, identifier_id=identifier_id)
    
    # add new train_match_file document to Train_Match_File Table
    train_match_identifier.create_train_match_identifier_document(identifier_id=identifier_id, identifier_content=identifier_content)

    log(generate_msg('1.2:', 'sponsor handles id data done'), user_id, task_id)

    # add new train_task document to Train_Task Table
    train_task.create_train_task_document(task_id=task_id, task_name=task_name, task_description=task_description, 
                                             task_mode=task_mode, model_name=model_name, metric_name=metric_name, 
                                             sponsor_id=sponsor_id, assistor_id_list=assistor_id_list, test_task_list=[])

    # update the participated_train_task in User Table
    pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{
        'participated_train_task.' + task_id + '.role': 'sponsor'
    }})

    print('-----sdfasdfsafss')
    # add notifications to all assistors
    print('assistor_id_list', user_id, assistor_id_list)
    for assistor_id in assistor_id_list:
        mongoDB.update_notification_document(user_id=assistor_id, notification_name='unread_request', 
                                                 id=task_id, sender_random_id=sponsor_random_id, 
                                                 role='assistor', cur_rounds_num=1, test_indicator='train')
    print('sdfsadfasdfascvv')
    log(generate_msg('1.3:', 'sponsor adds all unread request to assistors'), user_id, task_id)
    log(generate_msg('---- sponsor find assistor done \n'), user_id, task_id)

    response = {
        'task_id': task_id, 
        'assistor_num': len(assistor_id_list)
    }
    return jsonify(response)


@main.route('/find_test_assistor/<string:id>', methods=['POST'])
@token_auth.login_required
def find_test_assistor(id):

    """
    Add information of current task to matched database.

    Parameters:
        assistor_username_list - List[String]. The username of assistors for this task. 
        id_file - String. The matching id file sent by sponsor
        task_id - String. The id of task
        test_id - String. The id of test
        test_name - String. The name of test, which could be None.
        test_description - String. The description of test, which could be None.

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task, test_id - String: The id of test }

    Raises:
        KeyError - raises an exception
    """

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'identifier_content' not in data or not data.get('identifier_content'):
        return bad_request('identifier_content is required.')
    if 'task_mode' not in data:
        return bad_request('task_mode is required.')
    if 'model_name' not in data:
        return bad_request('model_name is required.')
    if 'metric_name' not in data:
        return bad_request('metric_name is required.')
    if 'test_name' not in data:
        return bad_request('test_name is required.')
    if 'test_description' not in data:
        return bad_request('test_description is required.')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id, username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data['task_id']
    test_id = data['test_id']
    identifier_content = data['identifier_content']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    test_name = data['test_name']
    test_description = data['test_description']
    
    # obtain assistor_id_list
    assistor_id_list = []
    train_match_document = train_match.search_train_match_document(task_id=task_id)
    for assistor_id in train_match_document['assistor_information']:
        assistor_id_list.append(assistor_id)

    # update test_task_list    
    train_task.update_train_task_document_test_task_list(task_id=task_id, test_id=test_id)

    log(generate_msg('Sponsor testing stage'), user_id, task_id)
    log(generate_msg('---- find_test_assistor begins'), user_id, task_id, test_id)
    log(generate_msg('Test 1.1', 'sponsor find_assistor'), user_id, task_id, test_id)
    
    print("assistor_id_list", assistor_id_list)

    # sponsor_random_id is unique in each task    
    sponsor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()
    sponsor_id = user_id

    # add new train_match document to Train_Match Table
    test_match.create_test_match_document(task_id=task_id, test_id=test_id, total_assistor_num=len(assistor_id_list), 
                                            sponsor_id=sponsor_id, sponsor_random_id=sponsor_random_id, identifier_id=identifier_id)

    
    # add new train_match_file document to Train_Match_File Table
    test_match_identifier.create_test_match_identifier_document(identifier_id=identifier_id, identifier_content=identifier_content)
    
    
    log(generate_msg('Test 1.2', 'sponsor handles id data done'), user_id, task_id, test_id)

    # add new train_task document to Train_Task Table
    test_task.create_test_task_document(test_id=test_id, task_id=task_id, test_name=test_name, test_description=test_description, 
                                           task_mode=task_mode, model_name=model_name, metric_name=metric_name, 
                                           sponsor_id=sponsor_id, assistor_id_list=assistor_id_list)
    
    
    for assistor_id in assistor_id_list:
        mongoDB.update_notification_document(user_id=assistor_id, notification_name='unread_test_request', 
                                                  id=test_id, sender_random_id=sponsor_random_id, 
                                                  role='assistor', cur_rounds_num=1, test_indicator='test')
    print('sdfsadfasdfascvv')
    log(generate_msg('Test 1.3:', 'sponsor adds all unread request to assistors'), user_id, task_id, test_id)
    log(generate_msg('---- sponsor find_test_assistor done \n'), user_id, task_id, test_id)

    response = {
        'task_id': task_id, 
        'assistor_num': len(assistor_id_list),
        'test_id': test_id
    }
    return jsonify(response)

