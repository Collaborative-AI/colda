# -*- coding: utf-8 -*-
import uuid
import json
import time

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Notification, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

# @main.route('/update_request_notification/', methods=['POST'])
# @token_auth.login_required
# def update_request_notification():

#     data = request.get_json()

#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'sender_random_id_list' not in data or not data.get('sender_random_id_list'):
#         return bad_request('sender_random_id_list is required.')
#     if 'task_id_list' not in data or not data.get('task_id_list'):
#         return bad_request('task_id_list is required.')

#     task_id_list = data.get('task_id_list')
#     print("update update_request_notification", task_id_list, type(task_id_list), len(task_id_list), g.current_user.id)

#     lastest_time = datetime(1900, 1, 1)

#     for i in range(len(task_id_list)):

#         record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id_list[i]).all()

#         # get the latest output timestamp
#         if record[0].match_id_timestamp > lastest_time:
#             lastest_time = record[0].match_id_timestamp

#     # Update the Notification
#     user = User.query.get_or_404(g.current_user.id)
#     last_requests_read_time = user.last_requests_read_time or datetime(1900, 1, 1)          
#     if lastest_time > last_requests_read_time:
#         user.last_requests_read_time = lastest_time

#         # submit to database
#         db.session.commit()
        
#         # Updata Notification
#         user.add_notification('unread request', user.new_request()) 
#         db.session.commit()

#     data = {"update request successfully": "true"}
#     response = jsonify(data)
    
#     return response

@main.route('/match_recipient_id/', methods=['POST'])
@token_auth.login_required
def match_recipient_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')

    task_id = data.get('task_id')

    record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
    sponsor_id = record.sponsor_id

    data_array = data['file']

    data_array_id = set()
    for i in range(1,len(data_array)-1):
        data_array_id.add(data_array[i][0])

    db_array = json.loads(record.Matched_id_file)
    same_id_keys = list(data_array_id & set(db_array))

    all_cur_task_matches = Matched.query.filter(Matched.recipient_id_pair != sponsor_id, Matched.task_id == task_id, Matched.test_indicator == "train").all()
    id_file_upload = 0
    for row in all_cur_task_matches:

        if int(row.recipient_id_pair) == g.current_user.id:
            print("---matching---------------",row.recipient_id_pair, type(row.recipient_id_pair))
            Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == g.current_user.id, Matched.test_indicator == "train").update({"Matched_id_file": json.dumps(same_id_keys), "matched_done": 1})
            db.session.commit()
            id_file_upload += 1
        elif row.matched_done and int(row.matched_done) == 1:
            print("tttttttttt")
            id_file_upload += 1

        if id_file_upload == len(all_cur_task_matches):

            queries = Matched.query.filter(Matched.recipient_id_pair != sponsor_id, Matched.task_id == task_id, Matched.test_indicator == "train").all()

            for row in queries:

                # update the db
                Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == row.recipient_id_pair, Matched.test_indicator == "train").update({"match_id_timestamp": datetime.utcnow()})
                db.session.commit()

                # send matched notification to the recipient
                user = User.query.get_or_404(row.recipient_id_pair)
          
                user.add_notification('unread match id', user.new_match_id()) 
                db.session.commit()

            user = User.query.get_or_404(sponsor_id)
            # send message notification to the sponsor when all recipient upload the output
            print("-----------------sendoutput", g.current_user.id)
            user.add_notification('unread match id', user.new_match_id())
            db.session.commit()

                  
    dict = {"stored": "recipient match id stored", "task_id": task_id}
    response = jsonify(dict)
    
    return response


