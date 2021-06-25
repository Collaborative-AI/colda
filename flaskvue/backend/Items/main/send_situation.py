from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/send_situation/', methods=['POST'])
@token_auth.login_required
def send_situation():

    data = request.get_json()
    
    if not data:
        return bad_request('You must post JSON data.')
    if 'situation' not in data or not data.get('body'):
        return bad_request('situation is required.')
    if 'initial_rounds' not in data or not data.get('initial_rounds'):
        return bad_request('initial_rounds is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    # json
    situation = data.get('situation')
    
    rounds = data.get('initial_rounds')
    task_id = data.get('task_id')

    # Now hardcode
    # testa: id 4(sponsor), testb: id 5(recipient), testc: id 6(recipient)
    query_of_task = Matched.query.filter(Matched.sponsor_id == g.current_user.id, Matched.task_id == task_id).all()
    sender_random_id = query_of_task[0].sponsor_random_id

    # should be [5,6]
    all_recipient_id = []
    for i in query_of_task:
        all_recipient_id.append(i.recipient_id_pair)

    # send to myself too
    all_recipient_id.append(g.current_user.id)

    for recipient_id in all_recipient_id:
        user = User.query.get_or_404(recipient_id)
        if g.current_user == user:
            return bad_request('You cannot send private message to yourself.')

        message = Message()
        message.from_dict(data)

        message.sender_id = g.current_user.id
        message.recipient_id = user.id
        message.task_id = task_id
        if rounds == "true":
            message.rounds = 0
        else:
            query = Message.query.filter(Message.sender_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()
            message.rounds = query.rounds + 1
        
        # Store the situation
        message.situation = situation
        message.sender_random_id = sender_random_id
        
        db.session.add(message)

        # send message notification to the recipient
        user.add_notification('unread situation', user.new_situation())
        db.session.commit()

    # return response
    response = jsonify(message.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('main.get_message', id=message.id)
    return response
