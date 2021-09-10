# -*- coding: utf-8 -*-
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



@main.route('/users/<int:id>/output/', methods=['POST'])
@token_auth.login_required
def get_user_output(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'rounds' not in data:
        return bad_request('rounds is required.')

    task_id = data.get('task_id')
    rounds = data.get('rounds')

    # only call this function with id that is sponsor
    query = Matched.query.filter(Matched.task_id == task_id).first()
    if int(query.sponsor_id) != id:
        return error_response(403)

    # check if the caller and the id is the same
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    data = {}
    query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id, Message.rounds == rounds, Message.test_indicator == "train").order_by(Message.rounds.desc()).all()

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

    return jsonify(data)  

@main.route('/test_output/', methods=['POST'])
@token_auth.login_required
def get_user_test_output():
    print("##############################")
    data = request.get_json()
    print("##############################", data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    test_id = data.get('test_id')
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

    return jsonify(data)  