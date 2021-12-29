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
from Items.main.apollo_utils import log, generate_msg

@main.route('/create_new_train_task', methods=['GET'])
@token_auth.login_required
def create_new_train_task():

    """
    Generate a new train task id from unique uuid4

    Parameters:
        None

    Returns:
        task_id - String. String task_id

    Raises:
        KeyError - raises an exception
    """

    task_id = str(uuid.uuid4())
    data = {"task_id": task_id}
    
    return jsonify(data)

@main.route('/create_new_test_task', methods=['GET'])
@token_auth.login_required
def create_new_test_task():

    """
    Generate a new test task id from unique uuid4

    Parameters:
        None

    Returns:
        test_id - String. String test_id

    Raises:
        KeyError - raises an exception
    """

    test_id = str(uuid.uuid4())
    data = {"test_id": test_id}
    
    return jsonify(data)

@main.route('/find_assistor', methods=['POST'])
@token_auth.login_required
def find_assistor():

    """
    Add information of current task to matched database.

    Parameters:
        assistor_username_list - List[String]. The username of assistors for this task. 
        id_file - String. The matching id file sent by sponsor
        task_id - String. The id of task
        task_name - String. The name of task, which could be None.
        task_description - String. The description of task, which could be None.

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task }

    Raises:
        KeyError - raises an exception
    """

    # check the data sent by the sponsor
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'assistor_username_list' not in data or not data.get('assistor_username_list'):
        return bad_request('assistor_username_list is required.')
    if 'id_file' not in data or not data.get('id_file'):
        return bad_request('id_file is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'task_mode' not in data:
        return bad_request('task_mode is required.')
    if 'model_name' not in data:
        return bad_request('model_name is required.')
    if 'metric_name' not in data:
        return bad_request('metric_name is required.')
    if 'task_name' not in data:
        return bad_request('task_name is required.')
    if 'task_description' not in data:
        return bad_request('task_description is required.')
    print('find_assistor----------------')
    assistor_username_list = data['assistor_username_list']
    id_file = data['id_file']
    task_id = data['task_id']
    task_name = data['task_name']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    task_description = data['task_description']
    
    assistor_id_list = []
    for username in assistor_username_list:
        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify("wrong username")
        print("user.id", username, user.id)
        assistor_id_list.append(user.id)

    log(generate_msg('Sponsor training stage'), g.current_user.id, task_id)
    log(generate_msg('-------------------- find_assistor begins'), g.current_user.id, task_id)
    log(generate_msg('1.1', 'sponsor find_assistor'), g.current_user.id, task_id)

    # If the user dont type in the task name, we give it a basic name
    id_file = id_file.split("\n")
    data_array_id = set()
    for i in range(len(id_file)):
        if id_file[i]: 
            data_array_id.add(id_file[i])
    
    data_array_id = list(data_array_id)

    log(generate_msg('1.2:', 'sponsor handles id data done'), g.current_user.id, task_id)

    # extract ID
    # data_array_id = set()
    # for i in range(1,len(id_file)):
    #     data_array_id.add(id_file[i][0])
    
    # data_array_id = list(data_array_id)

    # sponsor_random_id is unique in each task    
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
        else:
            matched.task_name = task_name
        matched.task_description = task_description
        matched.task_mode = task_mode
        matched.model_name = model_name
        matched.metric_name = metric_name
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
    
    log(generate_msg('1.3:', 'sponsor adds all unread request to assistors'), g.current_user.id, task_id)
    # print(g.current_user.id, type(g.current_user.id),"2")
    # A A
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    if task_name == "":
        temp_task_name = "Cooperate with " + ",".join(assistor_username_list)
        matched.task_name = temp_task_name
    else:
        matched.task_name = task_name
    
    matched.task_description = task_description
    matched.sponsor_id = g.current_user.id
    matched.assistor_id_pair = g.current_user.id
    matched.task_id = task_id
    matched.task_mode = task_mode
    matched.model_name = model_name
    matched.metric_name = metric_name
    matched.sponsor_random_id = sponsor_random_id
    matched.assistor_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "train"
    matched.Terminate = "false"
    db.session.add(matched) 
    # print(g.current_user.id, type(g.current_user.id),"3")                       
    db.session.commit()

    data = {"task_id": task_id, 'assistor_num': len(assistor_id_list)}
    
    log(generate_msg('1.4:', 'sponsor adds unread request to itself'), g.current_user.id, task_id)
    log(generate_msg('--------------------sponsor find assistor done \n'), g.current_user.id, task_id)

    return jsonify(data)


@main.route('/find_test_assistor', methods=['POST'])
@token_auth.login_required
def find_test_assistor():

    """
    Add information of current task to matched database.

    Parameters:
        assistor_username_list - List[String]. The username of assistors for this task. 
        id_file - String. The matching id file sent by sponsor
        task_id - String. The id of task
        test_id - String. The id of test
        test_name - String. The name of test, which could be None.
        test_description - String. The description of test, which could be None.

    Returns:
        data - Dict. { task_id - String: The id of task, assistor_num - Integer: The number of assistors in this task, test_id - String: The id of test }

    Raises:
        KeyError - raises an exception
    """

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
    if 'task_mode' not in data:
        return bad_request('task_mode is required.')
    if 'model_name' not in data:
        return bad_request('model_name is required.')
    if 'metric_name' not in data:
        return bad_request('metric_name is required.')
    if 'test_name' not in data:
        return bad_request('test_name is required.')
    if 'test_description' not in data:
        return bad_request('test_description is required.')

    task_id = data['task_id']
    id_file = data['id_file']
    test_id = data['test_id']
    test_name = data['test_name']
    task_mode = data['task_mode']
    model_name = data['model_name']
    metric_name = data['metric_name']
    test_description = data['test_description']

    assistor_id_list = []
    assistor_id_queries = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.assistor_id_pair != g.current_user.id,Matched.task_id == task_id, Matched.test_indicator == "train").all()
    for row in assistor_id_queries:
        assistor_id_list.append(row.assistor_id_pair)

    log(generate_msg('Sponsor testing stage'), g.current_user.id, task_id)
    log(generate_msg('------------------------- find_test_assistor begins'), g.current_user.id, task_id, test_id)
    log(generate_msg('Test 1.1', 'sponsor find_assistor'), g.current_user.id, task_id, test_id)

    id_file = id_file.split("\n")
    data_array_id = set()
    for i in range(len(id_file)):
        if id_file[i]: 
            data_array_id.add(id_file[i])
    
    data_array_id = list(data_array_id)

    log(generate_msg('Test 1.2', 'sponsor handles id data done'), g.current_user.id, task_id, test_id)
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
        else:
            matched.test_name = test_name
        
        matched.test_description = test_description
        matched.task_mode = task_mode
        matched.model_name = model_name
        matched.metric_name = metric_name
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
    log(generate_msg('Test 1.3', 'sponsor adds all unread request to assistors'), g.current_user.id, task_id, test_id)

    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    matched.sponsor_id = g.current_user.id
    matched.assistor_id_pair = g.current_user.id
    matched.task_id = task_id
    
    if test_name == "":
        temp_test_name = "Test of " + task_id
        matched.test_name = temp_test_name
    else:
        matched.test_name = test_name
    matched.task_mode = task_mode
    matched.model_name = model_name
    matched.metric_name = metric_name
    matched.test_description = test_description
    matched.sponsor_random_id = sponsor_random_id
    matched.assistor_random_id_pair = sponsor_random_id
    matched.Matched_id_file = json.dumps(data_array_id)
    matched.test_indicator = "test"
    matched.test_id = test_id
    matched.Terminate = "false"

    db.session.add(matched)                      
    db.session.commit()

    data = {"task_id": task_id, 'assistor_num': len(assistor_id_list), 'test_id': test_id}
    
    log(generate_msg('Test 1.4', 'sponsor adds unread request to itself'), g.current_user.id, task_id, test_id)
    log(generate_msg('------------------------- sponsor find_test_assistor done\n'), g.current_user.id, task_id, test_id)

    return jsonify(data)

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