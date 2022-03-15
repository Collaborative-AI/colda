# -*- coding: utf-8 -*-
import uuid
import json
import collections

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main

# from Items.models import User, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import log, generate_msg, add_new_token_to_response, obtain_user_id, obtain_unique_id

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

@main.route('/find_assistor', methods=['POST'])
@token_auth.login_required
def find_assistor():

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
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')
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
    assistor_username_list = data['assistor_username_list']
    id_file = data['id_file']
    task_id = data['task_id']
    task_name = data['task_name']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    task_description = data['task_description']

    assistor_id_list = []
    for username in assistor_username_list:
        user = pyMongo.db.User.find_one({'username': username})
        if user is None:
            return jsonify("wrong username")
        user_id = user['user_id']
        print("user.id", username, user_id)
        assistor_id_list.append(user_id)

    user_id = obtain_user_id()
    log(generate_msg('Sponsor training stage'), user_id, task_id)
    log(generate_msg('---- find_assistor begins'), user_id, task_id)
    log(generate_msg('1.1', 'sponsor find_assistor'), user_id, task_id)

    # sponsor_random_id is unique in each task    
    sponsor_random_id = obtain_unique_id()
    match_id_file_id = obtain_unique_id()
    sponsor_id = user_id

    train_match_document = {
        "task_id": task_id,
        'total_assistor_num': len(assistor_id_list),
        "request_timestamp": datetime.utcnow,
        "match_id_timestamp": datetime.utcnow,
        "sponsor_information": {
            "sponsor_id": sponsor_id,
            sponsor_id: {
                "sponsor_id_to_random_id": sponsor_random_id,
                'match_id_file_id': match_id_file_id
            }
        },
        "sponsor_random_id_mapping":{
            sponsor_random_id: sponsor_id
        },
        "assistor_information": {},
        "assistor_random_id_mapping": {},
        'sponsor_terminate_id_dict': {},
        'assistor_terminate_id_dict': {},
    }
    pyMongo.db.Train_Match.insert_one(train_match_document)
    
    train_match_file_document = {
        'match_id_file_id': match_id_file_id,
        'match_id_file_content': id_file,
    }
    pyMongo.db.Train_Match_File.insert_one(train_match_file_document)

    log(generate_msg('1.2:', 'sponsor handles id data done'), user_id, task_id)

    train_task_document = {
        "task_id": task_id,
        "task_name": task_name,
        "task_description": task_description,
        "task_mode": task_mode,
        "model_name": model_name,
        "metric_name": metric_name,
        "sponsor_id": sponsor_id,
        "assistor_id_list": assistor_id_list,
        "test_task_list": [],
    }
    pyMongo.db.Train_Task.insert_one(train_task_document)

    # update the participated_train_task in User Table
    pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{'participated_train_task.' + task_id: 'sponsor'}})

    # add notifications to all assistors
    for assistor_id in assistor_id_list:
        pyMongo.db.Notification.update_one({'user_id': assistor_id}, {'$set':{
            'category.unread_request.task_id_dict.sender_random_id': sponsor_random_id,
            'category.unread_request.task_id_dict.role': 'assistor',
            'category.unread_request.task_id_dict.role': 1,
        }})
    
    log(generate_msg('1.3:', 'sponsor adds all unread request to assistors'), user_id, task_id)

    pyMongo.db.Notification.update_one({'user_id': sponsor_id}, {'$set':{
        'category.unread_request.task_id_dict.sender_random_id': sponsor_random_id,
        'category.unread_request.task_id_dict.role': 'sponsor',
        'category.unread_request.task_id_dict.role': 1,
    }})
    
    log(generate_msg('1.4:', 'sponsor adds unread request to itself'), user_id, task_id)
    log(generate_msg('---- sponsor find assistor done \n'), user_id, task_id)

    response = {"task_id": task_id, 'assistor_num': len(assistor_id_list)}
    return jsonify(response)


