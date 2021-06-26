import uuid
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/find_recipient', methods=['POST'])
@token_auth.login_required
def find_recipient():

    # find recipient algorithm, return all_recipient_id
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'recipient_id_list' not in data or not data.get('recipient_id_list'):
        return bad_request('recipient_id_list is required.')

    recipient_id_list = json.loads(data['recipient_id_list'])
 
    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)

    # Unique in each task
    task_id = str(uuid.uuid4())

    sponsor_random_id = str(uuid.uuid4())

    for recipient_id in recipient_id_list:
        user = User.query.get_or_404(recipient_id)
      
        matched = Matched()
        matched.sponsor_id = g.current_user.id
        matched.recipient_id_pair = user.id
        matched.task_id = task_id

        matched.sponsor_random_id = sponsor_random_id

        recipient_random_id = str(uuid.uuid4())
        matched.recipient_random_id_pair = recipient_random_id

        db.session.add(matched)

        # send matched notification to the recipient
        user.add_notification('unread request', user.new_request()) 
    
    user = User.query.get_or_404(g.current_user.id)
    matched = Matched()
    matched.sponsor_id = g.current_user.id
    matched.recipient_id_pair = g.current_user.id
    matched.task_id = task_id
    matched.sponsor_random_id = sponsor_random_id
    matched.recipient_random_id_pair = sponsor_random_id
    db.session.add(matched)                        
    
    db.session.commit()

    data = {"task_id": task_id, 'recipient_num': len(recipient_id_list)}
    
    # response.status_code = 201

    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    # response.headers['Location'] = None
    # response.headers['Location'] = url_for('main.get_matched', id=matched.id)
    response = jsonify(data)
    # print("find",response)
    # response.status_code = 204
    
    return response

