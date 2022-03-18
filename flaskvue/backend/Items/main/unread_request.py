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
from Items.main.mongoDB import mongoDB, train_mongoDB, test_mongoDB

@main.route('/match_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def match_identifier_content(id):

    """
    Match the identifier of sponsor and assistor

    Parameters:
        task_id - String. The id of task
        identifier_content - List. The identifier list sent by sponsor

    Returns:
        data - {
                    task_id - String: The id of task, 
                    assistor_num - Integer: The number of assistors in this task
                }

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

    user_id = obtain_user_id_from_token()
    user = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data.get('task_id')
    identifier_content = data.get('identifier_content')
    assistor_id = user_id

    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    sponsor_information = train_match_document['sponsor_information']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    train_match_identifier_document = train_mongoDB.search_train_match_identifier_document(identifier_id=sponsor_identifier_id)
    sponsor_identifier_content = train_match_identifier_document['identifier_content']

    log(generate_msg('Assistor training stage'), user_id, task_id)
    log(generate_msg('---- unread request begins'), user_id, task_id)
    log(generate_msg('2.1:', 'assistor match_assistor_id begins'), user_id, task_id)

    same_identifiers = list(set(identifier_content) & set(sponsor_identifier_content))
    print('same_identifiers', same_identifiers)

    assistor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()

    train_mongoDB.assistor_update_train_match_document(task_id=task_id, assistor_id=assistor_id, 
                                                 assistor_random_id=assistor_random_id, identifier_id=identifier_id)

    # add new train_match_file document to Train_Match_File Table
    train_mongoDB.create_train_match_identifier_document(identifier_id=identifier_id, identifier_content=same_identifiers)
    
    log(generate_msg('2.2:', 'assistor matching', user_id), user_id, task_id)
    
    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    assistor_information = train_match_document['assistor_information']
    total_assistor_num = train_match_document['total_assistor_num']
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
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

    response = {
        "stored": "assistor match id stored",
        "task_id": task_id
    }
    return jsonify(response)


@main.route('/match_test_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def match_test_identifier_content(id):

    """
    Match the identifier of sponsor and assistor for test task

    Parameters:
        task_id - String. The id of train task
        test_id - String. The id of test task
        identifier_content - List. The identifier list sent by sponsor

    Returns:
        data - { 
                    task_id - String: The id of task, 
                    assistor_num - Integer: The number of assistors in this task 
                }

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'identifier_content' not in data or not data.get('identifier_content'):
        return bad_request('identifier_content is required.')
    
    user_id = obtain_user_id_from_token()
    user = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)
        
    task_id = data.get('task_id')
    test_id = data.get('test_id')
    identifier_content = data.get('identifier_content')
    assistor_id = user_id

    test_match_document = test_mongoDB.search_test_match_document(test_id=test_id)
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    sponsor_information = test_match_document['sponsor_information']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    test_match_identifier_document = test_mongoDB.search_test_match_identifier_document(identifier_id=sponsor_identifier_id)
    sponsor_identifier_content = test_match_identifier_document['identifier_content']
    
    log(generate_msg('Assistor testing stage'), user_id, task_id, test_id)
    log(generate_msg('---- unread test request begins'), user_id, task_id, test_id)
    log(generate_msg('Test 2.1:', 'assistor match_test_assistor_id begins'), user_id, task_id, test_id)

    same_identifiers = list(set(identifier_content) & set(sponsor_identifier_content))

    assistor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()

    test_mongoDB.assistor_update_test_match_document(test_id=test_id, assistor_id=assistor_id, 
                                                     assistor_random_id=assistor_random_id, identifier_id=identifier_id)

    # add new train_match_file document to Train_Match_File Table
    test_mongoDB.create_test_match_identifier_document(identifier_id=identifier_id, identifier_content=same_identifiers)                                             
    log(generate_msg('Test 2.2:', 'assistor matching', user_id), user_id, task_id, test_id)

    test_match_document = test_mongoDB.search_test_match_document(test_id=test_id)
    assistor_information = test_match_document['assistor_information']
    total_assistor_num = test_match_document['total_assistor_num']
    assistor_terminate_id_dict = test_match_document['assistor_terminate_id_dict']
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)
    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('Test 2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_match_done_dict)), user_id, task_id, test_id)
        for assistor_id in assistor_information:
            test_mongoDB.update_notification_document(user_id=assistor_id, notification_name='unread_test_match_id', 
                                                      test_id=test_id, sender_random_id=sponsor_random_id, 
                                                      role='assistor', cur_rounds_num=1)
                                                        
        # send unread_match_id notification to sponsor
        test_mongoDB.update_notification_document(user_id=sponsor_id, notification_name='unread_test_match_id', 
                                                  test_id=test_id, sender_random_id=sponsor_random_id, 
                                                  role='sponsor', cur_rounds_num=1)
        log(generate_msg('Test 2.4:', 'Server sends unread match id to all participants of this test task'), user_id, task_id, test_id)

    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('Test 2.5:', 'assistor match_test_assistor_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, task_id, test_id)
    else:
        log(generate_msg('Test 2.3:', 'assistor match_test_assistor_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, task_id, test_id)

    response = {
        "stored": "assistor test match id stored",
        "test_id": test_id
    }
    return jsonify(response)
    
    
