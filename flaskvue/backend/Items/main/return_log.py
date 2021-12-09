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

@main.route('/get_task_id_log', methods=['POST'])
@token_auth.login_required
def get_task_id_log():

    """
    return log of current task. Must have task_id in data, Might have test_id in data.

    Parameters:
       None

    Returns:
        data - List[String]. ['first log_interval\n', 'second\n', 'third']

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'task_id' not in data and 'test_id' not in data:
        return bad_request('task_id or test_id is required.')
    if not data.get('task_id') and not data.get('test_id'):
        return bad_request('task_id or test_id is required.')

    task_id = data['task_id']

    if "task_id" in data:
        return jsonify(get_log(g.current_user.id, task_id))

    elif "test_id" in data:
        test_id = data['test_id']
        return jsonify(get_log(g.current_user.id, task_id, test_id))