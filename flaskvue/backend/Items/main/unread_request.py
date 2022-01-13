# -*- coding: utf-8 -*-
import uuid
import json
import time

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.apollo_utils import log, generate_msg

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Notification, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/match_assistor_id/', methods=['POST'])
@token_auth.login_required
def match_assistor_id():

    """
    Match the id of sponsor and assistor

    Parameters:
        task_id - String. The id of task
        file - String. The matching id file sent by sponsor

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task }

    Raises:
        KeyError - raises an exception
    """
    print('match_assistor_id')
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')

    task_id = data.get('task_id')

    record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
    print('record', task_id, g.current_user.id, record)
    sponsor_id = record.sponsor_id

    data_array = data['file']

    log(generate_msg('Assistor training stage'), g.current_user.id, task_id)
    log(generate_msg('-------------------- unread request begins'), g.current_user.id, task_id)
    log(generate_msg('2.1:', 'assistor match_assistor_id begins'), g.current_user.id, task_id)

    # db_array: sponsor match id file
    # data_array: assistor match id file

    # x 本地id
    # y 有交集的id
    # intersect1d(x,y) x_index => 本地的index顺序

    # y 有交集的id
    # python3 match_id_position.py (文件夹地址)
    # 写进去， python3 handle_match_id.py 
  
    # data_array_id = set()
    # for i in range(1,len(data_array)):
    #     data_array_id.add(data_array[i][0])

    # data_array = data_array.split("\n")

    # data_array_id = set()
    # for i in range(len(data_array)):
    #     if data_array[i]:
    #         if data_array[i][-1] == '\r':
    #             data_array_id.add(data_array[i][:-1])
    #         else:
    #             data_array_id.add(data_array[i])

    data_array_id = set(data_array)
    db_array = json.loads(record.Matched_id_file)
    # print('db_array', type(db_array), db_array)
    # print('data_array_id', type(data_array_id), data_array_id)
    same_id_keys = list(data_array_id & set(db_array))
    # print('same_id_keys', same_id_keys)

    all_cur_task_matches = Matched.query.filter(Matched.assistor_id_pair != sponsor_id, Matched.task_id == task_id, Matched.test_indicator == "train").all()
    id_file_upload = 0
    for row in all_cur_task_matches:

        if int(row.assistor_id_pair) == g.current_user.id:
            log(generate_msg('2.2:', 'assistor matching', row.assistor_id_pair), g.current_user.id, task_id)
            Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == g.current_user.id, Matched.test_indicator == "train").update({"Matched_id_file": json.dumps(same_id_keys), "matched_done": 1})
            db.session.commit()
            id_file_upload += 1
        elif row.matched_done and int(row.matched_done) == 1:
            id_file_upload += 1

        if id_file_upload == len(all_cur_task_matches):

            log(generate_msg('2.3:', 'assistor matching_done', 'number of assistor:', id_file_upload), g.current_user.id, task_id)
            queries = Matched.query.filter(Matched.assistor_id_pair != sponsor_id, Matched.task_id == task_id, Matched.test_indicator == "train").all()

            for row in queries:

                # update the db
                Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == row.assistor_id_pair, Matched.test_indicator == "train").update({"match_id_timestamp": datetime.utcnow()})
                db.session.commit()

                # send matched notification to the assistor
                user = User.query.get_or_404(row.assistor_id_pair)
          
                user.add_notification('unread match id', user.new_match_id()) 
                print('match_assistor_id1')
                db.session.commit()

            user = User.query.get_or_404(sponsor_id)
            # send message notification to the sponsor when all assistor upload the output
            user.add_notification('unread match id', user.new_match_id())
            print('match_assistor_id2')
            db.session.commit()

            log(generate_msg('2.4:', 'Server sends unread match id to all participants of this task'), g.current_user.id, task_id)
              
    dict = {"stored": "assistor match id stored", "task_id": task_id}

    if id_file_upload != len(all_cur_task_matches):
        log(generate_msg('2.3:', 'assistor match_assistor_id done'), g.current_user.id, task_id)
        log(generate_msg('------------------------------ unread request done\n'), g.current_user.id, task_id)
    else:
        log(generate_msg('2.5:', 'assistor match_assistor_id done'), g.current_user.id, task_id)
        log(generate_msg('------------------------------ unread request done\n'), g.current_user.id, task_id)

    
    return jsonify(dict)