@main.route('/find_test_assistor', methods=['POST'])
@token_auth.login_required
def find_test_assistor():

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
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')
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

    task_id = data['task_id']
    test_id = data['test_id']
    id_file = data['id_file']
    test_name = data['test_name']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    test_description = data['test_description']

    # obtain assistor_id_list
    assistor_id_list = []
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    for assistor_id in train_match_document['assistor_information']:
        assistor_id_list.append(assistor_id)

    # update test_task_list    
    test_task_list = train_match_document['test_task_list']
    test_task_list.append(test_id)
    pyMongo.db.Train_Match.update_one({'task_id': task_id}, {'$set':{'test_task_list':test_task_list}})

    user_id = obtain_user_id()
    log(generate_msg('Sponsor testing stage'), user_id, task_id)
    log(generate_msg('---- find_test_assistor begins'), user_id, task_id, test_id)
    log(generate_msg('Test 1.1', 'sponsor find_assistor'), user_id, task_id, test_id)
    
    data_array_id = id_file
    data_array_id = json.dumps(data_array_id)
    log(generate_msg('Test 1.2', 'sponsor handles id data done'), user_id, task_id, test_id)

    print("assistor_id_list", assistor_id_list)

    assistor_information = collections.defaultdict(dict)
    assistor_random_id_mapping = {}
    test_match_file_document_list = []
    for assistor_id in assistor_id_list:
        assistor_random_id = obtain_unique_id()
        match_id_file_id = obtain_unique_id()
        assistor_information[assistor_id]['assistor_id_to_random_id'] = assistor_random_id
        assistor_information[assistor_id]['match_id_file_id'] = match_id_file_id

        assistor_random_id_mapping[assistor_random_id] = assistor_id

        test_match_file_document = {
            "match_id_file_id": match_id_file_id,
            "match_id_file_content": id_file
        }
        test_match_file_document_list.append(test_match_file_document)

    pyMongo.db.Test_Match_File.insert_many(test_match_file_document_list)

    # sponsor_random_id is unique in each task    
    sponsor_random_id = obtain_unique_id()
    sponsor_id = user_id

    test_match_document = {
        "test_id": test_id,
        "task_id": task_id,
        "request_timestamp": datetime.utcnow,
        "match_id_timestamp": datetime.utcnow,
        "sponsor_information": {
            "sponsor_id": sponsor_id,
            sponsor_id: {
                "sponsor_id_to_random_id": sponsor_random_id,
            }
        },
        "sponsor_random_id_mapping":{
            sponsor_random_id: sponsor_id
        },
        "assistor_information": assistor_information,
        "assistor_random_id_mapping": assistor_random_id_mapping,
        "assistor_match_done_dict": {},
        'sponsor_terminate_id_dict': {},
        'assistor_terminate_id_dict': {},
    }
    pyMongo.db.Test_Match.insert_one(test_match_document)
 
    test_task_document = {
        "test_id": test_id,
        "task_id": task_id,
        "test_name": test_name,
        "test_description": test_description,
        "task_mode": task_mode,
        "model_name": model_name,
        "metric_name": metric_name,
        "sponsor_id": sponsor_id,
        "assistor_id_list": assistor_id_list,
    }
    pyMongo.db.Test_Task.insert_one(test_task_document)

    user.add_notification('unread request', user.new_request()) 

    data = {"task_id": task_id, 'assistor_num': len(assistor_id_list), 'test_id': test_id}
    
    log(generate_msg('Test 1.4', 'sponsor adds unread request to itself'), user_id, task_id, test_id)
    log(generate_msg('---- sponsor find_test_assistor done\n'), user_id, task_id, test_id)

    return jsonify(data)

@main.route('/get_test_history_id', methods=['POST'])
@token_auth.login_required
def get_test_history_id():

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    task_id = data['task_id']
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    
    data = {"test_id_list": train_match_document['test_task_list']}
    print("test_id_list", data)
    response = jsonify(data)
    
    return response