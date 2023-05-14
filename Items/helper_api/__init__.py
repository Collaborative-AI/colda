from flask import Blueprint

helper_api_bp = Blueprint('helper_api', __name__, url_prefix='/helper_api')
# auth_bp = Blueprint('authentication', __name__, template_folder='./templates')

from Items.helper_api import ceshi
from Items.helper_api import get_user_history
from Items.helper_api import return_log