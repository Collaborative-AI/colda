# -*- coding: utf-8 -*-
import uuid
import json
import time

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.utils import log, generate_msg

# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main

# from Items.models import User, Notification, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import obtain_user_object_id_and_user_id

@main.route('/match_assistor_id/', methods=['POST'])
@token_auth.login_required
def match_assistor_id():

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
    
    print('match_assistor_id')
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')

    task_id = data.get('task_id')
    data_array = data['file']

    user_object_id, user_id = obtain_user_object_id_and_user_id()
    assistor_id = user_id

    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    total_assistor_num = train_match_document['total_assistor_num']
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    assistor_information = train_match_document['assistor_information']
    asssistor_random_id_mapping = train_match_document['asssistor_random_id_mapping']
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']

    sponsor_match_id_file_id = train_match_document['sponsor_information'][sponsor_id]['match_id_file_id']
    train_match_file_document = pyMongo.db.Train_Match_File.find_one({'match_id_file_id': sponsor_match_id_file_id})
    sponsor_match_id_file = train_match_file_document['match_id_file_content']

    log(generate_msg('Assistor training stage'), user_id, task_id)
    log(generate_msg('---- unread request begins'), user_id, task_id)
    log(generate_msg('2.1:', 'assistor match_assistor_id begins'), user_id, task_id)

    data_array_id = set(data_array)
    db_array = json.loads(sponsor_match_id_file)
    # print('db_array', type(db_array), db_array)
    # print('data_array_id', type(data_array_id), data_array_id)
    same_id_keys = list(data_array_id & set(db_array))
    # print('same_id_keys', same_id_keys)

    assistor_random_id = str(uuid.uuid4())
    match_id_file_id = str(uuid.uuid4())
    assistor_information[assistor_id]['assistor_id_to_random_id'] = assistor_random_id
    assistor_information[assistor_id]['match_id_file_id'] = match_id_file_id
    asssistor_random_id_mapping[assistor_random_id] = assistor_id
    pyMongo.db.Train_Match.update_one({'task_id': task_id}, {'$set':{
        assistor_information: assistor_information,
        asssistor_random_id_mapping: asssistor_random_id_mapping,
    }})
    # pyMongo.db.Train_Match.update_one({'task_id': task_id}, {'$set':{
    #     assistor_information.assistor_id.assistor_id_to_random_id: assistor_random_id,
    #     assistor_information.assistor_id.match_id_file_id: match_id_file_id,
    #     asssistor_random_id_mapping.assistor_random_id: assistor_id,
    # }})

    train_match_file_document = {
        "match_id_file_id": match_id_file_id,
        "match_id_file_content": same_id_keys
    }
    pyMongo.db.Train_Match_File.insert_many(train_match_file_document)
    log(generate_msg('2.2:', 'assistor matching', user_id), user_id, task_id)
    
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)
    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_match_done_dict)), user_id, task_id)
        for key, value in asssistor_random_id_mapping:
            # 要修改
            value.add_notification
            user.add_notification('unread match id', user.new_match_id())
        log(generate_msg('2.4:', 'Server sends unread match id to all participants of this task'), user_id, task_id)

    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.5:', 'assistor match_assistor_id done'), user_id, task_id)
        log(generate_msg('---- unread request done\n'), user_id, task_id)
    else:
        log(generate_msg('2.3:', 'assistor match_assistor_id done'), user_id, task_id)
        log(generate_msg('---- unread request done\n'), user_id, task_id)

    
    return jsonify({"stored": "assistor match id stored", "task_id": task_id})


@main.route('/match_test_assistor_id/', methods=['POST'])
@token_auth.login_required
def match_test_assistor_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    task_id = data.get('task_id')
    test_id = data.get('test_id')
    data_array = data.get('file')

    user_object_id, user_id = obtain_user_object_id_and_user_id()

    test_match_document = pyMongo.db.Test_Match.find_one({'test_id': test_id})
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    match_id_file_id = test_match_document['assistor_information'][user_id]['match_id_file_id']
    asssistor_random_id_mapping = test_match_document['asssistor_random_id_mapping']
    assistor_match_done_dict = test_match_document['assistor_match_done_dict']

    test_match_file_document = pyMongo.db.Test_Match_File.find_one({'match_id_file_id': match_id_file_id})
    match_id_file = test_match_file_document['match_id_file_content']
    
    log(generate_msg('Assistor testing stage'), g.current_user.id, task_id, test_id)
    log(generate_msg('---- unread test request begins'), g.current_user.id, task_id, test_id)
    log(generate_msg('Test 2.1:', 'assistor match_test_assistor_id begins'), g.current_user.id, task_id, test_id)

    data_array_id = set(data_array)
    db_array = json.loads(match_id_file)
    same_id_keys = list(data_array_id & set(db_array))
    pyMongo.db.Test_Match_File.update_one({'match_id_file_id': match_id_file_id}, {'$set':{'match_id_file_content': same_id_keys}})
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
    
    
