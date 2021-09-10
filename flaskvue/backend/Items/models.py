# -*- coding: utf-8 -*-
from flask.json import jsonify
import jwt
import json

from hashlib import md5
from Items import db
from time import time
from flask import url_for, current_app
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
'''
    DataBase models
'''
class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        # 如果当前没有任何资源时，或者前端请求的 page 越界时，都会抛出 404 错误
        # 由 @bp.app_errorhandler(404) 自动处理，即响应 JSON 数据：{ error: "Not Found" }
        resources = query.paginate(page, per_page, False)
        print("resources.items-----------------------------------",resources.items)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            # '_links': {
            #     'self': url_for(endpoint, page=page, per_page=per_page,
            #                     **kwargs),
            #     'next': url_for(endpoint, page=page + 1, per_page=per_page,
            #                     **kwargs) if resources.has_next else None,
            #     'prev': url_for(endpoint, page=page - 1, per_page=per_page,
            #                     **kwargs) if resources.has_prev else None
            # }
        }
        return data

class User(PaginatedAPIMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    last_requests_read_time = db.Column(db.DateTime)

    last_matched_file_read_time = db.Column(db.DateTime)

    last_situation_read_time = db.Column(db.DateTime)

    last_output_read_time = db.Column(db.DateTime)

    last_test_requests_read_time = db.Column(db.DateTime)

    last_test_matched_file_read_time = db.Column(db.DateTime)

    last_test_output_read_time = db.Column(db.DateTime)

    last_messages_read_time = db.Column(db.DateTime)

    # last_stop_read_time = db.Column(db.DateTime)

    # Message User sent
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id',
                                    backref='sender', lazy='dynamic',
                                    cascade='all, delete-orphan')
    # Message User received
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.assistor_id',
                                        backref='assistor', lazy='dynamic',
                                        cascade='all, delete-orphan')
    
    # Message User sent
    # match_sponsor = db.relationship('Matched', foreign_keys='Matched.sponsor_id',
    #                                 backref='matchsponsor', lazy='dynamic',
    #                                 cascade='all, delete-orphan')
    # # Message User received
    # match_assistor = db.relationship('Matched',
    #                                     foreign_keys='Matched.assistor_id_pair',
    #                                     backref='matchassistor', lazy='dynamic',
    #                                     cascade='all, delete-orphan')

    # Notification
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        '''头像'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # change User Object to dictionary, the dictionary would be changed to 
    # Json later
    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'about_me': self.about_me,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            '_links': {
                'self': url_for('main.get_user', id=self.id),
                'avatar': self.avatar(128),
            }
        }
        
        if include_email:
            data['email'] = self.email
        return data

    # change Json to User Object
    def from_dict(self, data, new_user=False):
        for key in ['username','email', 'name', 'about_me', 'location']:
            if key in data:
                setattr(self, key, data[key])
        if new_user and 'password' in data:
            self.set_password(data['password'])
    
    def add_notification(self, name, data):
        '''给用户实例对象增加通知'''
        # 如果具有相同名称的通知已存在，则先删除该通知
        self.notifications.filter_by(name=name).delete()

        task_id_list = data[0]
        sender_random_id_list = data[1]

        # print("task_id_list", task_id_list, json.dumps(task_id_list))
        # print(json.loads(json.dumps(task_id_list)))
        # print("sender", sender_random_id_list)

        count = len(task_id_list)

        # 为用户添加通知，写入数据库
        n = Notification(name=name, payload_json=json.dumps(count), user=self,
            sender_random_id_list=json.dumps(sender_random_id_list),task_id_list=json.dumps(task_id_list))

        db.session.add(n)
        return n
        
    def new_recived_messages(self):
        '''用户未读的私信计数'''
        last_read_time = self.last_messages_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(assistor=self).filter(
            Message.timestamp > last_read_time).count()

    def stop_train_task(self, task_id, most_recent_round):

        return [[task_id], [most_recent_round]]

    def new_request(self):
        '''用户未读的请求数'''
        last_request_time = self.last_requests_read_time or datetime(1900, 1, 1)

        query = Matched.query.filter_by(assistor_id_pair=self.id).filter(
            Matched.request_timestamp > last_request_time, Matched.test_indicator == "train").all()
        
        task_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            task_id_list.append(query[i].task_id)

            # sender must be sponsor
            sender_random_id_list.append(query[i].sponsor_random_id)

        return [task_id_list, sender_random_id_list]

    def new_match_id(self):
        '''用户未读的match完的id'''
        last_match_time = self.last_matched_file_read_time or datetime(1900, 1, 1)

        query = Matched.query.filter_by(assistor_id_pair=self.id).filter(
            Matched.match_id_timestamp > last_match_time, Matched.test_indicator == "train").all()

        task_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            task_id_list.append(query[i].task_id)

            # sender must be sponsor
            sender_random_id_list.append(query[i].sponsor_random_id)

        return [task_id_list, sender_random_id_list]

    def new_situation(self):
        '''用户未读的situation'''
        last_situation_time = self.last_situation_read_time or datetime(1900, 1, 1)
        query = Message.query.filter_by(assistor_id=self.id).filter(
            Message.situation_timestamp > last_situation_time, Message.test_indicator == "train").all()

        # print("last_situation_time",last_situation_time)
        # if self.id == 1:
        #     for i in query:
        #         print(i.situation_timestamp)

        task_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            if not query[i].output:
                task_id_list.append(query[i].task_id)

                # sender must be sponsor
                sender_random_id_list.append(query[i].sender_random_id)

        return [task_id_list, sender_random_id_list]
    
    def new_output(self):
        '''用户未读的output'''
        last_output_time = self.last_output_read_time or datetime(1900, 1, 1)
        query = Message.query.filter_by(assistor_id=self.id).filter(
            Message.output_timestamp > last_output_time, Message.test_indicator == "train").all()
        
        print("new_output---------------------",self.id)
        task_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            if query[i].output:
                task_id_list.append(query[i].task_id)

                # sender must be sponsor
                sender_random_id_list.append(query[i].sender_random_id)

        return [task_id_list, sender_random_id_list]

    def new_test_request(self):

        last_test_request_time = self.last_test_requests_read_time or datetime(1900, 1, 1)

        query = Matched.query.filter_by(assistor_id_pair=self.id).filter(
            Matched.request_timestamp > last_test_request_time, Matched.test_indicator == "test").all()
        
        test_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            test_id_list.append(query[i].test_id)

            # sender must be sponsor
            sender_random_id_list.append(query[i].sponsor_random_id)

        return [test_id_list, sender_random_id_list]

    def new_test_match_id(self):
        last_test_match_time = self.last_test_matched_file_read_time or datetime(1900, 1, 1)

        query = Matched.query.filter_by(assistor_id_pair=self.id).filter(
            Matched.match_id_timestamp > last_test_match_time, Matched.test_indicator == "test").all()

        test_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            test_id_list.append(query[i].test_id)

            # sender must be sponsor
            sender_random_id_list.append(query[i].sponsor_random_id)

        return [test_id_list, sender_random_id_list]

    def new_test_output(self):
        last_test_output_time = self.last_test_output_read_time or datetime(1900, 1, 1)
        query = Message.query.filter_by(assistor_id=self.id).filter(
            Message.output_timestamp > last_test_output_time, Message.test_indicator == "test").all()
        
        print("new_output---------------------",self.id)
        test_id_list = []
        sender_random_id_list = []
        for i in range(len(query)):
            if query[i].output:
                test_id_list.append(query[i].test_id)

                # sender must be sponsor
                sender_random_id_list.append(query[i].sender_random_id)

        return [test_id_list, sender_random_id_list]


    def update_jwt(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def get_jwt(self, expires_in=50000):
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'user_name': self.name if self.name else self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            return None
        return User.query.get(payload.get('user_id'))


class Message(PaginatedAPIMixin, db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    situation_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    output_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sender_random_id = db.Column(db.String(120))
    assistor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    task_id = db.Column(db.String(120), index=True)
    rounds = db.Column(db.Integer)
    situation = db.Column(db.Text)
    output = db.Column(db.Text, nullable=True)
    test_indicator = db.Column(db.String(10))
    test_id = db.Column(db.String(120), index=True)
    Sponsor_situation_training_done = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Message {}>'.format(self.id)

    # change User Object to dictionary, the dictionary would be changed to 
    # Json later
    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'sender': self.sender.to_dict(),
            'assistor': self.assistor.to_dict(),
            'timestamp': self.timestamp,
            'situation_timestamp': self.situation_timestamp,
            'output_timestamp': self.output_timestamp,
            'task_id': self.task_id,
            'rounds': self.rounds, 
        } 
        return data
    
    # change Json to User Object
    def from_dict(self, data):
        for key in ['body', 'timestamp']:
            if key in data:
                setattr(self, key, data[key])


class Notification(PaginatedAPIMixin, db.Model):  
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # category of notification
    name = db.Column(db.String(128), index=True)
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)
    sender_random_id_list = db.Column(db.Text)
    task_id_list = db.Column(db.Text)

    # sender_random_id = db.Column(db.Integer)
    # task_id = db.Column(db.String(120), index=True)
    # assistor_num = db.Column(db.Integer)

    def __repr__(self):
        return '<Notification {}>'.format(self.id)

    def get_data(self):
        return json.loads(str(self.payload_json))

    def get_sender_random_id_list(self):
        print("self.sender_random_id_list", self.sender_random_id_list)
        if not self.sender_random_id_list:
            return []
        return json.loads(str(self.sender_random_id_list))
    
    def get_task_id_list(self):
        print("self.task_id_list", self.task_id_list)
        if not self.task_id_list:
            return []
        return json.loads(str(self.task_id_list))

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'name': self.user.name,
            },
            'timestamp': self.timestamp,
            'payload': self.get_data(),
            'sender_random_id_list': self.get_sender_random_id_list(),
            'task_id_list': self.get_task_id_list(),
            # 'sender_random_id': self.sender_random_id,
            # 'task_id': self.task_id,
            # 'assistor_num': self.assistor_num,
            # '_links': {
            #     'self': url_for('main.get_notification', id=self.id),
            #     'user_url': url_for('main.get_user', id=self.user_id)
            # }
        }
        return data

    def from_dict(self, data):
        for key in ['body', 'timestamp']:
            if key in data:
                setattr(self, key, data[key])

class Matched(PaginatedAPIMixin, db.Model):  
    __tablename__ = 'matched'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(120), index=True)
    
    request_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    match_id_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # sponsor_id = db.Column(db.String(120), db.ForeignKey('users.id'))
    # assistor_id_pair = db.Column(db.String(120), db.ForeignKey('users.id'))

    sponsor_id = db.Column(db.Integer)
    assistor_id_pair = db.Column(db.Integer)

    Matched_id_file =  db.Column(db.Text, nullable=True)
    matched_done = db.Column(db.Integer, nullable=True)
    Assistor_matched_written_done = db.Column(db.String(120), nullable=True)
    sponsor_random_id = db.Column(db.String(120))
    assistor_random_id_pair = db.Column(db.String(120))

    test_indicator = db.Column(db.String(10))
    test_id = db.Column(db.String(120), index=True)
    
    Terminate = db.Column(db.String(120))


    def __repr__(self):
        return '<Match {}>'.format(self.id)

    def get_data(self):
        return json.loads(str(self.payload_json))

    def to_dict(self):
        data = {
            'id': self.id,
            'task_id': self.task_id,
            'request_timestamp': self.request_timestamp,
            'match_id_timestamp': self.match_id_timestamp,
            'sponsor_random_id': self.sponsor_random_id,
            'assistor_random_id_pair': self.assistor_random_id_pair,
            # '_links': {
            #     'self': url_for('main.get_notification', id=self.id),
            #     'user_url': url_for('main.get_user', id=self.user_id)
            # }
        }
        return data

    def from_dict(self, data):
        for key in ['file_to_match', 'timestamp']:
            if key in data:
                setattr(self, key, data[key])