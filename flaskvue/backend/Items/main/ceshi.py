import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

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