@main.route('/match_test_recipient_id/', methods=['POST'])
@token_auth.login_required
def match_test_recipient_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    # if 'task_id' not in data or not data.get('task_id'):
    #     return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    # task_id = data.get('task_id')
    test_id = data.get('test_id')

    record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
    sponsor_id = record.sponsor_id

    data_array = data['file']

    data_array_id = set()
    for i in range(1,len(data_array)-1):
        data_array_id.add(data_array[i][0])

    db_array = json.loads(record.Matched_id_file)
    same_id_keys = list(data_array_id & set(db_array))

    user = User.query.get_or_404(g.current_user.id)
    all_cur_task_matches = Matched.query.filter(Matched.recipient_id_pair != sponsor_id, Matched.test_id == test_id, Matched.test_indicator == "test").all()
    id_file_upload = 0
    for row in all_cur_task_matches:

        if int(row.recipient_id_pair) == g.current_user.id:
            print("---matching---------------",row.recipient_id_pair, type(row.recipient_id_pair))
            Matched.query.filter(Matched.test_id == test_id, Matched.recipient_id_pair == g.current_user.id, Matched.test_indicator == "test").update({"Matched_id_file": json.dumps(same_id_keys), "matched_done": 1})
            db.session.commit()
            id_file_upload += 1
        elif row.matched_done and int(row.matched_done) == 1:
            id_file_upload += 1

        if id_file_upload == len(all_cur_task_matches):

            queries = Matched.query.filter(Matched.recipient_id_pair != sponsor_id, Matched.test_id == test_id, Matched.test_indicator == "test").all()

            for row in queries:

                # update the db
                Matched.query.filter(Matched.test_id == test_id, Matched.recipient_id_pair == row.recipient_id_pair, Matched.test_indicator == "test").update({"match_id_timestamp": datetime.utcnow()})
                db.session.commit()

                # send matched notification to the recipient
                user = User.query.get_or_404(row.recipient_id_pair)
          
                user.add_notification('unread test match id', user.new_test_match_id()) 
                db.session.commit()

            user = User.query.get_or_404(sponsor_id)
            # send message notification to the sponsor when all recipient upload the output
            user.add_notification('unread test match id', user.new_test_match_id())
            db.session.commit()

                  
    dict = {"stored": "recipient test match id stored", "test_id": test_id}
    response = jsonify(dict)
    
    return response
    
# @main.route('/match_sponsor_id/', methods=['POST'])
# @token_auth.login_required
# def match_sponsor_id():

#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'task_id' not in data or not data.get('task_id'):
#         return bad_request('task_id is required.')  
#     if 'file' not in data or not data.get('file'):
#         return bad_request('File is required.')
    
#     data_array = data.get('file')
#     task_id = data.get('task_id')

#     response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair != g.current_user.id, Matched.task_id == task_id).all()

#     # while loop, wait for all recipients update match id file
#     match_ID_recipient_upload = 0
#     while match_ID_recipient_upload < len(response):
#         response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair != g.current_user.id, Matched.task_id == task_id).all()

#         match_ID_recipient_upload = 0
#         for row in response:
#             if row.Matched_id_file:
#                 match_ID_recipient_upload += 1
#         time.sleep(3)

#     # count the distinct id in the Sponsor ID file
#     data_array_id = set()
#     for i in range(1,len(data_array)-1):
#         data_array_id.add(data_array[i][0])
            
#     # data_array_id = {}
#     # for i in range(1,len(data_array)-1):
#     #     if data_array[i][0] not in data_array_id:
#     #         data_array_id[data_array[i][0]] = 1

#     # match id file
#     for row in response:
#         # if row.Matched_id_file:
#         same_id = {}
#         db_array = json.loads(row.Matched_id_file)

#         same_id_keys = list(data_array_id & set(db_array))
        
#         # # previous stored id
#         # for i in range(len(db_array)):
#         #     if db_array[i] in data_array_id:
#         #         same_id[db_array[i]] = 1

#         # # Store the key, dont need the value
#         # same_id_keys = []
#         # for i in same_id.keys():
#         #     same_id_keys.append(i)
        
#         # update the db
#         Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == row.recipient_id_pair).update({"Matched_id_file": json.dumps(same_id_keys), "match_id_timestamp": datetime.utcnow()})
#         db.session.commit()

#         # send matched notification to the recipient
#         user = User.query.get_or_404(row.recipient_id_pair)
  
#         user.add_notification('unread match id', user.new_match_id()) 
#         db.session.commit()

#     # when all match_id match, add notification to sponsor
#     user = User.query.get_or_404(g.current_user.id)
#     Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == g.current_user.id).update({"match_id_timestamp": datetime.utcnow()})
#     db.session.commit()
#     # print("user_id", g.current_user.id)
#     user.add_notification('unread match id', user.new_match_id()) 
#     db.session.commit()
    
#     dict = {"stored": "sponsor stores match id file successfully", "task_id": task_id}
#     response = jsonify(dict)

#     return response


