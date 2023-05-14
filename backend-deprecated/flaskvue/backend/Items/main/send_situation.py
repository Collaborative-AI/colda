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

    # json
    residual_list = data.get('residual_list')
    task_id = data.get('task_id')
    assistor_random_id_list = data.get('assistor_random_id_list')

    cur_round = 0
    query = Message.query.filter(Message.sender_id == g.current_user.id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first()
    if query is not None:
        cur_round = query.rounds + 1

    for i in range(len(residual_list)):

        cur_assistor_random_id = assistor_random_id_list[i]
        cur_residual = residual_list[i]
        # Now hardcode
        # testa: id 4(sponsor), testb: id 5(assistor), testc: id 6(assistor)
        query_of_task = Matched.query.filter(Matched.assistor_id_pair != g.current_user.id, Matched.task_id == task_id, Matched.assistor_random_id_pair == cur_assistor_random_id, Matched.test_indicator == "train").all()
        sender_random_id = query_of_task[0].sponsor_random_id
        assistor_id = query_of_task[0].assistor_id_pair

        # # should be [4,5,6], including sponsor itself
        # all_assistor_id = []
        # for i in query_of_task:
        #     all_assistor_id.append(i.assistor_id_pair)

        # check message
        
        print("all_assistor_id+++++++++++++++++++++++", assistor_id)
        # print("all_assistor_id", all_assistor_id)

        user = User.query.get_or_404(assistor_id)

        message = Message()
        message.from_dict(data)
        message.sender_id = g.current_user.id
        message.assistor_id = user.id
        message.task_id = task_id
        message.rounds = cur_round
        message.situation = json.dumps(cur_residual)
        message.sender_random_id = sender_random_id
        message.test_indicator = "train"

        db.session.add(message)
        db.session.commit()
        # send message notification to the assistor
        user.add_notification('unread situation', user.new_situation())
        db.session.commit()

    user = User.query.get_or_404(g.current_user.id)
    message = Message()
    message.from_dict(data)
    message.sender_id = g.current_user.id
    message.assistor_id = g.current_user.id
    message.task_id = task_id
    message.rounds = cur_round
    message.test_indicator = "train"

    db.session.add(message)
    db.session.commit()
    # send message notification to the assistor
    user.add_notification('unread situation', user.new_situation())
    db.session.commit()

    # return response
    dict = {"message": "send situation successfully!"}
    response = jsonify(dict)

    return response