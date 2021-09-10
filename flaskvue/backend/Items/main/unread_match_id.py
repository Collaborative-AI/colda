# -*- coding: utf-8 -*-
import uuid
import json

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.main import main
from Items.models import User, Notification, Matched, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/users/<int:id>/match_id_file/', methods=['POST'])
@token_auth.login_required
def get_user_match_id(id):

    data = request.get_json()
    # print(data)
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    # task_id = request.args.get('task_id', 0, type=int)
    # print("task_id-----------------------", task_id)
    
    task_id = data.get('task_id')

    # check if the current client is the sponsor
    isSponsor = False
    query = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").first()
    if int(query.sponsor_id) == g.current_user.id:
        isSponsor = True

    data = {}
    if isSponsor:
        query = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'assistor_random_id_pair': [item.assistor_random_id_pair for item in query]
        }
    else:
        query = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'sponsor_random_id': [item.sponsor_random_id for item in query]
        }

    return jsonify(data)


@main.route('/users/<int:id>/test_match_id_file/', methods=['POST'])
@token_auth.login_required
def get_user_test_match_id(id):

    data = request.get_json()
    # print(data)
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    # task_id = request.args.get('task_id', 0, type=int)
    # print("task_id-----------------------", task_id)
    test_id = data.get('test_id')

    user = User.query.get_or_404(g.current_user.id)
    # check if the current client is the sponsor
    isSponsor = False
    query = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").first()
    if int(query.sponsor_id) == g.current_user.id:
        isSponsor = True

    data = {}
    if isSponsor:
        query = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'assistor_random_id_pair': [item.assistor_random_id_pair for item in query]
        }
    else:
        query = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'sponsor_random_id': [item.sponsor_random_id for item in query]
        }

    return jsonify(data)

@main.route('/assistor_write_match_index_done/', methods=['POST'])
@token_auth.login_required
def assistor_write_match_index_done():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data.get('task_id')
    user = User.query.get_or_404(g.current_user.id)

    # Update current done situation
    Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == g.current_user.id, Matched.test_indicator == "train").update({"Assistor_matched_written_done": "done"})
    db.session.commit()
    
    query = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").all()
    sponsor_id = query[0].sponsor_id

    assistor_num = len(query) - 1

    cur_assistor_written_done_count = 0
    for row in query:
        if row.Assistor_matched_written_done == "done" and row.assistor_id_pair != sponsor_id:
            cur_assistor_written_done_count += 1
    
    if cur_assistor_written_done_count != assistor_num:
        response = jsonify({"assistor_write_match_index_done": "Assistors dont finish"})
        return response

    Message_query = Message.query.filter(Message.sender_id == sponsor_id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first()
    if not Message_query:
        response = jsonify({"assistor_write_match_index_done": "Situation doesnt update"})
        return response




    if Message_query is not None and cur_assistor_written_done_count == assistor_num:
        for row in query:
            user = User.query.get_or_404(row.assistor_id_pair)
            user.add_notification('unread situation', user.new_situation())
            db.session.commit()

    response = jsonify({"assistor_write_match_index_done": "Send unread situation"})
    return response
    




# @main.route('/get_task_id_max_rounds/', methods=['POST'])
# @token_auth.login_required
# def get_task_id_max_rounds():
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'test_id' not in data or not data.get('test_id'):
#         return bad_request('test_id is required.')
    
#     task_id = data['task_id']

#     query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id,  Message.test_indicator == "train").order_by(Message.rounds.desc()).first()

#     data = {"max_rounds": query.rounds}
#     response = jsonify(data)
    
#     return response


@main.route('/send_test_output/', methods=['POST'])
@token_auth.login_required
def send_test_output():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')

    output = data.get('output')
    test_id = data.get('test_id')
    user = User.query.get_or_404(g.current_user.id)
    # extract sponsor_id
    queries = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").all()
    assistor_num = len(queries) - 1
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
            user = User.query.get_or_404(queries[0].sponsor_id)

            query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
            if query_of_task.Terminate == 'true':
                continue
            # send message notification to the sponsor when all assistor upload the output
            print("-----------------send test output", g.current_user.id)
            user.add_notification('unread test output', user.new_test_output())
            db.session.commit()

    dict = {"send_test_output": "send test output successfully"}
    response = jsonify(dict)
    
    return response

    