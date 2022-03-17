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
from Items.main.mongoDB import train_mongoDB
from Items.main.utils import log, generate_msg, obtain_user_id_from_token, obtain_unique_id
from Items.main.utils import verify_token_user_id_and_function_caller_id

@main.route('/get_identifier_content/<string:id>', methods=['POST'])
@token_auth.login_required
def get_identifier_content(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    user = pyMongo.db.User.find_one({'user_id': id})
    if user is None:
        return error_response(403)

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data.get('task_id')

    log(generate_msg('---- unread match id begins'), user_id, task_id)
    log(generate_msg('3.1:', 'get_user_match_id begins'), user_id, task_id)

    # check if the current client is the sponsor
    isSponsor = False
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    if train_match_document['sponsor_information']['sponsor_id'] == user_id:
        isSponsor = True 

    response = {}

    if isSponsor:
        assistor_random_id_to_identifier_content_dict = {}
        for assistor_id in train_match_document['assistor_information']:
            identifier_id = train_match_document['assistor_information'][assistor_id]['identifier_id']
            assistor_random_id = train_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']

            train_match_file_document = pyMongo.db.Train_Match_File.find_one({'identifier_id': identifier_id})
            identifier_content = train_match_file_document['identifier_content']

            assistor_random_id_to_identifier_content_dict[assistor_random_id] = identifier_content

        response = {
            'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
        }
        log(generate_msg('3.2:', 'get_user_match_id done'), user_id, task_id)

    else:
        sponsor_random_id_to_identifier_content_dict = {}
        identifier_id = train_match_document['assistor_information'][assistor_id]['identifier_id']
        sponsor_id = train_match_document['sponsor_information']['sponsor_id']
        sponsor_random_id = train_match_document['sponsor_information'][sponsor_id]['sponsor_id_to_random_id']

        train_match_file_document = pyMongo.db.Train_Match_File.find_one({'identifier_id': identifier_id})
        identifier_content = train_match_file_document['identifier_content']

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

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data.get('task_id')
    test_id = data.get('test_id')

    user_id = obtain_user_id_from_token()

    log(generate_msg('---- unread test match id begins'), user_id, task_id, test_id)
    log(generate_msg('Test 3.1:', 'get_user_test_match_id begins'), user_id, task_id, test_id)

    # check if the current client is the sponsor
    isSponsor = False
    test_match_document = pyMongo.db.Test_Match.find_one({'test_id': test_id})
    if test_match_document['sponsor_information']['sponsor_id'] == user_id:
        isSponsor = True 

    data = {}
    identifier_content_list = []
    assistor_random_id_list = []
    if isSponsor:
        for assistor_id in test_match_document['assistor_information']:
            identifier_id = test_match_document['assistor_information'][assistor_id]['identifier_id']
            test_match_file_document = pyMongo.db.Test_Match_File.find_one({'identifier_id': identifier_id})
            identifier_content = test_match_file_document['identifier_content']
            identifier_content_list.append(identifier_content)

            assistor_random_id = test_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
            assistor_random_id_list.append(assistor_random_id)

        data = {
            'identifier_content_list': identifier_content_list, 
            'assistor_random_id_list': assistor_random_id_list,
        }

        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
        log(generate_msg('---- unread test match id done\n'), user_id, task_id, test_id)
    else:
        identifier_id = test_match_document['assistor_information'][assistor_id]['identifier_id']
        test_match_file_document = pyMongo.db.Train_Match_File.find_one({'identifier_id': identifier_id})
        identifier_content = test_match_file_document['identifier_content']
        identifier_content_list.append(identifier_content)

        assistor_random_id = test_match_document['assistor_information'][assistor_id]['assistor_id_to_random_id']
        assistor_random_id_list.append(assistor_random_id)

        data = {
            'identifier_content_list': identifier_content_list,
            'sponsor_random_id_list': assistor_random_id_list,
        }

        log(generate_msg('Test 3.2:', 'get_user_test_match_id done'), user_id, task_id, test_id)
    return jsonify(data)

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
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
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
            'rounds_' + str(cur_rounds_num).situation_dict: situation_dict
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

    return jsonify({"message": "send situation successfully!"})


@main.route('/send_test_output/<string:id>', methods=['POST'])
@token_auth.login_required
def send_test_output(id):

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')

    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    output = data.get('output')
    test_id = data.get('test_id')
    task_id = data.get('task_id')

    user_id = obtain_user_id_from_token()

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

    