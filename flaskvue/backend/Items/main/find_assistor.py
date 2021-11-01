# -*- coding: utf-8 -*-
import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/create_new_train_task', methods=['GET'])
@token_auth.login_required
def create_new_train_task():
    task_id = str(uuid.uuid4())

    data = {"task_id": task_id}
    
    response = jsonify(data)
    
    return response

@main.route('/create_new_test_task', methods=['GET'])
@token_auth.login_required
def create_new_test_task():
    test_id = str(uuid.uuid4())

    data = {"test_id": test_id}
    
    response = jsonify(data)
    
    return response

@main.route('/find_assistor', methods=['POST'])
@token_auth.login_required
def find_assistor():

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'assistor_username_list' not in data or not data.get('assistor_username_list'):
        return bad_request('assistor_username_list is required.')
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'task_name' not in data:
        return bad_request('task_name is required.')
    if 'task_description' not in data:
        return bad_request('task_description is required.')

    assistor_username_list = data['assistor_username_list']
    id_file = data['id_file']
    task_id = data['task_id']
    task_name = data['task_name']
    task_description = data['task_description']
    
    assistor_id_list = []
    for username in assistor_username_list:
        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify("wrong username")
        print("user.id", username, user.id)
        assistor_id_list.append(user.id)

    # user = User.query.filter_by(username="unittest").first()
    # print(user.id)

    # If the user dont type in the task name, we give it a basic name
    

    id_file = id_file.split("\n")
    data_array_id = set()
    for i in range(len(id_file)):
        if id_file[i]: 
            data_array_id.add(id_file[i])
    
    data_array_id = list(data_array_id)
    print("data_array_id", data_array_id)

    # extract ID
    # data_array_id = set()
    # for i in range(1,len(id_file)):
    #     data_array_id.add(id_file[i][0])
    
    # data_array_id = list(data_array_id)

    print("assistor_id_list", assistor_id_list)

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(assistor), testc: id 6(assistor)

    # Unique in each task
    
    sponsor_random_id = str(uuid.uuid4())

    # print(g.current_user.id, type(g.current_user.id),"1")
    for assistor_id in assistor_id_list:
        user = User.query.get_or_404(assistor_id)
      
        matched = Matched()
        matched.sponsor_id = g.current_user.id
        print("g.current_user.id", g.current_user.id)
        matched.assistor_id_pair = user.id
        matched.task_id = task_id
        if task_name == "":
            temp_task_name = "Cooperate with " + g.current_user.username
        matched.task_name = temp_task_name
        matched.task_description = task_description

        matched.sponsor_random_id = sponsor_random_id

        assistor_random_id = str(uuid.uuid4())
        matched.assistor_random_id_pair = assistor_random_id

        matched.Matched_id_file = json.dumps(data_array_id)
        matched.test_indicator = "train"
        matched.Terminate = "false"

        db.session.add(matched)
        db.session.commit()
        # send matched notification to the assistor
        user.add_notification('unread request', user.new_request()) 
        db.session.commit()
    # print(g.current_user.id, type(g.current_user.id),"2")
    # A A
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    if task_name == "":
        temp_task_name = "Cooperate with " + ",".join(assistor_username_list)
    matched.task_name = temp_task_name
    matched.task_description = task_description
    matched.sponsor_id = g.current_user.id
    matched.assistor_id_pair = g.current_user.id
    matched.task_id = task_id
    matched.sponsor_random_id = sponsor_random_id
    matched.assistor_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "train"
    matched.Terminate = "false"
    db.session.add(matched) 
    # print(g.current_user.id, type(g.current_user.id),"3")                       
    db.session.commit()

    # print(g.current_user.id, type(g.current_user.id),"4")

    # query = Matched.query.filter(Matched.task_id == task_id).all()
    # for row in query:
    #     print("all_find_assistor_query", row.sponsor_id, type(row.sponsor_id), row.assistor_id_pair, type(row.assistor_id_pair))

    # record1 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair == 2, Matched.task_id == task_id).first()
    # print("1111111", json.loads(record1.Matched_id_file))

    # record2 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair == str(2), Matched.task_id == task_id).first()
    # print("22222", json.loads(record2.Matched_id_file))
    
    # query = Matched.query.filter(Matched.task_id == task_id).first()
    # print("find_assistor_query", query.sponsor_id, type(query.sponsor_id))

    data = {"task_id": task_id, 'assistor_num': len(assistor_id_list)}
    
    response = jsonify(data)
    
    return response


