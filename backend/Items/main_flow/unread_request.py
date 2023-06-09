from __future__ import annotations
import sys

# -*- coding: utf-8 -*-
from flask import request
from flask.json import jsonify

# import BluePrint
from Items import pyMongo
from Items.main_flow import main_flow_bp
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.utils import log, generate_msg, obtain_unique_id
from Items.utils.api import (
    check_if_data_is_valid,
    input_data_err_msg
)

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_match_identifier
from Items.mongoDB import test_match, test_match_identifier

@main_flow_bp.route('/match_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def match_identifier_content(id):

    """
    Match the identifier of sponsor and assistor

    Parameters:
        train_id - String. The id of task
        identifier_content - List. The identifier list sent by sponsor

    Returns:
        data - {
                    train_id - String: The id of task, 
                    assistor_num - Integer: The number of assistors in this task
                }

    Raises:
        KeyError - raises an exception
    """
    
    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')

    expected_data = {
        'train_id': str,
        'identifier_content': list
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
    identifier_content = data.get('identifier_content')
    assistor_id = user_id

    train_match_document = train_match.search_train_match_document(train_id=train_id)
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    sponsor_information = train_match_document['sponsor_information']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    train_match_identifier_document = train_match_identifier.search_train_match_identifier_document(identifier_id=sponsor_identifier_id)
    if train_match_identifier_document['is_large_file'] == False:
        sponsor_identifier_content = train_match_identifier_document['identifier_content']
    elif train_match_identifier_document['is_large_file'] == True:
        gridfs_id = train_match_identifier_document['identifier_content']
        sponsor_identifier_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_id)

    log(generate_msg('Assistor training stage'), user_id, train_id)
    log(generate_msg('---- unread request begins'), user_id, train_id)
    log(generate_msg('2.1:', 'assistor match_assistor_id begins'), user_id, train_id)

    same_identifiers = list(set(identifier_content) & set(sponsor_identifier_content))

    assistor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()

    train_match.assistor_update_train_match_document(
        train_id=train_id, 
        assistor_id=assistor_id, 
        assistor_random_id=assistor_random_id, 
        identifier_id=identifier_id
    )

    # add new train_match_file document to Train_Match_File Table
    train_match_identifier.create_train_match_identifier_document(
        identifier_id=identifier_id, 
        identifier_content=same_identifiers
    )
    
    log(generate_msg('2.2:', 'assistor matching', user_id), user_id, train_id)
    
    # update the participated_train_task in User Table
    pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{
        f'participated_train_task.{train_id}.role': 'assistor'
    }})

    train_match_document = train_match.search_train_match_document(train_id=train_id)
    assistor_information = train_match_document['assistor_information']
    total_assistor_num = train_match_document['total_assistor_num']
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)
    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_information)), user_id, train_id)
        # send unread_match_identifier notification to assistors
        for assistor_id in assistor_information:
            mongoDB.update_notification_document(
                user_id=assistor_id, 
                notification_name='unread_match_identifier', 
                train_id=train_id, 
                sender_random_id=sponsor_random_id, 
                role='assistor', 
                cur_rounds_num=1, 
                test_indicator='train'
            )
                                                        
        # send unread_match_identifier notification to sponsor
        mongoDB.update_notification_document(
            user_id=sponsor_id, 
            notification_name='unread_match_identifier', 
            train_id=train_id, 
            sender_random_id=sponsor_random_id, 
            role='sponsor', 
            cur_rounds_num=1, 
            test_indicator='train'
        )

        log(generate_msg('2.4:', 'Server sends unread match id to all participants of this task (sponsor and all assistors)'), user_id, train_id)

    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('2.5:', 'assistor match_assistor_id done'), user_id, train_id)
        log(generate_msg('---- unread request done\n'), user_id, train_id)
    else:
        log(generate_msg('2.3:', 'assistor match_assistor_id done'), user_id, train_id)
        log(generate_msg('---- unread request done\n'), user_id, train_id)

    response = {
        "stored": "assistor match id stored",
        "train_id": train_id
    }
    return jsonify(response)


