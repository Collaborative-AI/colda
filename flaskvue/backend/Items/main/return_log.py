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
from Items.main.apollo_utils import get_log

@main.route('/get_backend_log', methods=['POST'])
@token_auth.login_required
def get_backend_log():

    """
    return log of current task. Must have task_id in data, Might have test_id in data.

    Parameters:
       None

    Returns:
        data - List[List[String, String, List[String]]]. List[String]: ['first log_interval\n', 'second\n', 'third']

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    print('data',data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    # if 'task_id' not in data and 'test_id' not in data:
    #     return bad_request('task_id or test_id is required.')
    # if not data.get('task_id') and not data.get('test_id'):
    #     return bad_request('task_id or test_id is required.')

    task_id = data['task_id']

    records = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == g.current_user.id).all()
    
    res = []
    for record in records:
        if record.test_indicator == "train":
            task_id = record.task_id
            res.append([task_id, "train", get_log(g.current_user.id, task_id)])
        elif record.test_indicator == "test":
            task_id = record.task_id
            test_id = record.test_id
            res.append([test_id, "test", get_log(g.current_user.id, task_id, test_id)])

    return jsonify(res)

