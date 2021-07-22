# -*- coding: utf-8 -*-
import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/find_recipient', methods=['POST'])
@token_auth.login_required
def find_recipient():

    # find recipient algorithm, return all_recipient_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'recipient_id_list' not in data or not data.get('recipient_id_list'):
        return bad_request('recipient_id_list is required.')
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')

    recipient_id_list = data['recipient_id_list']
    id_file = data['id_file']
    
    # extract ID
    data_array_id = set()
    for i in range(1,len(id_file)-1):
        data_array_id.add(id_file[i][0])
    
    data_array_id = list(data_array_id)

    print("recipient_id_list", recipient_id_list)

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)

    # Unique in each task
    task_id = str(uuid.uuid4())
    sponsor_random_id = str(uuid.uuid4())

    # print(g.current_user.id, type(g.current_user.id),"1")
    for recipient_id in recipient_id_list:
        user = User.query.get_or_404(recipient_id)
      
        matched = Matched()
        matched.sponsor_id = g.current_user.id
        matched.recipient_id_pair = user.id
        matched.task_id = task_id

        matched.sponsor_random_id = sponsor_random_id

        recipient_random_id = str(uuid.uuid4())
        matched.recipient_random_id_pair = recipient_random_id

        matched.Matched_id_file = json.dumps(data_array_id)
        matched.test_indicator = "train"
        db.session.add(matched)
        db.session.commit()
        # send matched notification to the recipient
        user.add_notification('unread request', user.new_request()) 
        db.session.commit()
    # print(g.current_user.id, type(g.current_user.id),"2")
    # A A
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    matched.sponsor_id = g.current_user.id
    matched.recipient_id_pair = g.current_user.id
    matched.task_id = task_id
    matched.sponsor_random_id = sponsor_random_id
    matched.recipient_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "train"
    db.session.add(matched) 
    # print(g.current_user.id, type(g.current_user.id),"3")                       
    db.session.commit()

    # print(g.current_user.id, type(g.current_user.id),"4")

    # query = Matched.query.filter(Matched.task_id == task_id).all()
    # for row in query:
    #     print("all_find_recipient_query", row.sponsor_id, type(row.sponsor_id), row.recipient_id_pair, type(row.recipient_id_pair))

    # record1 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair == 2, Matched.task_id == task_id).first()
    # print("1111111", json.loads(record1.Matched_id_file))

    # record2 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair == str(2), Matched.task_id == task_id).first()
    # print("22222", json.loads(record2.Matched_id_file))
    
    # query = Matched.query.filter(Matched.task_id == task_id).first()
    # print("find_recipient_query", query.sponsor_id, type(query.sponsor_id))

    data = {"task_id": task_id, 'recipient_num': len(recipient_id_list)}
    
    response = jsonify(data)
    
    return response


@main.route('/find_test_recipient', methods=['POST'])
@token_auth.login_required
def find_test_recipient():

    # find recipient algorithm, return all_recipient_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')

    task_id = data['task_id']
    id_file = data['id_file']

    recipient_id_list = []
    recipient_id_queries = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair != g.current_user.id,Matched.task_id == task_id, Matched.test_indicator == "train").all()
    for row in recipient_id_queries:
        recipient_id_list.append(row.recipient_id_pair)

    # extract ID
    data_array_id = set()
    for i in range(1,len(id_file)-1):
        data_array_id.add(id_file[i][0])
    
    data_array_id = list(data_array_id)

    print("recipient_id_list", recipient_id_list)

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)

    # Unique in each task
    sponsor_random_id = str(uuid.uuid4())

    # print(g.current_user.id, type(g.current_user.id),"1")
    for recipient_id in recipient_id_list:
        user = User.query.get_or_404(recipient_id)
      
        matched = Matched()
        matched.sponsor_id = g.current_user.id
        matched.recipient_id_pair = user.id
        matched.task_id = task_id

        matched.sponsor_random_id = sponsor_random_id

        recipient_random_id = str(uuid.uuid4())
        matched.recipient_random_id_pair = recipient_random_id

        matched.Matched_id_file = json.dumps(data_array_id)
        matched.test_indicator = "test"
        db.session.add(matched)
        db.session.commit()
        # send matched notification to the recipient
        user.add_notification('unread test request', user.new_test_request()) 
        db.session.commit()
    # print(g.current_user.id, type(g.current_user.id),"2")
    # A A
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    matched.sponsor_id = g.current_user.id
    matched.recipient_id_pair = g.current_user.id
    matched.task_id = task_id
    matched.sponsor_random_id = sponsor_random_id
    matched.recipient_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "test"
    db.session.add(matched) 
    # print(g.current_user.id, type(g.current_user.id),"3")                       
    db.session.commit()

    # print(g.current_user.id, type(g.current_user.id),"4")

    # query = Matched.query.filter(Matched.task_id == task_id).all()
    # for row in query:
    #     print("all_find_recipient_query", row.sponsor_id, type(row.sponsor_id), row.recipient_id_pair, type(row.recipient_id_pair))

    # record1 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair == 2, Matched.task_id == task_id).first()
    # print("1111111", json.loads(record1.Matched_id_file))

    # record2 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.recipient_id_pair == str(2), Matched.task_id == task_id).first()
    # print("22222", json.loads(record2.Matched_id_file))
    
    # query = Matched.query.filter(Matched.task_id == task_id).first()
    # print("find_recipient_query", query.sponsor_id, type(query.sponsor_id))

    data = {"task_id": task_id, 'recipient_num': len(recipient_id_list)}
    
    response = jsonify(data)
    
    return response

