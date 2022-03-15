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
from Items.main.utils import log, generate_msg, obtain_user_id

@main.route('/users/<int:id>/match_id_file/', methods=['POST'])
@token_auth.login_required
def get_user_match_id(id):

    user = pyMongo.db.User.find_one({'user_id': id})
    if g.current_user != user:
        return error_response(403)

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data.get('task_id')

    user_id = obtain_user_id()

    log(generate_msg('---- unread match id begins'), user_id, task_id)
    log(generate_msg('3.1:', 'get_user_match_id begins'), user_id, task_id)

    # check if the current client is the sponsor
    isSponsor = False
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    if train_match_document['sponsor_information']['sponsor_id'] == user_id:
        isSponsor = True 

    data = {}
    match_id_file_list = []
    assistor_random_id_list = []
    if isSponsor:
        for assistor_id in train_match_document['assistor_information']:
            match_id_file_id = train_match_document['assistor_information'][assistor_id]['match_id_file_id']
            train_match_file_document = pyMongo.db.Train_Match_File.find_one({'match_id_file_id': match_id_file_id})
            match_id_file = train_match_file_document['match_id_file_content']
            match_id_file_list.append(match_id_file)

            assistor_random_id = train_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
            assistor_random_id_list.append(assistor_random_id)

        data = {
            'match_id_file_list': match_id_file_list,
            'assistor_random_id_list': assistor_random_id_list
        }
        log(generate_msg('3.2:', 'get_user_match_id done'), user_id, task_id)

    else:
        match_id_file_id = train_match_document['assistor_information'][assistor_id]['match_id_file_id']
        train_match_file_document = pyMongo.db.Train_Match_File.find_one({'match_id_file_id': match_id_file_id})
        match_id_file = train_match_file_document['match_id_file_content']
        match_id_file_list.append(match_id_file)

        assistor_random_id = train_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
        assistor_random_id_list.append(assistor_random_id)

        data = {
            'match_id_file_list': match_id_file_list,
            'sponsor_random_id_list': assistor_random_id_list,
        }

        log(generate_msg('3.2:', 'get_user_match_id done'), user_id, task_id)
        log(generate_msg('---- unread match id done\n'), user_id, task_id)
    
    return jsonify(data)


@main.route('/users/<int:id>/test_match_id_file/', methods=['POST'])
@token_auth.login_required
def get_user_test_match_id(id):

    user = pyMongo.db.User.find_one({'user_id': id})
    if g.current_user != user:
        return error_response(403)

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    task_id = data.get('task_id')
    test_id = data.get('test_id')

    user_id = obtain_user_id()

    log(generate_msg('---- unread test match id begins'), user_id, task_id, test_id)
    log(generate_msg('Test 3.1:', 'get_user_test_match_id begins'), user_id, task_id, test_id)

    # check if the current client is the sponsor
    isSponsor = False
    test_match_document = pyMongo.db.Test_Match.find_one({'test_id': test_id})
    if test_match_document['sponsor_information']['sponsor_id'] == user_id:
        isSponsor = True 

    data = {}
    match_id_file_list = []
    assistor_random_id_list = []
    if isSponsor:
        for assistor_id in test_match_document['assistor_information']:
            match_id_file_id = test_match_document['assistor_information'][assistor_id]['match_id_file_id']
            test_match_file_document = pyMongo.db.Test_Match_File.find_one({'match_id_file_id': match_id_file_id})
            match_id_file = test_match_file_document['match_id_file_content']
            match_id_file_list.append(match_id_file)

            assistor_random_id = test_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
            assistor_random_id_list.append(assistor_random_id)

        data = {
            'match_id_file_list': match_id_file_list, 
            'assistor_random_id_list': assistor_random_id_list,
        }

        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test match id done\n'), user_id, task_id, test_id)
    else:
        match_id_file_id = test_match_document['assistor_information'][assistor_id]['match_id_file_id']
        test_match_file_document = pyMongo.db.Train_Match_File.find_one({'match_id_file_id': match_id_file_id})
        match_id_file = test_match_file_document['match_id_file_content']
        match_id_file_list.append(match_id_file)

        assistor_random_id = test_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
        assistor_random_id_list.append(assistor_random_id)

        data = {
            'match_id_file_list': match_id_file_list,
            'sponsor_random_id_list': assistor_random_id_list,
        }

        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
    return jsonify(data)

