from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='./templates')
# auth_bp = Blueprint('authentication', __name__, template_folder='./templates')

from Items.user import users