from __future__ import annotations
import sys
# -*- coding: utf-8 -*-
from flask import request
from flask.json import jsonify

# import BluePrint
from Items.main_flow import main_flow_bp
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.mongoDB.train_mongoDB.train_message_situation import train_message_situation
from Items.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.utils import log, generate_msg
from Items.utils.api import (
    check_if_data_is_valid,
    input_data_err_msg
)

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_message, train_message_output
from Items.mongoDB import test_match, test_message, test_message_output

@main_flow_bp.route('/get_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_output_content(id):

    """
    Sponsor gets outputs of assistors. Only sponsor enters this function.

    Parameters:
        train_id - String. The id of task
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
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')

    expected_data = {
        'train_id': str,
        'rounds': int
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

    train_id = data['train_id']
    rounds = data['rounds']
    sponsor_id = user_id

    # if caller is not sponsor, it should not enter this function
    task_match_document = train_match.search_train_match_document(train_id=train_id)
    sponsor_id = task_match_document['sponsor_information']['sponsor_id']
    if sponsor_id != user_id:
        return error_response(403)

    log(generate_msg('---- unread situation begins'), user_id, train_id)
    log(generate_msg('---- unread situation done (no function pass server)\n'), user_id, train_id)
    log(generate_msg('---- unread output begins'), user_id, train_id)
    log(generate_msg('5.1:"', 'sponsor get_user_output start'), user_id, train_id)

    train_message_document = train_message.search_train_message_document(train_id=train_id)
    output_dict = train_message_document[f'rounds_{rounds}']['output_dict']

    assistor_random_id_to_output_content_dict = {}
    for assistor_id in output_dict:
        output_id = output_dict[assistor_id]['output_id']
        train_message_output_document = train_message_output.search_train_message_output_document(output_id=output_id)

        sender_random_id = train_message_output_document['sender_random_id']
        
        if train_message_output_document['is_large_file'] == False:
            output_content = train_message_output_document['output_content']
        elif train_message_output_document['is_large_file'] == True:
            gridfs_file_id = train_message_output_document['output_content']
            output_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_file_id)
        assistor_random_id_to_output_content_dict[sender_random_id] = output_content

    log(generate_msg('5.2:"', 'sponsor get_user_output done'), user_id, train_id)

    response = {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
    }
    print ('output res', response)
    return jsonify(response)  


@main_flow_bp.route('/get_test_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_output_content(id):

    """
    Sponsor gets test outputs of assistors. Only sponsor enters this function.
    test stage will only have 1 round

    Parameters:
        train_id - String. The id of train task
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
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')

    expected_data = {
        'train_id': str,
        'test_id': str,
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

    test_id = data.get('test_id')
    train_id = data.get('train_id')
    sponsor_id = user_id

    # if caller is not sponsor, it should not enter this function
    test_match_document = test_match.search_test_match_document(test_id=test_id)
    sponsor_id = test_match_document['sponsor_information']['sponsor_id']
    if sponsor_id != user_id:
        return error_response(403)

    log(generate_msg('---- unread test output begins'), user_id, train_id, test_id)
    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output start'), user_id, train_id, test_id)

    test_message_document = test_message.search_test_message_document(test_id=test_id)
    output_dict = test_message_document['rounds_1']['output_dict']

    assistor_random_id_to_output_content_dict = {}
    for assistor_id in output_dict:
        output_id = output_dict[assistor_id]['output_id']
        test_message_output_document = test_message_output.search_test_message_output_document(output_id=output_id)

        sender_random_id = test_message_output_document['sender_random_id']
        
        if test_message_output_document['is_large_file'] == False:
            output_content = test_message_output_document['output_content']
        elif test_message_output_document['is_large_file'] == True:
            gridfs_file_id = test_message_output_document['output_content']
            output_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_file_id)
        assistor_random_id_to_output_content_dict[sender_random_id] = output_content
    # Delete the test output content sent by the assistors
    # We can delete the test message output when we have already retrieved it
    test_message_output.delete_test_message_output_document(test_id=test_id)

    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output done'), user_id, train_id, test_id)
    log(generate_msg('---- unread test output done\n'), user_id, train_id, test_id)

    response = {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
    }
    return jsonify(response)  