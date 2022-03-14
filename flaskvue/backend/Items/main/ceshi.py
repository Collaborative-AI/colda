import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
# import py
from Items import db
from Items import pyMongo

# import BluePrint
from Items.main import main

from Items.models import User, Message, Matched, Notification, Stop, Pending
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

# @main.route('/ceshi', methods=['GET'])
@main.route('/changshi', methods=['GET'])
def changshi():
  print("NIHAO!!!!!")

#   zzz = id
#   print("aaaa", zzz)
#   args = request.args.get("id")
#   print("oo", args)
#   file_obj = request.get_json()
#   print(file_obj)

#   print("zhuanhuan", json.loads(file_obj['file']))

#   file_array = json.loads(file_obj['file'])
#   for i in file_array:
#     print(i)
#   print("data",request.values.get("Json"))
#   print("data",request.values.get("JSON"))
#   print("data2", request.get_data())
  return "good,NIHAO"

# @main.route('/ceshi', methods=['GET'])
@main.route('/changshi2', methods=['GET'])
def changshi2():
  print("wori")

  return "best,NIHAO"

@main.route('/ceshi/<string:ID>/<int:value>', methods=['GET'])
@token_auth.login_required
def ceshi(ID,value):
  print("jinlaile!!!!!")

  # zzz = id
  # print("aaaa", zzz)
  # args = request.args.get("ID")
  # print("ARGS",args)
  print("ID", ID)
  print("value", value)
  # print("oo", args)
  # file_obj = request.get_json()
  # print("FILE", file_obj)

  # print("zhuanhuan", json.loads(file_obj['file']))

  # file_array = json.loads(file_obj['file'])
  # for i in file_array:
  #   print(i)
  print("data",request.values.get("Json"))
  print("data",request.values.get("JSON"))
  print("data2", request.get_data())
  return "good"

@main.route('/create_unittest_user/', methods=['POST'])
def create_unittest_user():
    data = request.get_json()
    username = data['username']

    if User.query.filter_by(username = username).first():
        return 'repetition'

    user = User()
    user.from_dict(data, new_user=True)
    user.confirmed = 'true'
    db.session.add(user)
    db.session.commit()

    return 'gg'

# @main.route('/ceshi', methods=['GET'])
@main.route('/delete_unittest_db/', methods=['GET'])
def delete_unittest_db():
  
  # Message, Matched, Notification
  queries = Matched.query.all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  Users = User.query.all()
  for row in Users:
      db.session.delete(row)
      db.session.commit()

  return "gg"

# @main.route('/ceshi', methods=['GET'])
@main.route('/delete_all_rows/', methods=['GET'])
@token_auth.login_required
def delete_all_rows():
  
  # Message, Matched, Notification
  queries = Matched.query.all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  return "done"

@main.route('/delete_test_rows/', methods=['GET'])
@token_auth.login_required
def delete_test_rows():
  
  # Message, Matched, Notification
  queries = Matched.query.filter(Matched.test_indicator == "test").all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.filter(Message.test_indicator == "test").all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Stops = Stop.query.all()
  for row in Stops:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  return "done"


@main.route('/ceshi_mongo/', methods=['POST', 'GET'])
def ceshi_mongo():
    res = pyMongo.db.user.find_one_or_404({"name": "Ada Lovelace"})
    print('res', res)
    collections = pyMongo.db.list_collection_names()
    print('collections_1', collections)
    res = pyMongo.db.shuaiqi.insert_one({'x': 1})
    print('res1', res)
    collections = pyMongo.db.list_collection_names()
    print('collections_2', collections)

    user = pyMongo.db.User.find_one({'username': 'qq'})
    print('user', user)

    pyMongo.db.User.insert_one({'username': 'qq'})
    user = pyMongo.db.User.find_one({'username': 'qq'})
    user_id = user['_id']
    print('user2', user)
    print(user['_id'], type(user['_id']))
    print('hhh', str(user['_id']), type(str(user['_id'])))

    user = pyMongo.db.User.find_one({'_id': str(user_id)})
    print('user3', user)
    user = pyMongo.db.User.find_one({'_id': user_id})
    print('user4', user)

    record = {
        'username': 'qia', 
        "information": [],
    }
    pyMongo.db.User.insert_one(record)

    res = pyMongo.db.User.find_one({'username': 'qia'})
    print('hhh', res)

    pyMongo.db.User.update_one({'username': 'qia'}, {'$set':{'isTerminate': True}})
    res = pyMongo.db.User.find_one({'username': 'qia'})
    print('hhh6', res)

    isTerminate = res['isTerminate']
    print('type', type(isTerminate))

    return 'gg'
