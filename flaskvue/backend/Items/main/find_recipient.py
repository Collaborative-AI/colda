import uuid

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, matched, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/find_recipient/', methods=['POST'])
@token_auth.login_required
def find_recipient():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    
    # hardcode 
    user = User.query.get_or_404(5)
    if g.current_user == user:
        return bad_request('You cannot send private matched to yourself.')

    task_id = uuid.uuid4()
   
    matched = Matched()
    matched.from_dict(data)
    matched.sender = g.current_user
    matched.recipient = user
    matched.task_id = task_id

    sponsor_random_id = uuid.uuid4()
    matched.sponsor_random_id = sponsor_random_id

    recipient_random_id = uuid.uuid4()
    matched.recipient_random_id = recipient_random_id

    db.session.add(matched)

    # send matched notification to the recipient
    user.add_notification('unread request',
                          user.new_request()) 
                        
    db.session.commit()

    dict = {"new_task_id": task_id}
    response = jsonify(dict)
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('main.get_matched', id=matched.id)
    
    return response
