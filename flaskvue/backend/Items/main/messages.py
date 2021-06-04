from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/messages/', methods=['POST'])
@token_auth.login_required
def create_message():
    '''Send Request to other users'''
    print("aaa")
    
    data = request.get_json()
    print('data',data)
    if not data:
        return bad_request('You must post JSON data.')
    if 'body' not in data or not data.get('body'):
        return bad_request('Body is required.')
    if 'recipient_id' not in data or not data.get('recipient_id'):
        return bad_request('Recipient id is required.')

    user = User.query.get_or_404(int(data.get('recipient_id')))
    if g.current_user == user:
        return bad_request('You cannot send private message to yourself.')

    message = Message()
    message.from_dict(data)
    print("message1-----", message)
    message.sender = g.current_user
    message.recipient = user
    print("message2----", message)
    db.session.add(message)

    # 给私信接收者发送新私信通知
    user.add_notification('unread_messages_count',
                          user.new_recived_messages())
    db.session.commit()
    response = jsonify(message.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('main.get_message', id=message.id)
    return response


@main.route('/messages/', methods=['GET'])
@token_auth.login_required
def get_messages():
    '''
        Implement later
    '''
    return "welcome to get_messages!"


@main.route('/messages/<int:id>', methods=['GET'])
@token_auth.login_required
def get_message(id):
    '''返回单个私信'''
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict())

@main.route('/messages/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_message(id):
    '''修改单个私信'''
    message = Message.query.get_or_404(id)
    if g.current_user != message.sender:
        return error_response(403)
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'body' not in data or not data.get('body'):
        return bad_request('Body is required.')
    message.from_dict(data)
    db.session.commit()
    return jsonify(message.to_dict())


@main.route('/messages/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_message(id):
    '''删除单个私信'''
    message = Message.query.get_or_404(id)
    if g.current_user != message.sender:
        return error_response(403)
    db.session.delete(message)
    # 给私信接收者发送新私信通知(需要自动减1)
    message.recipient.add_notification('unread_messages_count',
                                       message.recipient.new_recived_messages())
    db.session.commit()
    return '', 204
