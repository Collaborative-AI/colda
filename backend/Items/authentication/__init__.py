from flask import Blueprint

authentication_bp = Blueprint('authentication', __name__, url_prefix='/auth')
from Items.authentication.auth import token_auth, basic_auth