from flask import Blueprint

main = Blueprint('main', __name__, template_folder='./templates')
# print("-------",__name__)
from . import auth, ceshi, errors, find_assistor, mongoDB, get_notifications, unread_request, unread_match_id, unread_output, unread_situation, users, mongoDB, get_user_history, stop, pending, utils, return_log