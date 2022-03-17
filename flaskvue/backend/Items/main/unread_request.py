# -*- coding: utf-8 -*-
import uuid
import json
import time

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.utils import log, generate_msg, obtain_unique_id

# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main

# from Items.models import User, Notification, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.main.mongoDB import train_mongoDB, test_mongoDB

@main.route('/match_identifier_content/<int:id>', methods=['POST'])
@token_auth.login_required
def match_identifier_content():

    """
    Match the id of sponsor and assistor

    Parameters:
        task_id - String. The id of task
        file - String. The matching id file sent by sponsor

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task }

    Raises:
        KeyError - raises an exception
    """
    
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'identifier_content' not in data or not data.get('identifier_content'):
        return bad_request('identifier_content is required.')

    task_id = data.get('task_id')
    identifier_content = data.get('identifier_content')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    assistor_id = user_id

    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    total_assistor_num = train_match_document['total_assistor_num']
    sponsor_information = train_match_document['sponsor_information']
    assistor_information = train_match_document['assistor_information']
    sponsor_terminate_id_dict = train_match_document['sponsor_terminate_id_dict']
    # check how many assistors in this train task have terminated train task
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
    asssistor_random_id_mapping = train_match_document['assistor_random_id_mapping']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    train_match_file_document = pyMongo.db.Train_Match_File.find_one({'identifier_id': sponsor_identifier_id})
    sponsor_match_id_file = train_match_file_document['identifier_content']

    log(generate_msg('Assistor training stage'), user_id, task_id)
    log(generate_msg('---- unread request begins'), user_id, task_id)
    log(generate_msg('2.1:', 'assistor match_assistor_id begins'), user_id, task_id)

    same_id_keys = list(set(identifier_content) & set(sponsor_match_id_file))
    print('same_id_keys', same_id_keys)

    assistor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()

    train_mongoDB.assistor_update_train_match_document(task_id=task_id, assistor_id=assistor_id, 
                                                 assistor_random_id=assistor_random_id, identifier_id=identifier_id)

    # add new train_match_file document to Train_Match_File Table
    train_mongoDB.add_match_file_document(identifier_id=identifier_id, identifier_content=same_id_keys)
    
    log(generate_msg('2.2:', 'assistor matching', user_id), user_id, task_id)
    
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)
    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_information)), user_id, task_id)
        # send unread_match_id notification to assistors
        for assistor_id in assistor_information:
            train_mongoDB.update_notification_document(user_id=assistor_id, notification_name='unread_match_id', 
                                                       task_id=task_id, sender_random_id=sponsor_random_id, 
                                                       role='assistor', cur_rounds_num=1)
                                                        
        # send unread_match_id notification to sponsor
        train_mongoDB.update_notification_document(user_id=sponsor_id, notification_name='unread_match_id', 
                                                   task_id=task_id, sender_random_id=sponsor_random_id, 
                                                   role='sponsor', cur_rounds_num=1)
        log(generate_msg('2.4:', 'Server sends unread match id to all participants of this task (sponsor and all assistors)'), user_id, task_id)

    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.5:', 'assistor match_assistor_id done'), user_id, task_id)
        log(generate_msg('---- unread request done\n'), user_id, task_id)
    else:
        log(generate_msg('2.3:', 'assistor match_assistor_id done'), user_id, task_id)
        log(generate_msg('---- unread request done\n'), user_id, task_id)

    return jsonify({"stored": "assistor match id stored", "task_id": task_id})


@main.route('/match_test_identifier_content/<int:id>', methods=['POST'])
@token_auth.login_required
def match_test_identifier_content():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)
        
    task_id = data.get('task_id')
    test_id = data.get('test_id')
    data_array = data.get('file')

    user_id = obtain_user_id_from_token()

    test_match_document = pyMongo.db.Test_Match.find_one({'test_id': test_id})
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    identifier_id = test_match_document['assistor_information'][user_id]['identifier_id']
    asssistor_random_id_mapping = test_match_document['asssistor_random_id_mapping']
    assistor_match_done_dict = test_match_document['assistor_match_done_dict']

    test_match_file_document = pyMongo.db.Test_Match_File.find_one({'identifier_id': identifier_id})
    match_id_file = test_match_file_document['identifier_content']
    
    log(generate_msg('Assistor testing stage'), user_id, task_id, test_id)
    log(generate_msg('---- unread test request begins'), user_id, task_id, test_id)
    log(generate_msg('Test 2.1:', 'assistor match_test_assistor_id begins'), user_id, task_id, test_id)

    data_array_id = set(data_array)
    db_array = json.loads(match_id_file)
    same_id_keys = list(data_array_id & set(db_array))
    pyMongo.db.Test_Match_File.update_one({'identifier_id': identifier_id}, {'$set':{'identifier_content': same_id_keys}})
    log(generate_msg('Test 2.2:', 'assistor matching', user_id), user_id, task_id, test_id)

    assistor_match_done_dict[user_id] = True
    pyMongo.db.Test_Match.update_one({'test_id': test_id}, {'$set':{'assistor_match_done_dict': assistor_match_done_dict}})
    if len(assistor_match_done_dict) >= len(asssistor_random_id_mapping):
        log(generate_msg('Test 2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_match_done_dict)), user_id, task_id, test_id)
        for key, value in asssistor_random_id_mapping:
            # 要修改
            value.add_notification
            user.add_notification('unread test match id', user.new_test_match_id())
        log(generate_msg('Test 2.4:', 'Server sends unread match id to all participants of this test task'), user_id, task_id, test_id)

    dict = {"stored": "assistor test match id stored", "test_id": test_id}

    if len(assistor_match_done_dict) != len(asssistor_random_id_mapping):
        log(generate_msg('Test 2.3:', 'assistor match_test_assistor_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, task_id, test_id)
    else:
        log(generate_msg('Test 2.5:', 'assistor match_test_assistor_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, task_id, test_id)

    return jsonify(dict)
    
    
