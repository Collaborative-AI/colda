import uuid
import json
import time

from sqlalchemy import update
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Notification, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/match_sponsor_id/', methods=['POST'])
@token_auth.login_required
def match_sponsor_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')  
    if 'file' not in data or not data.get('file'):
        return bad_request('File is required.')
    
    data_array = json.loads(data['file'])
    task_id = data.get('task_id')

    response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id).all()

    # while loop, wait for all recipients update match id file
    match_ID_recipient_upload = 0
    while match_ID_recipient_upload < len(response):
        response = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id).all()

        match_ID_recipient_upload = 0
        for row in response:
            if row.Matched_id_file:
                match_ID_recipient_upload += 1
        time.sleep(2)

    # count the distinct id in the Sponsor ID file
    data_array_id = {}
    for i in range(1,len(data_array)-1):
        if data_array[i][0] not in data_array_id:
            data_array_id[data_array[i][0]] = 1

    # match id file
    for row in response:

        same_id = {}
        db_array = json.loads(row.Matched_id_file)
        
        # previous stored id
        for i in range(len(db_array)):
            if db_array[i] in data_array_id:
                same_id[db_array[i]] = 1

        # Store the key, dont need the value
        same_id_keys = []
        for i in same_id.keys():
            same_id_keys.append(i)
        
        # update the db
        Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == row.recipient_id_pair).update({"Matched_id_file": json.dumps(same_id_keys), "match_id_timestamp": datetime.utcnow()})
        db.session.commit()

        # send matched notification to the recipient
        user = User.query.get_or_404(row.recipient_id_pair)
        user.add_notification('unread match id', user.new_match_id()) 

    # when all match_id match, add notification to sponsor
    user = User.query.get_or_404(g.current_user.id)
    user.add_notification('unread match id', user.new_match_id()) 

    dict = {"stored": "sponsor stores match id file successfully", "task_id": task_id}
    response = jsonify(dict)

    return response



@main.route('/match_recipient_id/', methods=['POST'])
@token_auth.login_required
def match_recipient_id():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    if 'file' not in data or not data.get('file'):
        return bad_request('file is required.')

    task_id = data.get('task_id')

    # Update last_requests_read_time
    user = User.query.get_or_404(g.current_user.id)
    last_requests_read_time = user.last_requests_read_time or datetime(1900, 1, 1)
    # one record for a recipient_id_pair per task
    record = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id).all()

    # If can be omitted
    if record[0].request_timestamp > last_requests_read_time:
        user.last_requests_read_time = record[0].request_timestamp

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread request', user.new_request()) 
        db.session.commit()

    data_array = json.loads(data['file'])

    # extract ID
    data_array_id = []
    for i in range(1,len(data_array)-1):
        data_array_id.append(data_array[i][0])

    # response is a row
    response = Matched.query.filter(Matched.recipient_id_pair == g.current_user.id, Matched.task_id == task_id)

    # update the db
    Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == g.current_user.id).update({"Matched_id_file": json.dumps(data_array_id)})
    db.session.commit()
                        
    dict = {"stored": "recipient match id stored", "task_id": task_id}
    response = jsonify(dict)
    
    return response