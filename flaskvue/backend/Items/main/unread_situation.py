# -*- coding: utf-8 -*-
import json
import uuid

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from bson import ObjectId

from Items.main.utils import log, generate_msg

# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main
# from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import obtain_user_object_id_and_user_id

@main.route('/users/<int:id>/situation_file/', methods=['POST'])
@token_auth.login_required
def get_user_situation(id):

    """
    Assistor obtains the situation file uploaded by sponsor to train the model locally.

    Parameters:
       task_id - String. The id of current train task
       rounds - Integer. The number of current round
       
    Returns:
        {
            'situation': situation_file,
            'sender_random_id': sender_random_id
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

    task_id = data.get('task_id')
    rounds = data.get('rounds')

    user_object_id, user_id = obtain_user_object_id_and_user_id()

    # check if the caller of the function and the id is the same
    user = pyMongo.db.User.find_one({'_id': ObjectId(id)})
    if user_object_id != user['_id']:
        return error_response(403)

    log(generate_msg('---- unread sitaution begins'), user_id, task_id)
    log(generate_msg('4.1:', 'assistor get_user_situation from sponsor'), user_id, task_id)

    # obtain some information from Train_Message table using specific key, such as rounds_1, rounds_2
    rounds_key = 'rounds_' + str(rounds)
    train_message_document = pyMongo.db.Train_Message.find_one({'task_id': task_id})
    sender_random_id = train_message_document[rounds_key][user_id]['sender_random_id']
    situation_id = train_message_document[rounds_key][user_id]['situation']

    # obtain situation file from Train_Message_Situation table
    train_message_situation_document = pyMongo.db.Train_Message_Situation.find_one({'situation_id': situation_id})
    situation_file = train_message_situation_document['situation_content']

    log(generate_msg('4.2:', 'assistor get_user_situation done'), user_id, task_id)

    response = {
        'situation': situation_file,
        'sender_random_id': sender_random_id
    }
    return jsonify(response)  

@main.route('/send_output/', methods=['POST'])
@token_auth.login_required
def send_output():

    """
    Assistors send outputs in this function to sponsor. Only when all the assistors in current train task upload
    their outputs, server will send all the assistors and sponsor the unread_output notifications.

    Parameters:
        task_id - String. The id of current train task
        output - 
       
    Returns:
        {"send_output": "send output successfully"}

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')

    output = data.get('output')
    task_id = data.get('task_id')

    user_object_id, user_id = obtain_user_object_id_and_user_id()
    assistor_id = user_id
    log(generate_msg('4.3:"', 'assistor send_output start'), user_id, task_id)

    # get sponsor id    
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    total_assistor_num = train_match_document['total_assistor_num']
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    assistor_random_id = train_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
    # check how many assistors in this train task are still running, not terminating
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']

    train_message_document = pyMongo.db.Train_Message.find_one({'task_id': task_id})
    cur_rounds_num = train_message_document['cur_rounds_num']
    output_dict = train_message_document['rounds_' + str(cur_rounds_num)]['output_dict']

    output_id = str(uuid.uuid4())
    output_dict[assistor_id] = output_id

    train_message_output_document = {
        'output_id': output_id,
        'sender_id': user_id,
        'sender_random_id': assistor_random_id,
        'recipient_id': sponsor_id,
        'output_content': output,
    }
    pyMongo.db.Train_Message_Output.insert_one(train_message_output_document)

    pyMongo.db.Train_Message.update_one({'task_id': task_id}, {'$set':{'rounds_' + str(cur_rounds_num).output_dict: output_dict}})

    # check how many assistors are still participate in this train task
    remain_assistor_num = total_assistor_num - len(assistor_terminate_id_dict)

    # check how many assistors have uploaded their output 
    # if the number of output surpasses the ramin_assistor_num, we can send notifications
    if len(output_dict) >= remain_assistor_num:
        sponsor.add_notification('unread output', user.new_output())

    log(generate_msg('4.5:"', 'assistor send_output done'), g.current_user.id, task_id)
    log(generate_msg('---- unread situation done\n'), g.current_user.id, task_id)

    return jsonify({"send_output": "send output successfully"})


    