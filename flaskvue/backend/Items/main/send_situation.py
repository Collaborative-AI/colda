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
    if 'situation' not in data or not data.get('situation'):
        return bad_request('situation is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    # json
    situation = data.get('situation')
    task_id = data.get('task_id')

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)
    query_of_task = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").all()
    sender_random_id = query_of_task[0].sponsor_random_id

    # should be [4,5,6], including sponsor itself
    all_recipient_id = []
    for i in query_of_task:
        all_recipient_id.append(i.recipient_id_pair)

    # check message
    cur_round = 0
    query = Message.query.filter(Message.sender_id == g.current_user.id, Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first()
    if query is not None:
        cur_round = query.rounds + 1
        
    print("all_recipient_id+++++++++++++++++++++++", all_recipient_id)
    # print("all_recipient_id", all_recipient_id)
    for recipient_id in all_recipient_id:
        user = User.query.get_or_404(recipient_id)

        message = Message()
        message.from_dict(data)

        message.sender_id = g.current_user.id
        message.recipient_id = user.id
        message.task_id = task_id
        message.rounds = cur_round
        
        # Store the situation
        message.situation = json.dumps(situation)
        message.sender_random_id = sender_random_id
        
        message.test_indicator = "train"

        db.session.add(message)
        db.session.commit()
        # send message notification to the recipient
        user.add_notification('unread situation', user.new_situation())
        db.session.commit()

    # return response
    dict = {"message": "send situation successfully!"}
    response = jsonify(dict)

    return response
