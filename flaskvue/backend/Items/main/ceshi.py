import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

# @main.route('/ceshi', methods=['GET'])
@main.route('/ceshi/', methods=['GET'])
@token_auth.login_required
def ceshi():
  print("jinlaile!!!!!")

  zzz = id
  print("aaaa", zzz)
  args = request.args.get("id")
  print("oo", args)
  file_obj = request.get_json()
  print(file_obj)

  # print("zhuanhuan", json.loads(file_obj['file']))

  # file_array = json.loads(file_obj['file'])
  # for i in file_array:
  #   print(i)
  # print("data",request.values.get("Json"))
  # print("data",request.values.get("JSON"))
  # print("data2", request.get_data())
  return "good"