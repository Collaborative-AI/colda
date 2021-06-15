import uuid
import json

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, matched, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/check_sponsor/', methods=['POST'])
@token_auth.login_required
def check_sponsor():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    task_id = data.get('task_id')

    # Update the Notification
    user = User.query.get_or_404(g.current_user.id)
    last_matched_file_read_time = user.last_matched_file_read_time or datetime(1900, 1, 1)

    record = Matched.query.filter(Matched.recipient_id_pair == g.current_user, Matched.task_id == task_id).all()

    # If can be omitted
    if last_matched_file_read_time > record['match_id_timestamp']:
        user.last_matched_file_read_time = record['match_id_timestamp']

        # submit to database
        db.session.commit()
        
    # check if the current client is the sponsor
    query = Matched.query.filter(Matched.task_id == task_id).first()

    dict = {}
    if query.sponsor_id == g.current_user.id:
        dict = {"sponsor": "true"}
    else:
        dict = {"sponsor": "false"}

    response = jsonify(dict)

    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('main.get_matched', id=matched.id)
    
    return response