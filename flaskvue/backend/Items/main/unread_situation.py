# -*- coding: utf-8 -*-
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from bson import ObjectId

from Items.main.apollo_utils import log, generate_msg

# from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main
# from Items.models import User, Message, Matched
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
    user = pyMongo.db.User.find_one({'_id': ObjectId(id)})
    if g.current_user != user:
        return error_response(403)

    log(generate_msg('-------------------- unread sitaution begins'), g.current_user.id, task_id)
    log(generate_msg('4.1:', 'assistor get_user_situation from sponsor'), g.current_user.id, task_id)

    user_object_id = g.current_user['_id']
    user_id = str(user_object_id)

    data = {}
    rounds_key = 'rounds_' + str(rounds)
    train_message_document = pyMongo.db.Train_Message.find_one({'task_id': task_id})
    sender_random_id = train_message_document[rounds_key][user_id]['sender_random_id']
    situation_id = train_message_document[rounds_key][user_id]['situation']

    train_message_situation_document = pyMongo.db.Train_Message_Situation.find_one({'situation_id': situation_id})
    situation_file = train_message_situation_document['situation_content']

    data = {
        'situation': situation_file,
        'sender_random_id': sender_random_id
    }

    log(generate_msg('4.2:', 'assistor get_user_situation done'), g.current_user.id, task_id)

    return jsonify(data)  

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

    log(generate_msg('4.3:"', 'assistor send_output start'), g.current_user.id, task_id)

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
        if row.output:
            output_upload += 1

        if output_upload == assistor_num:
            log(generate_msg('4.4:"', 'assistor uploads all output'), g.current_user.id, task_id)
            user = User.query.get_or_404(queries[0].sponsor_id)
            query_of_task = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
            if query_of_task.Terminate == 'true':
                continue

            # send message notification to the sponsor when all assistor upload the output
            print("-----------------sendoutput", g.current_user.id)
            user.add_notification('unread output', user.new_output())
            db.session.commit()

    log(generate_msg('4.5:"', 'assistor send_output done'), g.current_user.id, task_id)
    log(generate_msg('----------------------- unread situation done\n'), g.current_user.id, task_id)

    return jsonify({"send_output": "send output successfully"})


    # response = jsonify({"send_output": "Assistors havent upload all outputs"})
    # return response

    