# -*- coding: utf-8 -*-
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


# @main.route('/update_situation_notification/', methods=['POST'])
# @token_auth.login_required
# def update_situation_notification():

#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'sender_random_id_list' not in data or not data.get('sender_random_id_list'):
#         return bad_request('sender_random_id_list is required.')
#     if 'task_id_list' not in data or not data.get('task_id_list'):
#         return bad_request('task_id_list is required.')

#     task_id_list = data.get('task_id_list')

#     check_dict = {}
#     rounds_dict = {}
#     lastest_time = datetime(1900, 1, 1)

#     for i in range(len(task_id_list)):
#         # check if the current client is the sponsor
#         isSponsor = False
#         query = Matched.query.filter(Matched.task_id == task_id_list[i]).first()
#         if query:
#             if int(query.sponsor_id) == g.current_user.id:
#                 isSponsor = True

#             record = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id_list[i]).order_by(Message.situation_timestamp.desc()).first()
#             # record = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id_list[i]).all()
#             # for i in record:
#             #     print()
#             cur_rounds = record.rounds
            
#             # get the latest output timestamp
#             if record.situation_timestamp > lastest_time:
#                 lastest_time = record.situation_timestamp
            
#             if isSponsor:
#                 check_dict[task_id_list[i]] = 1
#             else:
#                 check_dict[task_id_list[i]] = 0
            
#             rounds_dict[task_id_list[i]] = cur_rounds

#     # Update the Notification
#     user = User.query.get_or_404(g.current_user.id)
#     last_situation_read_time = user.last_situation_read_time or datetime(1900, 1, 1)
#     if lastest_time > last_situation_read_time:
#         user.last_situation_read_time = lastest_time

#         # submit to database
#         db.session.commit()
        
#         # Updata Notification
#         user.add_notification('unread situation', user.new_situation()) 
#         db.session.commit()

#     dict = {"check_sponsor": check_dict, "rounds": rounds_dict}
    
#     response = jsonify(dict)
    
#     return response


@main.route('/users/<int:id>/situation_file/', methods=['POST'])
@token_auth.login_required
def get_user_situation(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'rounds' not in data:
        return bad_request('rounds is required.')

    task_id = data.get('task_id')
    rounds = data.get('rounds')

    # check if the caller and the id is the same
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    data = {}
    query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train").order_by(Message.rounds.desc()).all()

    situation_file = None
    sender_random_id = None
    for row in query:
        if row.situation:
            situation_file = row.situation
            sender_random_id = row.sender_random_id

    data = {
        'situation': situation_file,
        'sender_random_id': sender_random_id
    }

    return jsonify(data)  


@main.route('/send_output/', methods=['POST'])
@token_auth.login_required
def send_output():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')
    # if 'rounds' not in data:
    #     return bad_request('rounds is required.')  
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    output = data.get('output')
    # rounds = data.get('rounds')
    task_id = data.get('task_id')

    rounds = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first().rounds

    # extract sponsor_id
    queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").all()
    assistor_num = len(queries) - 1

    message = Message()
    message.from_dict(data)
    message.sender_id = g.current_user.id
    message.assistor_id = queries[0].sponsor_id
    message.task_id = task_id
    message.rounds = rounds

    # Store the output
    message.output = json.dumps(output)
    message.test_indicator = "train"

    for i in range(len(queries)):
      if int(queries[i].assistor_id_pair) == g.current_user.id:
        print("----------queries[i].assistor_random_id_pair", queries[i].assistor_random_id_pair)
        print("----------queries[i].assistor_id_pair", queries[i].assistor_id_pair)
        print("----------queries[i].sponsor_id", queries[i].sponsor_id)
        print("----------queries[i].sponsor_random_id", queries[i].sponsor_random_id)
        # print("----------queries[i].output", queries[i].output)
        message.sender_random_id = queries[i].assistor_random_id_pair

    db.session.add(message)
    db.session.commit()

    all_cur_round_messages = Message.query.filter(Message.assistor_id == queries[0].sponsor_id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train").all()
    output_upload = 0
    for row in all_cur_round_messages:
        print("row", row)
        if row.output:
            output_upload += 1

        if output_upload == assistor_num:
            user = User.query.get_or_404(queries[0].sponsor_id)
            # send message notification to the sponsor when all assistor upload the output
            print("-----------------sendoutput", g.current_user.id)
            user.add_notification('unread output', user.new_output())
            db.session.commit()

    dict = {"send_output": "send output successfully"}
    response = jsonify(dict)
    
    return response

    