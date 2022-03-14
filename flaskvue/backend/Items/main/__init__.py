from flask import Blueprint

main = Blueprint('main', __name__, template_folder='./templates')
# print("-------",__name__)
from . import auth, ceshi, errors, find_assistor, unread_request, messages, unread_match_id, unread_output, unread_situation, users, update_all_notifications, get_user_history, stop, pending, utils, return_log