from flask import Blueprint

main = Blueprint('main', __name__)

from . import askhelp, auth, ceshi, errors, find_recipient, unread_request, messages, notifications, send_situation, tokens, unread_match_id, unread_output, unread_situation, users, update_all_notifications, get_user_history