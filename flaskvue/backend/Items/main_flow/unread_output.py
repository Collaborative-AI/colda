# -*- coding: utf-8 -*-
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime


# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main_flow import main_flow_bp
# from Items.models import User, Notification, Matched, Message
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.utils import log, generate_msg
from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_message, train_message_output
from Items.mongoDB import test_match, test_message, test_message_output

@main_flow_bp.route('/get_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_output_content(id):

    """
    Sponsor gets outputs of assistors. Only sponsor enters this function.

    Parameters:
        task_id - String. The id of task
        rounds - String. The round number

    Returns:
        data - { 
                    assistor_random_id_to_output_content_dict: assistor_random_id_to_output_content_dict
                }

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'rounds' not in data:
        return bad_request('rounds is required.')

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data.get('task_id')
    rounds = data.get('rounds')
    sponsor_id = user_id

    # if caller is not sponsor, it should not enter this function
    task_match_document = train_match.search_train_match_document(task_id=task_id)
    sponsor_id = task_match_document['sponsor_information']['sponsor_id']
    if sponsor_id != user_id:
        return error_response(403)

    log(generate_msg('---- unread situation begins'), user_id, task_id)
    log(generate_msg('---- unread situation done (no function pass server)\n'), user_id, task_id)
    log(generate_msg('---- unread output begins'), user_id, task_id)
    log(generate_msg('5.1:"', 'sponsor get_user_output start'), user_id, task_id)

    train_message_document = train_message.search_train_message_document(task_id=task_id)
    output_dict = train_message_document['rounds_' + str(rounds)]['output_dict']

    assistor_random_id_to_output_content_dict = {}
    for assistor_id in output_dict:
        output_id = output_dict[assistor_id]['output_id']
        train_message_output_document = train_message_output.search_train_message_output_document(output_id=output_id)

        output_content = train_message_output_document['output_content']
        sender_random_id = train_message_output_document['sender_random_id']
        assistor_random_id_to_output_content_dict[sender_random_id] = output_content

    log(generate_msg('5.2:"', 'sponsor get_user_output done'), user_id, task_id)

    response = {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
    }
    return jsonify(response)  


@main_flow_bp.route('/get_test_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_output_content(id):

    """
    Sponsor gets test outputs of assistors. Only sponsor enters this function.
    test stage will only have 1 round

    Parameters:
        task_id - String. The id of train task
        test_id - String. The id of test task

    Returns:
        data - { 
                    assistor_random_id_to_output_content_dict: assistor_random_id_to_output_content_dict
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
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    test_id = data.get('test_id')
    task_id = data.get('task_id')
    sponsor_id = user_id

    # if caller is not sponsor, it should not enter this function
    test_match_document = test_match.search_test_match_document(test_id=test_id)
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    if sponsor_id != user_id:
        return error_response(403)

    log(generate_msg('---- unread test output begins'), user_id, task_id, test_id)
    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output start'), user_id, task_id, test_id)

    test_message_document = test_message.search_test_message_document(test_id=test_id)
    output_dict = test_message_document['rounds_1']['output_dict']

    assistor_random_id_to_output_content_dict = {}
    for assistor_id in output_dict:
        output_id = output_dict[assistor_id]['output_id']
        test_message_output_document = test_message_output.search_test_message_output_document(output_id=output_id)

        output_content = test_message_output_document['output_content']
        sender_random_id = test_message_output_document['sender_random_id']
        assistor_random_id_to_output_content_dict[sender_random_id] = output_content

    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output done'), user_id, task_id, test_id)
    log(generate_msg('--------------------unread test output done\n'), user_id, task_id, test_id)

    response = {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
    }
    return jsonify(response)  