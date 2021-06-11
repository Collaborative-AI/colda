from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from Items import db

# import BluePrint
from Items.main import main

from Items.models import User, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/ceshi/', methods=['POST'])
@token_auth.login_required
def ceshi():
  print("jinlaile!!!!!")
  file_obj = request.files['file']
  print(file_obj)

  return "good"