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
    task_description = query.task_description

    pending = Pending()
    pending.pending_assistor_id = g.current_user.id
    pending.pending_task_id = task_id
    pending.pending_task_name = task_name
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
    test_description = query.test_description

    pending = Pending()
    pending.pending_assistor_id = g.current_user.id
    pending.pending_test_id = test_id
    pending.pending_task_name = test_name
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
    queries = Pending.query.filter(Pending.pending_assistor_id == g.current_user.id).all()
    
    res = []
    
    
    return jsonify("add test pending successfully")