from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4

home = Blueprint('home', __name__)
# Same prefix
# account = Blueprint('account', __name__, url_prefix='/admin')

@home.before_request
def bf():
    #g.x = "a"
    print("axxxxx")

@home.route('/index', methods=['GET'])
def index():
    user_info = session.get('user_info', None)
    print(user_info)
    session['user_info']['id'] = "aaaaa"
    return "index"

@home.route('/test')
def test():
    print(session.get('user_info', None))
    return "test"
