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

@main.route('/update_match_id_notification/', methods=['POST'])
@token_auth.login_required
def update_match_id_notification():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'sender_random_id_list' not in data or not data.get('sender_random_id_list'):
        return bad_request('sender_random_id_list is required.')
    if 'task_id_list' not in data or not data.get('task_id_list'):
        return bad_request('task_id_list is required.')

    task_id_list = data.get('task_id_list')

    check_dict = {}
    lastest_time = float("-inf")
    for i in range(len(task_id_list)):
        # check if the current client is the sponsor
        isSponsor = False
        query = Matched.query.filter(Matched.task_id == task_id_list[i]).first()
        if query.sponsor_id == g.current_user.id:
            isSponsor = True

        # Update the Notification
        user = User.query.get_or_404(g.current_user.id)
        last_matched_file_read_time = user.last_matched_file_read_time or datetime(1900, 1, 1)

        if isSponsor:
            record = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id_list[i]).order_by(Matched.match_id_timestamp.desc()).first()
        else:
            record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id_list[i]).all()

        # get the latest output timestamp
        if record['match_id_timestamp'] > lastest_time:
            lastest_time = record['match_id_timestamp']
        
        if isSponsor:
            check_dict[task_id_list[i]] = 1
        else:
            check_dict[task_id_list[i]] = 0

    if lastest_time > last_matched_file_read_time:
        user.last_matched_file_read_time = lastest_time

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread match id', user.new_match_id()) 
        db.session.commit()

    dict = {"check_sponsor": check_dict}
    
    response = jsonify(dict)

    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = None
    # response.headers['Location'] = url_for('main.get_matched', id=matched.id)
    
    return response

@main.route('/users/<int:id>/match_id_file/', methods=['GET'])
@token_auth.login_required
def get_user_match_id(id):

    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    task_id = request.args.get('task_id', 0, type=int)

    # check if the current client is the sponsor
    isSponsor = False
    query = Matched.query.filter(Matched.task_id == task_id).first()
    if query.sponsor_id == g.current_user.id:
        isSponsor = True

    data = {}
    if isSponsor:
        query = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id).all()

        data = {
            'match_id_file': [item for item in query.Matched_id_file],
            'recipient_random_id_pair': [item for item in query.recipient_random_id_pair]
        }
    else:
        query = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id).all()

        data = {
            'match_id_file': [item for item in query.Matched_id_file],
            'sponsor_random_id': [item for item in query.sponsor_random_id]
        }

    return jsonify(data)