@main.route('/send_situation/', methods=['POST'])
@token_auth.login_required
def send_situation():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'residual_list' not in data or not data.get('residual_list'):
        return bad_request('residual_list is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'assistor_random_id_list' not in data or not data.get('assistor_random_id_list'):
        return bad_request('assistor_random_id_list is required.')

    # get data from transferred message
    residual_list = data.get('residual_list')
    print('residual length', len(residual_list))
    task_id = data.get('task_id')
    assistor_random_id_list = data.get('assistor_random_id_list')

    user_id = obtain_user_id()

    # get recent round
    cur_rounds_num = None
    train_message_document = pyMongo.db.Train_Message.find_one({'task_id': task_id})
    # if train_message_document is None, it means it is the first round of this train_task
    if train_message_document is None:
        cur_rounds_num = 1
    else:
        cur_rounds_num = train_message_document['cur_rounds_num'] + 1

    if cur_rounds_num == 1:
        log(generate_msg('3.3:', 'sponsor send_situation begins'), user_id, task_id)
    elif cur_rounds_num > 1:
        log(generate_msg('5.3:', 'sponsor send_situation begins'), user_id, task_id)

    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    sponsor_terminate_id_dict = train_match_document['sponsor_terminate_id_dict']
    assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
    sponsor_id = train_match_document['sponsor_information']['sponsor_id']
    if sponsor_id in sponsor_terminate_id_dict:
        return jsonify({"message": "sponsor ends train task"})

    rounds_key = {}
    assistor_id_list = []
    for i in range(len(residual_list)):
        assistor_random_id = assistor_random_id_list[i]
        residual = residual_list[i]

        assistor_id = train_match_document['asssistor_random_id_mapping'][assistor_random_id]
        if assistor_id in assistor_terminate_id_dict:
            continue
        
        assistor_id_list.append(assistor_id)
        sponsor_random_id = train_match_document['sponsor_information'][sponsor_id]['sponsor_id_to_random_id']

        situation_id = obtain_unique_id()
        rounds_key[assistor_id] = {
            'situation_id': situation_id,
        }

        train_message_situation_document = {
            'situation_id': situation_id,
            'sender_id': sponsor_id,
            'sender_random_id': sponsor_random_id,
            'recipient_id': assistor_id,
            'situation_content': residual
        }
        pyMongo.db.Train_Message_Situation.insert_one(train_message_situation_document)

    # sponsor also sends information to itself to trigger next stage
    situation_id = obtain_unique_id()
    rounds_key[sponsor_id] = {
        'situation_id': situation_id
    }

    train_message_situation_document = {
        'situation_id': situation_id,
        'sender_id': sponsor_id,
        'sender_random_id': sponsor_random_id,
        'recipient_id': sponsor_id,
        'situation_content': None
    }
    pyMongo.db.Train_Message_Situation.insert_one(train_message_situation_document)

    if cur_rounds_num == 1:
        train_message_document = {
            'task_id': task_id,
            'cur_rounds_num': cur_rounds_num,
            'assistor_situation_done_dict': {},
            'rounds_' + str(cur_rounds_num): {
                'situation_dict': rounds_key,
                'output_dict': {},
            },
        }
        pyMongo.db.Train_Message.insert_one(train_message_document)
    elif cur_rounds_num > 1:
        pyMongo.db.Train_Message.update_one({'task_id': task_id}, {'$set':{'rounds_' + str(cur_rounds_num).situation_dict: rounds_key}})

    for assistor_id in assistor_id_list:
        user.add_notification('unread situation', user.new_situation())

    if cur_rounds_num == 1:
        log(generate_msg('3.4:"', 'sponsor adds unread situation to assistors done'), user_id, task_id)
    elif cur_rounds_num > 1:
        log(generate_msg('5.4:"', 'sponsor adds unread situation to assistors done'), user_id, task_id)
    
    # sponsor
    user.add_notification('unread situation', user.new_situation())

    if cur_rounds_num == 0:
        log(generate_msg('3.5:"', 'sponsor add unread situation to sponsor done'), g.current_user.id, task_id)
        log(generate_msg('------------------------ unread situation done\n'), g.current_user.id, task_id)
    else:
        log(generate_msg('5.5:"', 'sponsor add unread situation to sponsor done'), g.current_user.id, task_id)
        log(generate_msg('------------------------ unread output done\n'), g.current_user.id, task_id)

    return jsonify({"message": "send situation successfully!"})



@main.route('/send_test_output/', methods=['POST'])
@token_auth.login_required
def send_test_output():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')

    output = data.get('output')
    test_id = data.get('test_id')
    task_id = data.get('task_id')

    user_id = obtain_user_id()

    log(generate_msg('Test 3.3:"', 'assistor send_test_output start'), g.current_user.id, task_id, test_id)

    find_sponsor_query = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").first()
    sponsor = find_sponsor_query.sponsor_id

    # extract sponsor_id
    queries = Matched.query.filter(Matched.assistor_id_pair != sponsor, Matched.test_id == test_id, Matched.test_indicator == "test", Matched.Terminate == "false").all()
    assistor_num = len(queries)

    current_user_test_situation = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
    if current_user_test_situation.Terminate == "false":
        user = User.query.get_or_404(g.current_user.id)
        task_id = queries[0].task_id

        message = Message()
        message.from_dict(data)
        message.sender_id = g.current_user.id
        message.assistor_id = queries[0].sponsor_id
        message.task_id = task_id

        # Store the output
        message.output = json.dumps(output)
        message.test_indicator = "test"
        message.test_id = test_id

        for i in range(len(queries)):
            if int(queries[i].assistor_id_pair) == g.current_user.id:
                print("----------queries[i].assistor_random_id_pair", queries[i].assistor_random_id_pair)
                print("----------queries[i].assistor_id_pair", queries[i].assistor_id_pair)
                print("----------queries[i].sponsor_id", queries[i].sponsor_id)
                print("----------queries[i].sponsor_random_id", queries[i].sponsor_random_id)
                print("----------queries[i].sponsor_random_id", queries[i].test_id, queries[i].task_id)
                # print("----------queries[i].output", queries[i].output)
                message.sender_random_id = queries[i].assistor_random_id_pair

        db.session.add(message)
        db.session.commit()
   
    all_cur_round_messages = Message.query.filter(Message.assistor_id == queries[0].sponsor_id, Message.test_id == test_id, Message.test_indicator == "test").all()

    output_upload = 0
    for row in all_cur_round_messages:
        print("row(((((((((((((((((((((((-----------------------------------------)))))))))))))))))))))))", row)
        if row.output:
            output_upload += 1

        if output_upload == assistor_num:
            log(generate_msg('Test 3.4:"', 'assistor uploads all test output'), g.current_user.id, task_id, test_id)
            user = User.query.get_or_404(queries[0].sponsor_id)

            # query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
            # if query_of_task.Terminate == 'true':
            #     continue
            # send message notification to the sponsor when all assistor upload the output
            print("-----------------send test output", g.current_user.id)
            user.add_notification('unread test output', user.new_test_output())
            db.session.commit()

    dict = {"send_test_output": "send test output successfully"}
    log(generate_msg('Test 3.5:"', 'assistor send_test_output done'), g.current_user.id, task_id, test_id)
    log(generate_msg('----------------------- unread_test_match_id done\n'), g.current_user.id, task_id, test_id)
    
    return jsonify(dict)

    