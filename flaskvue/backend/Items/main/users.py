import re
from operator import itemgetter
from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db
from flask_cors import CORS, cross_origin
# import BluePrint
from Items.main import main
from datetime import datetime

from Items.models import User, Notification, Message
from Items.main.errors import bad_request, error_response
from Items.main.auth import token_auth

@main.route('/users', methods=['POST'])
def create_user():

    data = request.get_json()
    if not data:
      return bad_request('No data. Please import JSON data')

    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'
    if 'password' not in data or not data.get('password', None):
        message['password'] = 'Please provide a valid password.'

    if User.query.filter_by(username=data.get('username', None)).first():
        message['username'] = 'Please use a different username.'
    if User.query.filter_by(email=data.get('email', None)).first():
        message['email'] = 'Please use a different email address.'
    if message:
        return bad_request(message)

    user = User()
    user.from_dict(data, new_user=True)
    print("user",user)
    # Add to database
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('main.get_user', id=user.id)  

    return response

@main.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    '''
      Implement later
    '''
    return "welcome to users!"


@main.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    '''Return a User'''
    user = User.query.get_or_404(id)
    print("id------",id)
    print("user------",user)
    print("g.current", g.current_user)
    if g.current_user == user:
        return jsonify(user.to_dict(include_email=True))
    return jsonify(user.to_dict())

@main.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'username' in data and not data.get('username', None).strip():
        message['username'] = 'Please provide a valid username.'

    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' in data and not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'

    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        message['username'] = 'Please use a different username.'
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        message['email'] = 'Please use a different email address.'

    if message:
        return bad_request(message)

    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


@main.route('/users/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_user(id):
    '''
      Delete a User. Implement Later
    '''
    return "Welcome to Delete!"

@main.route('/users/<int:id>/notifications/', methods=['GET'])
@token_auth.login_required
def get_user_notifications(id):
    '''返回该用户的新通知'''
    user = User.query.get_or_404(id)

    print("user_notification", user)
    if g.current_user != user:
        return error_response(403)
    # 只返回上次看到的通知以来发生的新通知
    # 比如用户在 10:00:00 请求一次该API，在 10:00:10 再次请求该API只会返回 10:00:00 之后产生的新通知
    since = request.args.get('since', 0.0, type=float)
    print("since",since)
    notifications = user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([n.to_dict() for n in notifications])

@main.route('/users/<int:id>/messages-recipients/', methods=['GET'])
@token_auth.login_required
def get_user_messages_recipients(id):
    '''我给哪些用户发过私信，按用户分组，返回我给各用户最后一次发送的私信
    即: 我给 (谁) 最后一次 发了 (什么私信)'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    data = Message.to_collection_dict(
        user.messages_sent.group_by(Message.recipient_id).order_by(Message.timestamp.desc()), page, per_page,
        'main.get_user_messages_recipients', id=id)
        
    # 我给每个用户发的私信，他们有没有未读的
    for item in data['items']:
        # 发给了谁
        recipient = User.query.get(item['recipient']['id'])
        # 总共给他发过多少条
        item['total_count'] = user.messages_sent.filter_by(recipient_id=item['recipient']['id']).count()
        # 他最后一次查看收到的私信的时间
        last_read_time = recipient.last_messages_read_time or datetime(1900, 1, 1)
        # item 是发给他的最后一条，如果最后一条不是新的，肯定就没有啦
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            # 继续获取发给这个用户的私信有几条是新的
            item['new_count'] = user.messages_sent.filter_by(recipient_id=item['recipient']['id']).filter(Message.timestamp > last_read_time).count()
    return jsonify(data)

@main.route('/users/<int:id>/messages-senders/', methods=['GET'])
@token_auth.login_required
def get_user_messages_senders(id):
    '''哪些用户给我发过私信，按用户分组，返回各用户最后一次发送的私信
    即: (谁) 最后一次 给我发了 (什么私信)'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    data = Message.to_collection_dict(
        user.messages_received.group_by(Message.sender_id).order_by(Message.timestamp.desc()), page, per_page,
        'main.get_user_messages_senders', id=id)

    # 这个用户发给我的私信有没有新的
    last_read_time = user.last_messages_read_time or datetime(1900, 1, 1)
    new_items = []  # 最后一条是新的
    not_new_items = []  # 最后一条不是新的
    for item in data['items']:
        # item 是他发的最后一条，如果最后一条不是新的，肯定就没有啦
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            # 继续获取这个用户发的私信有几条是新的
            item['new_count'] = user.messages_received.filter_by(sender_id=item['sender']['id']).filter(Message.timestamp > last_read_time).count()
            new_items.append(item)
        else:
            not_new_items.append(item)
    # 对那些最后一条是新的按 timestamp 正序排序，不然用户更新 last_messages_read_time 会导致时间靠前的全部被标记已读
    new_items = sorted(new_items, key=itemgetter('timestamp'))
    data['items'] = new_items + not_new_items
    return jsonify(data)

@main.route('/users/<int:id>/history-messages/', methods=['GET'])
@token_auth.login_required
def get_user_history_messages(id):
    '''返回我与某个用户(由查询参数 from 获取)之间的所有私信记录'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    from_id = request.args.get('from', type=int)

    if not from_id:  # 必须提供聊天的对方用户的ID
        return bad_request('You must provide the user id of opposite site.')
    # 对方发给我的
    q1 = Message.query.filter(Message.sender_id == from_id, Message.recipient_id == id)
    # 我发给对方的
    q2 = Message.query.filter(Message.sender_id == id, Message.recipient_id == from_id)
    # 按时间正序排列构成完整的对话时间线
    history_messages = q1.union(q2).order_by(Message.timestamp)
    data = Message.to_collection_dict(history_messages, page, per_page, 'main.get_user_history_messages', id=id)
    # 现在这一页的 data['items'] 包含对方发给我和我发给对方的
    # 需要创建一个新列表，只包含对方发给我的，用来查看哪些私信是新的
    recived_messages = [item for item in data['items'] if item['sender']['id'] != id]
    sent_messages = [item for item in data['items'] if item['sender']['id'] == id]
    # 然后，标记哪些私信是新的
    last_read_time = user.last_messages_read_time or datetime(1900, 1, 1)
    new_count = 0
    for item in recived_messages:
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            new_count += 1
    if new_count > 0:
        # 更新 last_messages_read_time 属性值为收到的私信列表最后一条(最近的)的时间
        user.last_messages_read_time = recived_messages[-1]['timestamp']
        db.session.commit()  # 先提交数据库，这样 user.new_recived_messages() 才会变化
        # 更新用户的新私信通知的计数
        user.add_notification('unread_messages_count', user.new_recived_messages())
        db.session.commit()
    # 最后，重新组合 data['items']，因为收到的新私信添加了 is_new 标记
    messages = recived_messages + sent_messages
    messages.sort(key=data['items'].index)  # 保持 messages 列表元素的顺序跟 data['items'] 一样
    data['items'] = messages
    return jsonify(data)