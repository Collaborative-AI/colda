# -*- coding: utf-8 -*-
import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.apollo_utils import log, generate_msg

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Matched, Pending
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/add_train_pending', methods=['POST'])
@token_auth.login_required
def add_train_pending():
    '''
     Add traing stage pending to the Pending database
    
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data['task_id']

    # Retrieve task name and task description of thie unique task_id
    query = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
    task_name = query.task_name
    task_mode = query.task_mode
    model_name = query.model_name
    metric_name = query.metric_name
    task_description = query.task_description

    pending = Pending()
    pending.pending_assistor_id = g.current_user.id
    pending.pending_task_id = task_id
    pending.pending_task_name = task_name
    pending.pending_task_mode = task_mode
    pending.pending_model_name = model_name
    pending.pending_metric_name = metric_name
    pending.pending_task_description = task_description
    pending.test_indicator = "train"

    db.session.add(pending)
    db.session.commit()
    
    return jsonify("add train pending successfully")

@main.route('/add_test_pending', methods=['POST'])
@token_auth.login_required
def add_test_pending():
    '''
     Add test stage pending to the Pending database
    
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')
    

    test_id = data['test_id']
    

    # Retrieve task name and task description of thie unique task_id
    query = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id, Matched.test_indicator == "test").first()
    test_name = query.test_name
    task_mode = query.task_mode
    model_name = query.model_name
    metric_name = query.metric_name
    test_description = query.test_description
    task_id = query.task_id

    pending = Pending()
    pending.pending_assistor_id = g.current_user.id
    pending.pending_task_id = task_id
    pending.pending_test_id = test_id
    pending.pending_task_name = test_name
    pending.pending_task_mode = task_mode
    pending.pending_model_name = model_name
    pending.pending_metric_name = metric_name
    pending.pending_task_description = test_description
    pending.test_indicator = "test"

    db.session.add(pending)
    db.session.commit()
    
    return jsonify("add test pending successfully")


@main.route('/get_all_pending', methods=['GET'])
@token_auth.login_required
def get_all_pending():
    '''
     Get all pending from the Pending database
    
    '''

    # Retrieve sponsor id of thie unique test_id
    all_pending_items = Pending.query.filter(Pending.pending_assistor_id == g.current_user.id).all()
    res = [item.to_dict() for item in all_pending_items]

    data = {"all_pending_items": res}
    
    return jsonify(data)

@main.route('/delete_pending', methods=['POST'])
@token_auth.login_required
def dalete_pending():
    '''
     Delete the specific task_id or test_id in pending
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data:
        return bad_request('task_id is required.')
    if 'test_id' not in data:
        return bad_request('test_id is required.')
    if 'test_indicator' not in data or not data.get('test_indicator'):
        return bad_request('test_indicator is required.')

    task_id = data['task_id']
    test_id = data['test_id']
    test_indicator = data['test_indicator']

    if test_indicator == "train":
        Pending.query.filter(Pending.pending_assistor_id == g.current_user.id, Pending.test_indicator == test_indicator, Pending.pending_task_id == task_id).delete()
        db.session.commit()
    else:
        Pending.query.filter(Pending.pending_assistor_id == g.current_user.id, Pending.test_indicator == test_indicator, Pending.pending_test_id == test_id).delete()
        db.session.commit()

    return jsonify("Sucessfully delete")