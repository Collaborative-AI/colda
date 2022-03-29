from flask import Blueprint

main_flow_bp = Blueprint('main_flow', __name__, url_prefix='/main_flow')
# auth_bp = Blueprint('authentication', __name__, template_folder='./templates')

from Items.authentication import auth

from Items.main_flow import find_assistor
from Items.main_flow import get_notifications
from Items.main_flow import pending
from Items.main_flow import stop
from Items.main_flow import unread_match_id
from Items.main_flow import unread_output
from Items.main_flow import unread_request
from Items.main_flow import unread_situation