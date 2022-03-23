# -*- coding: utf-8 -*-
import json
import math
import heapq

from typing import Match

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from operator import itemgetter

from Items import db, pyMongo
# import BluePrint
from Items.main import main
# from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import log, generate_msg
from Items.main.auth import token_auth
from Items.main.utils import obtain_user_id_from_token, verify_token_user_id_and_function_caller_id
from Items.main.mongoDB import mongoDB, train_mongoDB, test_mongoDB

@main.route('/get_user_history/<string:id>', methods=['GET'])
@token_auth.login_required
def get_user_history(id):

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)

    participated_train_task = user_document['participated_train_task']
    participated_task = []
    for task_id in participated_train_task:
        train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
        task_name = train_match_document['task_name']
        task_description = train_match_document['task_description']
        timestamp = 5
        sub_task = {
            'task_id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'test_indicator': 'train',
            'test_id': None,
            'test_name': None,
            'test_description': None,
        }
        heapq.heappush(participated_task, (-timestamp, sub_task))

        test_task_list = train_match_document['test_task_list']
        for test_id in test_task_list:
            test_match_document = test_mongoDB.search_test_match_document(test_id=test_id)
            test_name = test_match_document['test_name']
            test_description = test_match_document['test_description']
            timestamp = 5
            sub_task = {
                'task_id': None,
                'task_name': None,
                'task_description': None,
                'test_indicator': 'test',
                'test_id': test_id,
                'test_name': test_name,
                'test_description': test_description,
            }
            heapq.heappush(participated_task, (-timestamp, sub_task))
    
    # sub_task with larger timestamp indicates the closer task
    # Put the closer task at front position
    participated_sort_task = []
    while participated_task:
        _, sub_task = heapq.heappop(participated_task)
        participated_sort_task.append(sub_task)
    
    response = {
        'items': participated_sort_task,
        '_meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': math.ceil(len(participated_sort_task) / per_page),
            'total_items': len(participated_sort_task),
        },
    }
    return jsonify(response)

@main.route('/check_sponsor/<string:id>', methods=['POST'])
@token_auth.login_required
def check_sponsor(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data['task_id']
    
    task_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    sponsor_id = task_match_document['sponsor_information']['sponsor_id']

    if sponsor_id == user_id:
        role = "sponsor"
    else:
        role = "assistor"

    response = {
        'role': role
    }
    return jsonify(response)


@main.route('/get_test_task_id_history/<string:id>', methods=['POST'])
@token_auth.login_required
def get_test_history_id(id):

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    task_id = data['task_id']
    train_match_document = train_mongoDB.search_train_match_document(task_id=task_id)
    
    response = {
        "test_id_list": train_match_document['test_task_list']
    }    
    return jsonify(response)