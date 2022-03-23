# -*- coding: utf-8 -*-
import uuid
import json

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from bson import ObjectId
from datetime import datetime

# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main import main
# from Items.models import User, Notification, Matched, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.mongoDB import mongoDB, train_mongoDB, test_mongoDB
from Items.main.utils import log, generate_msg, obtain_user_id_from_token, obtain_unique_id
from Items.main.utils import verify_token_user_id_and_function_caller_id

@main.route('/get_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_identifier_content(id):

    """
    Sponsor or assistor obtains the same_identifiers generated by sponsor and assistor.

    Parameters:
       task_id - String. The id of current train task
       
    Returns:
        If sponsor:
            {
                'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
            }
        elif assistor:
            {
                'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
            }

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    user_document = mongoDB.search_user_document(user_id=id)
    if user is None:
        return error_response(403)

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data.get('task_id')

    log(generate_msg('---- unread match id begins'), user_id, task_id)
    log(generate_msg('3.1:', 'get_user_match_id begins'), user_id, task_id)

    # check if the current client is the sponsor
    isSponsor = False
    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    if sponsor_id == user_id:
        isSponsor = True 

    response = {}
    if isSponsor:
        assistor_random_id_to_identifier_content_dict = {}
        assistor_information = train_match_document['assistor_information']
        for assistor_id in assistor_information:
            identifier_id = assistor_information[assistor_id]['identifier_id']
            assistor_random_id = assistor_information[assistor_id]['assistor_id_to_random_id']

            train_match_identifier_document = train_mongoDB.search_train_match_identifier_document(identifier_id=identifier_id)
            identifier_content = train_match_identifier_document['identifier_content']

            assistor_random_id_to_identifier_content_dict[assistor_random_id] = identifier_content

        response = {
            'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
        }
        log(generate_msg('3.2:', 'get_user_match_id done'), user_id, task_id)
    else:
        sponsor_random_id_to_identifier_content_dict = {}
        assistor_id = user_id
        assistor_information = train_match_document['assistor_information']
        sponsor_information = train_match_document['sponsor_information']

        identifier_id = assistor_information[assistor_id]['identifier_id']
        sponsor_random_id =sponsor_information[sponsor_id]['sponsor_id_to_random_id']

        train_match_identifier_document = train_mongoDB.search_train_match_identifier_document(identifier_id=identifier_id)
        identifier_content = train_match_identifier_document['identifier_content']

        sponsor_random_id_to_identifier_content_dict[sponsor_random_id] = identifier_content

        response = {
            'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
        }

        log(generate_msg('3.2:', 'get_user_match_id done'), user_id, task_id)
        log(generate_msg('---- unread match id done\n'), user_id, task_id)
    
    return jsonify(response)


@main.route('/get_test_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_identifier_content(id):

    """
    Sponsor or assistor obtains the same_identifiers generated by sponsor and assistor.

    Parameters:
       task_id - String. The id of train task
       test_id - String. The id of test task
       
    Returns:
        If sponsor:
            {
                'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
            }
        elif assistor:
            {
                'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
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

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data.get('task_id')
    test_id = data.get('test_id')

    log(generate_msg('---- unread test match id begins'), user_id, task_id, test_id)
    log(generate_msg('Test 3.1:', 'get_user_test_match_id begins'), user_id, task_id, test_id)

    # check if the current client is the sponsor
    isSponsor = False
    test_match_document = test_mongoDB.search_test_match_document(test_id=test_id)
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    if sponsor_id == user_id:
        isSponsor = True 

    response = {}
    if isSponsor:
        assistor_random_id_to_identifier_content_dict = {}
        assistor_information = test_match_document['assistor_information']
        for assistor_id in test_match_document['assistor_information']:
            identifier_id = assistor_information[assistor_id]['identifier_id']
            assistor_random_id = assistor_information[assistor_id]['assistor_id_to_random_id']

            test_match_identifier_document = test_mongoDB.search_test_match_identifier_document(identifier_id=identifier_id)
            identifier_content = test_match_identifier_document['identifier_content']

            assistor_random_id_to_identifier_content_dict[assistor_random_id] = identifier_content

        response = {
            'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
        }
        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
    else:
        sponsor_random_id_to_identifier_content_dict = {}
        assistor_id = user_id
        assistor_information = test_match_document['assistor_information']
        sponsor_information = test_match_document['sponsor_information']

        identifier_id = assistor_information[assistor_id]['identifier_id']
        sponsor_random_id =sponsor_information[sponsor_id]['sponsor_id_to_random_id']

        test_match_identifier_document = test_mongoDB.search_test_match_identifier_document(identifier_id=identifier_id)
        identifier_content = test_match_identifier_document['identifier_content']

        sponsor_random_id_to_identifier_content_dict[sponsor_random_id] = identifier_content

        response = {
            'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
        }
        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test match id done\n'), user_id, task_id, test_id)

    return jsonify(response)

@main.route('/send_situation/<string:id>', methods=['POST'])
@token_auth.login_required
def send_situation(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'assistor_random_id_to_residual_dict' not in data or not data.get('assistor_random_id_to_residual_dict'):
        return bad_request('residual_list is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    # get data from transferred message
    assistor_random_id_to_residual_dict = data.get('assistor_random_id_to_residual_dict')
    print('residual length', len(assistor_random_id_to_residual_dict))
    task_id = data.get('task_id')

    # get recent round
    cur_rounds_num = None
    train_message_document = train_mongoDB.search_train_message_document(task_id=task_id)
    # if train_message_document is None, it means it is the first round of this train_task
    if train_message_document is None:
        cur_rounds_num = 1
    else:
        cur_rounds_num = train_message_document['cur_rounds_num'] + 1

    if cur_rounds_num == 1:
        log(generate_msg('3.3:', 'sponsor send_situation begins'), user_id, task_id)
    elif cur_rounds_num > 1:
        log(generate_msg('5.3:', 'sponsor send_situation begins'), user_id, task_id)

    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    total_assistor_num = train_match_document['total_assistor_num']
    sponsor_information = train_match_document['sponsor_information']
    assistor_information = train_match_document['assistor_information']
    sponsor_terminate_id_dict = train_match_document['sponsor_terminate_id_dict']
    # check how many assistors in this train task have terminated train task
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
    asssistor_random_id_mapping = train_match_document['asssistor_random_id_mapping']
    sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
    sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

    if sponsor_id in sponsor_terminate_id_dict:
        return jsonify({"message": "sponsor ends train task"})

    situation_dict = {}
    assistor_id_list = []
    for assistor_random_id, residual in assistor_random_id_to_residual_dict.items():

        assistor_id = asssistor_random_id_mapping[assistor_random_id]
        print('send situation assistor_id', assistor_id)
        if assistor_id in assistor_terminate_id_dict:
            continue
        
        assistor_id_list.append(assistor_id)
        sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']

        situation_id = obtain_unique_id()
        situation_dict[assistor_id] = {
            'situation_id': situation_id,
        }

        # assistor add train_message_situation to Train_Message_Situation Table
        train_mongoDB.create_train_message_situation_document(situation_id=situation_id, sender_id=sponsor_id, 
                                                              sender_random_id=sponsor_random_id, recipient_id=assistor_id, 
                                                              situation_content=residual)

    # sponsor also sends information to itself to trigger next stage
    situation_id = obtain_unique_id()
    situation_dict[sponsor_id] = {
        'situation_id': situation_id
    }

    train_mongoDB.create_train_message_situation_document(situation_id=situation_id, sender_id=sponsor_id, 
                                                          sender_random_id=sponsor_random_id, recipient_id=sponsor_id, 
                                                          situation_content=None)

    if cur_rounds_num == 1:
        train_mongoDB.create_train_message_document(task_id=task_id, cur_rounds_num=cur_rounds_num, situation_dict=situation_dict)
    elif cur_rounds_num > 1:
        pyMongo.db.Train_Message.update_one({'task_id': task_id}, {'$set':{
            'cur_rounds_num': cur_rounds_num,
            'rounds_' + str(cur_rounds_num) + '.situation_dict': situation_dict
        }})

    # send unread_situation notification to all assistors in this train task 
    for assistor_id in assistor_id_list:
        train_mongoDB.update_notification_document(user_id=assistor_id, notification_name='unread_situation', 
                                                       task_id=task_id, sender_random_id=sponsor_random_id, 
                                                       role='assistor', cur_rounds_num=1)

    if cur_rounds_num == 1:
        log(generate_msg('3.4:"', 'sponsor adds unread situation to assistors done'), user_id, task_id)
    elif cur_rounds_num > 1:
        log(generate_msg('5.4:"', 'sponsor adds unread situation to assistors done'), user_id, task_id)
    
    # send unread_situation notification to sponsor in this train task 
    train_mongoDB.update_notification_document(user_id=sponsor_id, notification_name='unread_situation', 
                                                       task_id=task_id, sender_random_id=sponsor_random_id, 
                                                       role='sponsor', cur_rounds_num=1)

    if cur_rounds_num == 0:
        log(generate_msg('3.5:"', 'sponsor add unread situation to sponsor done'), user_id, task_id)
        log(generate_msg('------------------------ unread situation done\n'), user_id, task_id)
    else:
        log(generate_msg('5.5:"', 'sponsor add unread situation to sponsor done'), user_id, task_id)
        log(generate_msg('------------------------ unread output done\n'), user_id, task_id)

    response = {
        "message": "send situation successfully!"
    }
    return jsonify(response)


@main.route('/send_test_output/<string:id>', methods=['POST'])
@token_auth.login_required
def send_test_output(id):

    
    """
    1. Assistors send test outputs in this function to sponsor. Only when all the assistors in test task upload
    their outputs, server will send sponsor the unread_test_output notifications.
    2. Only assistor will enter this function

    Parameters:
        task_id - String. The id of current train task
        output_content - List
       
    Returns:
        {"send_test_output": "send test output successfully"}

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'output_content' not in data or not data.get('output_content'):
        return bad_request('output_content is required.')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    output_content = data.get('output_content')
    test_id = data.get('test_id')
    task_id = data.get('task_id')
    assistor_id = user_id

    log(generate_msg('Test 3.3:"', 'assistor send_test_output start'), user_id, task_id, test_id)

    test_match_document = test_mongoDB.search_test_match_document(test_id=test_id)
    total_assistor_num = test_match_document['total_assistor_num']
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    assistor_random_id = test_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
    assistor_terminate_id_dict = test_match_document['assistor_terminate_id_dict']

    cur_rounds_num = 1

    output_id = obtain_unique_id()
    res = test_mongoDB.update_test_message_document(test_id=test_id, cur_rounds_num=cur_rounds_num, 
                                                    assistor_id=assistor_id, output_id=output_id)

    test_mongoDB.create_test_message_output_document(output_id=output_id, sender_id=assistor_id,
                                                     sender_random_id=assistor_random_id, recipient_id=sponsor_id,
                                                     output_content=output_content)

    # check how many assistors are still participate in this train task
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)

    # check how many assistors have uploaded their output 
    # if the number of output surpasses the ramin_assistor_num, we can send notifications
    test_message_document = test_mongoDB.search_test_message_document(test_id=test_id)
    print('test_message_document', test_message_document)
    output_dict = test_message_document['rounds_' + str(cur_rounds_num)]['output_dict']
    print('test_message_document')
    if len(output_dict) >= remain_assistor_num:
        print('gggggggggggggg')
        test_mongoDB.update_notification_document(user_id=sponsor_id, notification_name='unread_test_output', 
                                                   test_id=test_id, sender_random_id=assistor_random_id, 
                                                   role='sponsor', cur_rounds_num=cur_rounds_num)
        log(generate_msg('Test 3.4:"', 'assistor uploads all test output'), user_id, task_id, test_id)
    else:
        print('xxxxxx')
        log(generate_msg('Test 3.4:"', 'assistor send_test_output done'), user_id, task_id, test_id)

    log(generate_msg('----------------------- unread_test_match_id done\n'), user_id, task_id, test_id)
    
    response = {
        "send_test_output": "send test output successfully"
    }
    return jsonify(response)

    