@main_flow_bp.route('/match_test_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def match_test_identifier_content(id):

    """
    Match the identifier of sponsor and assistor for test task

    Parameters:
        train_id - String. The id of train task
        test_id - String. The id of test task
        identifier_content - List. The identifier list sent by sponsor

    Returns:
        data - { 
                    test_id - String: The id of task, 
                    assistor_num - Integer: The number of assistors in this task 
                }

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')

    expected_data = {
        'train_id': str,
        'test_id': str,
        'identifier_content': list
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
    test_id = data.get('test_id')
    identifier_content = data.get('identifier_content')
    assistor_id = user_id

    test_match_document = test_match.search_test_match_document(test_id=test_id)
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    sponsor_information = test_match_document['sponsor_information']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    test_match_identifier_document = test_match_identifier.search_test_match_identifier_document(identifier_id=sponsor_identifier_id)
    if test_match_identifier_document['is_large_file'] == False:
        sponsor_identifier_content = test_match_identifier_document['identifier_content']
    elif test_match_identifier_document['is_large_file'] == True:
        gridfs_id = test_match_identifier_document['identifier_content']
        sponsor_identifier_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_id)
    
    log(generate_msg('Assistor testing stage'), user_id, train_id, test_id)
    log(generate_msg('---- unread test request begins'), user_id, train_id, test_id)
    log(generate_msg('Test 2.1:', 'assistor match_test_assistor_id begins'), user_id, train_id, test_id)

    same_identifiers = list(set(identifier_content) & set(sponsor_identifier_content))

    assistor_random_id = obtain_unique_id()
    identifier_id = obtain_unique_id()

    test_match.assistor_update_test_match_document(test_id=test_id, assistor_id=assistor_id, 
                                                     assistor_random_id=assistor_random_id, identifier_id=identifier_id)

    # add new train_match_file document to Train_Match_File Table
    test_match_identifier.create_test_match_identifier_document(identifier_id=identifier_id, identifier_content=same_identifiers)                                             
    log(generate_msg('Test 2.2:', 'assistor matching', user_id), user_id, train_id, test_id)

    test_match_document = test_match.search_test_match_document(test_id=test_id)
    assistor_information = test_match_document['assistor_information']
    total_assistor_num = test_match_document['total_assistor_num']
    assistor_terminate_id_dict = test_match_document['assistor_terminate_id_dict']
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)
    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('Test 2.3:', 'assistor matching_done', 'number of assistor:', len(assistor_information)), user_id, train_id, test_id)

        for assistor_id in assistor_information:
            mongoDB.update_notification_document(
                user_id=assistor_id, 
                notification_name='unread_test_match_identifier', 
                train_id=train_id, 
                sender_random_id=sponsor_random_id, 
                role='assistor', 
                cur_rounds_num=1, 
                test_indicator='test',
                test_id=test_id
            )
                                                        
        # send unread_match_identifier notification to sponsor
        mongoDB.update_notification_document(
            user_id=sponsor_id, 
            notification_name='unread_test_match_identifier', 
            train_id=train_id, 
            sender_random_id=sponsor_random_id, 
            role='sponsor', 
            cur_rounds_num=1, 
            test_indicator='test',
            test_id=test_id
        )
                                                  
        log(generate_msg('Test 2.4:', 'Server sends unread match id to all participants of this test task'), user_id, train_id, test_id)

    if len(assistor_information) >= remain_assistor_num:
        log(generate_msg('Test 2.5:', 'assistor match_test_assistor_id done'), user_id, train_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, train_id, test_id)
    else:
        log(generate_msg('Test 2.3:', 'assistor match_test_assistor_id done'), user_id, train_id, test_id)
        log(generate_msg('---- unread test request done\n'), user_id, train_id, test_id)

    response = {
        "stored": "assistor test match id stored",
        "test_id": test_id
    }
    return jsonify(response)
    
    
