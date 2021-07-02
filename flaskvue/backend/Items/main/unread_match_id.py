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
    print("update match_id_notification", task_id_list, type(task_id_list), len(task_id_list), g.current_user.id)

    check_dict = {}
    lastest_time = datetime(1900, 1, 1)
    last_matched_file_read_time = datetime(1900, 1, 1)

    for i in range(len(task_id_list)):
        # check if the current client is the sponsor
        isSponsor = False
        query = Matched.query.filter(Matched.task_id == task_id_list[i]).first()
        
        if query:
            print("match_id_query", query)
            print("match_id_query.sponsor_id", query.sponsor_id, type(query.sponsor_id))
            print("g.current_user.id", g.current_user.id, type(g.current_user.id))
            if int(query.sponsor_id) == g.current_user.id:
                isSponsor = True

            # Update the Notification
            user = User.query.get_or_404(g.current_user.id)
            last_matched_file_read_time = user.last_matched_file_read_time or datetime(1900, 1, 1)

            # if isSponsor:
            #     record = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id_list[i]).order_by(Matched.match_id_timestamp.desc()).first()
            # else:
            record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id_list[i]).all()

            # get the latest output timestamp
            if record[0].match_id_timestamp > lastest_time:
                lastest_time = record[0].match_id_timestamp
            
            print("isSponsor", isSponsor)
            if isSponsor:
                print("sponsor")
                check_dict[task_id_list[i]] = 1
            else:
                print("recipient")
                check_dict[task_id_list[i]] = 0

    if lastest_time > last_matched_file_read_time:
        user.last_matched_file_read_time = lastest_time

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread match id', user.new_match_id()) 
        db.session.commit()
    print("check_dict", check_dict)
    dict = {"check_sponsor": check_dict}
    
    response = jsonify(dict)
    
    return response

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
    query = Matched.query.filter(Matched.task_id == task_id).first()
    if int(query.sponsor_id) == g.current_user.id:
        isSponsor = True

    data = {}
    if isSponsor:
        query = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair != g.current_user.id, Matched.task_id == task_id).all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'recipient_random_id_pair': [item.recipient_random_id_pair for item in query]
        }
    else:
        query = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id).all()

        data = {
            'match_id_file': [item.Matched_id_file for item in query],
            'sponsor_random_id': [item.sponsor_random_id for item in query]
        }

    return jsonify(data)