@main.route('/find_test_assistor', methods=['POST'])
@token_auth.login_required
def find_test_assistor():

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    if 'test_name' not in data:
        return bad_request('test_name is required.')
    if 'test_description' not in data:
        return bad_request('test_description is required.')

    task_id = data['task_id']
    id_file = data['id_file']
    test_id = data['test_id']
    test_name = data['task_name']
    test_description = data['task_description']

    assistor_id_list = []
    assistor_id_queries = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id,Matched.task_id == task_id, Matched.test_indicator == "train").all()
    for row in assistor_id_queries:
        assistor_id_list.append(row.assistor_id_pair)

    id_file = id_file.split("\n")
    data_array_id = set()
    for i in range(len(id_file)):
        if id_file[i]: 
            data_array_id.add(id_file[i])
    
    data_array_id = list(data_array_id)

    # # extract ID
    # data_array_id = set()
    # for i in range(1,len(id_file)):
    #     data_array_id.add(id_file[i][0])
    
    # data_array_id = list(data_array_id)

    print("assistor_id_list", assistor_id_list)

    Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "test").all()
    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(assistor), testc: id 6(assistor)

    # Unique in each test
    sponsor_random_id = str(uuid.uuid4())

    # print(g.current_user.id, type(g.current_user.id),"1")
    for assistor_id in assistor_id_list:
        user = User.query.get_or_404(assistor_id)
      
        matched = Matched()
        matched.sponsor_id = g.current_user.id
        matched.assistor_id_pair = user.id
        matched.task_id = task_id
        if test_name == "":
            temp_test_name = "Test of " + task_id
        matched.test_name = temp_test_name
        matched.test_description = test_description

        matched.sponsor_random_id = sponsor_random_id

        assistor_random_id = str(uuid.uuid4())
        matched.assistor_random_id_pair = assistor_random_id

        matched.Matched_id_file = json.dumps(data_array_id)
        matched.test_indicator = "test"
        matched.test_id = test_id

        matched.Terminate = "false"

        db.session.add(matched)
        db.session.commit()
        # send matched notification to the assistor
        user.add_notification('unread test request', user.new_test_request()) 
        db.session.commit()
    # print(g.current_user.id, type(g.current_user.id),"2")
    # A A
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    matched.sponsor_id = g.current_user.id
    matched.assistor_id_pair = g.current_user.id
    matched.task_id = task_id
    if test_name == "":
        temp_test_name = "Test of " + task_id
    matched.test_name = temp_test_name
    matched.test_description = test_description
    matched.sponsor_random_id = sponsor_random_id
    matched.assistor_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "test"
    matched.test_id = test_id
    matched.Terminate = "false"

    db.session.add(matched) 
    # print(g.current_user.id, type(g.current_user.id),"3")                       
    db.session.commit()

    # print(g.current_user.id, type(g.current_user.id),"4")

    # query = Matched.query.filter(Matched.task_id == task_id).all()
    # for row in query:
    #     print("all_find_assistor_query", row.sponsor_id, type(row.sponsor_id), row.assistor_id_pair, type(row.assistor_id_pair))

    # record1 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair == 2, Matched.task_id == task_id).first()
    # print("1111111", json.loads(record1.Matched_id_file))

    # record2 = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair == str(2), Matched.task_id == task_id).first()
    # print("22222", json.loads(record2.Matched_id_file))
    
    # query = Matched.query.filter(Matched.task_id == task_id).first()
    # print("find_assistor_query", query.sponsor_id, type(query.sponsor_id))

    data = {"task_id": task_id, 'assistor_num': len(assistor_id_list), 'test_id': test_id}
    
    response = jsonify(data)
    
    return response

@main.route('/get_test_history_id', methods=['POST'])
@token_auth.login_required
def get_test_history_id():

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    task_id = data['task_id']

    records = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "test").all()

    test_id_list = []
    for row in records:
        test_id_list.append(row.test_id)
    
    data = {"test_id_list": test_id_list}
    print("test_id_list", data)
    response = jsonify(data)
    
    return response