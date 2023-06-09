from __future__ import annotations

import sys
# -*- coding: utf-8 -*-
from flask import request
from flask.json import jsonify
# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main_flow import main_flow_bp
# from Items.models import User, Message, Matched
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import obtain_user_id_from_token, obtain_unique_id
from Items.utils import verify_token_user_id_and_function_caller_id
from Items.utils import log, generate_msg
from Items.utils.api import (
    check_if_data_is_valid,
    input_data_err_msg
)

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_message, train_message_situation, train_message_output

@main_flow_bp.route('/get_situation_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_situation_content(id):

    """
    Assistor obtains the situation file uploaded by sponsor to train the model locally.

    Parameters:
       train_id - String. The id of current train task
       rounds - Integer. The number of current round
       
    Returns:
        {
            'situation_content': situation_content,
            'sender_random_id': sender_random_id
        }

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')

    expected_data = {
        'train_id': str,
        'rounds': int,
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
    rounds = data.get('rounds')

    user_id = obtain_user_id_from_token()

    log(generate_msg('---- unread sitaution begins'), user_id, train_id)
    log(generate_msg('4.1:', 'assistor get_user_situation from sponsor'), user_id, train_id)

    # obtain some information from Train_Message table using specific key, such as rounds_1, rounds_2
    train_message_document = train_message.search_train_message_document(train_id=train_id)
    situation_id = train_message_document[f'rounds_{rounds}']['situation_dict'][user_id]['situation_id']

    # obtain situation file from Train_Message_Situation table
    train_message_situation_document = train_message_situation.search_train_message_situation_document(situation_id=situation_id)
    sender_random_id = train_message_situation_document['sender_random_id']
    if train_message_situation_document['is_large_file'] == False:
        situation_content = train_message_situation_document['situation_content']
    elif train_message_situation_document['is_large_file'] == True:
        gridfs_file_id = train_message_situation_document['situation_content']
        situation_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_file_id)

    log(generate_msg('4.2:', 'assistor get_user_situation done'), user_id, train_id)

    response = {
        'situation_content': situation_content,
        'sender_random_id': sender_random_id
    }
    return jsonify(response)  

@main_flow_bp.route('/send_output/<string:id>', methods=['POST'])
@token_auth.login_required
def send_output(id):
    """
    1. Assistors send outputs in this function to sponsor. Only when all the assistors in current train task upload
    their outputs, server will send sponsor the unread_output notifications.
    2. Only assistor will enter this function
    
    Parameters:
        train_id - String. The id of current train task
        output_content - List. 
       
    Returns:
        {"send_output": "send output successfully"}

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name), 'You must post JSON data')
    
    expected_data = {
        'train_id': str,
        'output_content': list
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

    output_content = data.get('output_content')
    train_id = data.get('train_id')
    assistor_id = user_id

    log(generate_msg('4.3:"', 'assistor send_output start'), user_id, train_id)

    # get sponsor id    
    train_match_document = train_match.search_train_match_document(train_id=train_id)
    total_assistor_num = train_match_document['total_assistor_num']
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    assistor_random_id = train_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']

    train_message_document = train_message.search_train_message_document(train_id=train_id)
    cur_rounds_num = train_message_document['cur_rounds_num']

    output_id = obtain_unique_id()
    pyMongo.db.Train_Message.update_one({'train_id': train_id}, {'$set':
        {f'rounds_{cur_rounds_num}.output_dict.{assistor_id}.output_id': output_id}
    })
    train_message_output.create_train_message_output_document(
        output_id=output_id, 
        train_id=train_id, 
        sender_id=assistor_id,
        sender_random_id=assistor_random_id, 
        recipient_id=sponsor_id,
        output_content=output_content
    )

    # check how many assistors are still participate in this train task
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)

    # check how many assistors have uploaded their output 
    # if the number of output surpasses the ramin_assistor_num, we can send notifications
    train_message_document = train_message.search_train_message_document(train_id=train_id)
    output_dict = train_message_document['rounds_' + str(cur_rounds_num)]['output_dict']
    if len(output_dict) >= remain_assistor_num:
        # Delete the situation content sent by the sponsor
        # When we need to update unread_output, it means the unread_situation stage is finished 
        train_message_situation.delete_train_message_situation_document(train_id=train_id)
        mongoDB.update_notification_document(
            user_id=sponsor_id, 
            notification_name='unread_output', 
            train_id=train_id, 
            sender_random_id=assistor_random_id, 
            role='sponsor', 
            cur_rounds_num=cur_rounds_num, 
            test_indicator='train'
        )

        log(generate_msg('4.5:"', 'assistor uploads all output'), user_id, train_id)
    else:
        log(generate_msg('4.5:"', 'assistor send_output done'), user_id, train_id)
    
    log(generate_msg('---- unread situation done\n'), user_id, train_id)

    response = {
        "send_output": "send output successfully"
    }
    return jsonify(response)


    