@main.route('/match_test_assistor_id/', methods=['POST'])
@token_auth.login_required
def match_test_assistor_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    task_id = data.get('task_id')
    test_id = data.get('test_id')

    record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
    print('match_test_assistor_id', record)
    sponsor_id = record.sponsor_id

    data_array = data['file']

    log(generate_msg('Assistor testing stage'), g.current_user.id, task_id, test_id)
    log(generate_msg('-------------------- unread test request begins'), g.current_user.id, task_id, test_id)
    log(generate_msg('Test 2.1:', 'assistor match_test_assistor_id begins'), g.current_user.id, task_id, test_id)

    # data_array_id = set()
    # for i in range(1,len(data_array)):
    #     data_array_id.add(data_array[i][0])

    # data_array = data_array.split("\n")

    # data_array_id = set()
    # for i in range(len(data_array)):
    #     if data_array[i]:
    #         if data_array[i][-1] == '\r':
    #             data_array_id.add(data_array[i][:-1])
    #         else:
    #             data_array_id.add(data_array[i])

    data_array_id = set(data_array)
    db_array = json.loads(record.Matched_id_file)
    same_id_keys = list(data_array_id & set(db_array))
   
    user = User.query.get_or_404(g.current_user.id)
    all_cur_task_matches = Matched.query.filter(Matched.assistor_id_pair != sponsor_id, Matched.test_id == test_id, Matched.test_indicator == "test").all()
    id_file_upload = 0
    for row in all_cur_task_matches:

        if int(row.assistor_id_pair) == g.current_user.id:
            log(generate_msg('Test 2.2:', 'assistor matching', row.assistor_id_pair), g.current_user.id, task_id, test_id)
            Matched.query.filter(Matched.test_id == test_id, Matched.assistor_id_pair == g.current_user.id, Matched.test_indicator == "test").update({"Matched_id_file": json.dumps(same_id_keys), "matched_done": 1})
            db.session.commit()
            id_file_upload += 1
        elif row.matched_done and int(row.matched_done) == 1:
            id_file_upload += 1

        if id_file_upload == len(all_cur_task_matches):
            log(generate_msg('Test 2.3:', 'match_done', 'number of assistor:', id_file_upload), g.current_user.id, task_id, test_id)
            queries = Matched.query.filter(Matched.assistor_id_pair != sponsor_id, Matched.test_id == test_id, Matched.test_indicator == "test").all()

            for row in queries:

                # update the db
                Matched.query.filter(Matched.test_id == test_id, Matched.assistor_id_pair == row.assistor_id_pair, Matched.test_indicator == "test").update({"match_id_timestamp": datetime.utcnow()})
                db.session.commit()

                # send matched notification to the assistor
                user = User.query.get_or_404(row.assistor_id_pair)
                user.add_notification('unread test match id', user.new_test_match_id()) 
                db.session.commit()

            log(generate_msg('Test 2.4:', 'Server sends unread match id to all participants of this test'), g.current_user.id, task_id, test_id)

            user = User.query.get_or_404(sponsor_id)
            # send message notification to the sponsor when all assistor upload the output
            user.add_notification('unread test match id', user.new_test_match_id())
            db.session.commit()
  
    dict = {"stored": "assistor test match id stored", "test_id": test_id}
    log(generate_msg('Test 2.5:', 'assistor match_test_assistor_id done'), g.current_user.id, task_id, test_id)
    log(generate_msg('----------------------------- unread test request done\n'), g.current_user.id, task_id, test_id)

    return jsonify(dict)
    
    
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

#     response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id, Matched.task_id == task_id).all()

#     # while loop, wait for all assistors update match id file
#     match_ID_assistor_upload = 0
#     while match_ID_assistor_upload < len(response):
#         response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id, Matched.task_id == task_id).all()

#         match_ID_assistor_upload = 0
#         for row in response:
#             if row.Matched_id_file:
#                 match_ID_assistor_upload += 1
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
#         Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == row.assistor_id_pair).update({"Matched_id_file": json.dumps(same_id_keys), "match_id_timestamp": datetime.utcnow()})
#         db.session.commit()

#         # send matched notification to the assistor
#         user = User.query.get_or_404(row.assistor_id_pair)
  
#         user.add_notification('unread match id', user.new_match_id()) 
#         db.session.commit()

#     # when all match_id match, add notification to sponsor
#     user = User.query.get_or_404(g.current_user.id)
#     Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == g.current_user.id).update({"match_id_timestamp": datetime.utcnow()})
#     db.session.commit()
#     # print("user_id", g.current_user.id)
#     user.add_notification('unread match id', user.new_match_id()) 
#     db.session.commit()
    
#     dict = {"stored": "sponsor stores match id file successfully", "task_id": task_id}
#     response = jsonify(dict)

#     return response


