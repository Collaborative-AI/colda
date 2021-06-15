from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/xx/', methods=['POST'])
@token_auth.login_required
def create_message():

    data = request.get_json()
    print('data',data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'situation' not in data or not data.get('body'):
        return bad_request('Body is required.')

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)
    all_recipient_id = [5,6]

    for recipient_id in all_recipient_id:
        user = User.query.get_or_404(recipient_id)
        if g.current_user == user:
            return bad_request('You cannot send private message to yourself.')

        message = Message()
        message.from_dict(data)

        message.sender_id = g.current_user.id
        message.recipient_id = user.id
        message.rounds = 0
        db.session.add(message)

        # send message notification to the recipient
        user.add_notification('unread situation', user.new_situation())
        db.session.commit()

    response = jsonify(message.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('main.get_message', id=message.id)
    return response
