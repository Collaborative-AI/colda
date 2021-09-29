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

@main.route('/Sponsor_situation_training_done/', methods=['POST'])
@token_auth.login_required
def Sponsor_situation_training_done():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data.get('task_id')

    rounds = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first().rounds

    return_val = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train", Message.output == None).update({"Sponsor_situation_training_done": "done"})
    db.session.commit()

    a = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train", Message.output == None).all()
    for zz in a:
        print(zz.Sponsor_situation_training_done)
    
    queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != g.current_user.id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
    assistor_num = len(queries)

    all_cur_round_messages = Message.query.filter(Message.assistor_id == queries[0].sponsor_id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train").all()
    output_upload = 0
    for row in all_cur_round_messages:
        print("row", row)
        if row.output:
            output_upload += 1

        if output_upload == assistor_num:
            user = User.query.get_or_404(queries[0].sponsor_id)
            query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").all()
            if query_of_task[0].Terminate == 'true':
                continue
            # send message notification to the sponsor when all assistor upload the output
            print("-----------------sendoutput", g.current_user.id)
            user.add_notification('unread output', user.new_output())
            db.session.commit()

            response = jsonify({"Sponsor_situation_training_done": "Send unread output"})
            return response
    
    response = jsonify({"Sponsor_situation_training_done": "Assistors havent upload all output"})
    return response

@main.route('/send_output/', methods=['POST'])
@token_auth.login_required
def send_output():

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    output = data.get('output')
    task_id = data.get('task_id')

    # get sponsor id
    query = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").all()
    sponsor_id = query[0].sponsor_id

    # check how many assistors in this train task are still running, not terminate
    queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != sponsor_id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
    assistor_num = len(queries)

    # check the most recent round
    rounds = 0
    round_query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first()
    if round_query:
        rounds = round_query.rounds
    

    query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
    # check if current assistor is still running. If yes => add new message, else: not add anything
    if query_of_task.Terminate == 'false':
        message = Message()
        message.from_dict(data)
        message.sender_id = g.current_user.id
        message.assistor_id = queries[0].sponsor_id
        message.task_id = task_id
        message.rounds = rounds

        # Store the output
        message.output = json.dumps(output)
        message.test_indicator = "train"

        # Sponsor_situation_training_done

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

    # check if sponsor finish training
    # check_sponsor_training_done = Message.query.filter(Message.assistor_id == queries[0].sponsor_id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train", Message.Sponsor_situation_training_done == "done").all()
    # if not check_sponsor_training_done:
    #     response = jsonify({"send_output": "Sponsor doesnt finish training"})
    #     return response

    # check how many message we have of current round
    # if the number of message rows containing output reaches the assistor_num, send "unread output" to sponsor
    # if we delete the round R, then assistor_num == 0. It will check the message R-1, which would not match the assistor_num. Even it matches, we will check the Terminate
    all_cur_round_messages = Message.query.filter(Message.assistor_id == queries[0].sponsor_id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train").all()
    output_upload = 0
    for row in all_cur_round_messages:
        print("row", row)
        if row.output:
            print("row.output", row.output)
            output_upload += 1

        if output_upload == assistor_num:
            user = User.query.get_or_404(queries[0].sponsor_id)
            query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
            if query_of_task.Terminate == 'true':
                continue

            # send message notification to the sponsor when all assistor upload the output
            print("-----------------sendoutput", g.current_user.id)
            user.add_notification('unread output', user.new_output())
            db.session.commit()

    response = jsonify({"send_output": "send output successfully"})
    return response


    # response = jsonify({"send_output": "Assistors havent upload all outputs"})
    # return response

    