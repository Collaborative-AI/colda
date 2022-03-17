# -*- coding: utf-8 -*-
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.mongoDB import train_mongoDB
from Items.main.utils import log, generate_msg

# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main import main
# from Items.models import User, Notification, Matched, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id

@main.route('/get_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_output_content(id):

    """
    Sponsor gets outputs of assistors. Only sponsor enters this function.

    Parameters:
        task_id - String. The id of task
        rounds - String. The round number

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
    if 'rounds' not in data:
        return bad_request('rounds is required.')

    task_id = data.get('task_id')
    rounds = data.get('rounds')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    sponsor_id = user_id

    log(generate_msg('---- unread situation begins'), user_id, task_id)
    log(generate_msg('---- unread situation done (no function pass server)\n'), user_id, task_id)
    log(generate_msg('---- unread output begins'), user_id, task_id)
    log(generate_msg('5.1:"', 'sponsor get_user_output start'), user_id, task_id)

    train_message_document = train_mongoDB.search_train_message_document(task_id=task_id)
    output_dict = train_message_document['rounds_' + str(rounds)]['output_dict']

    assistor_random_id_to_output_content_dict = {}
    for assistor_id in output_dict:
        output_id = output_dict[assistor_id]
        train_message_output_document = train_mongoDB.search_train_message_output_document(output_id=output_id)

        output_content = train_message_output_document['output_content']
        sender_random_id = train_message_output_document['sender_random_id']

        assistor_random_id_to_output_content_dict[sender_random_id] = output_content

    log(generate_msg('5.2:"', 'sponsor get_user_output done'), user_id, task_id)

    return jsonify({
                'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
            })  


@main.route('/get_test_output_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_output_content(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    test_id = data.get('test_id')
    task_id = data.get('task_id')
    
    user_id = obtain_user_id_from_token()

    log(generate_msg('---- unread test output begins'), g.current_user.id, task_id, test_id)
    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output start'), g.current_user.id, task_id, test_id)

    user = User.query.get_or_404(g.current_user.id)
    # only call this function with id that is sponsor
    query = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").first()
    if int(query.sponsor_id) != g.current_user.id:
        return error_response(403)

    data = {}
    query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.test_id == test_id, Message.test_indicator == "test").all()

    output_files = []
    sender_random_ids = []
    for row in query:
        if row.output:
            output_files.append(row.output)
            sender_random_ids.append(row.sender_random_id)

    data = {
        'output': output_files,
        'sender_random_ids_list': sender_random_ids
    }

    log(generate_msg('Test 5.1:', 'sponsor get_user_test_output done'), g.current_user.id, task_id, test_id)
    log(generate_msg('--------------------unread test output done\n'), g.current_user.id, task_id, test_id)


    return jsonify(data)  