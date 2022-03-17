# -*- coding: utf-8 -*-
import json
from typing import Match

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from operator import itemgetter
from Items import db
# import BluePrint
from Items.main import main
# from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth
from Items.main.utils import log, generate_msg

@main.route('/get_user_history/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user_history(id):

    print("a")
    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    user = User.query.get_or_404(g.current_user.id)
    if g.current_user != user:
        return error_response(403)

    print("b")
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)

    print("c")
    
    participated_task = Matched.to_collection_dict(
        Matched.query.filter(Matched.assistor_id_pair == g.current_user.id).order_by(Matched.match_id_timestamp.desc()), page, per_page, 
          'None', id=g.current_user.id)

    sorted_items = sorted(participated_task['items'], key=itemgetter('match_id_timestamp'), reverse=True)
    participated_task['items'] = sorted_items

    print("d")
    return jsonify(participated_task)

@main.route('/check_sponsor/<int:id>', methods=['POST'])
@token_auth.login_required
def check_sponsor(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data['task_id']
  
    query = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id, Matched.test_indicator == "train").first()
    
    data = ""
    print("))))))))))))))))%", query.sponsor_id, g.current_user.id)
    if int(query.sponsor_id) == g.current_user.id:
        print("vvvvvvvvvvvvv")
        data = "sponsor"
    else:
        print("yyyyyyyyyy")
        data = "assistor"

    dict = {"result": data}
    return jsonify(dict)


@main.route('/get_test_history_id/<int:id>', methods=['POST'])
@token_auth.login_required
def get_test_history_id(id):

    # find assistor algorithm, return all_assistor_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    task_id = data['task_id']
    train_match_document = pyMongo.db.Train_Match.find_one({'task_id': task_id})
    
    data = {"test_id_list": train_match_document['test_task_list']}
    print("test_id_list", data)
    response = jsonify(data)
    
    return response