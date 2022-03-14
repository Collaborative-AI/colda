from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from Items import pyMongo
from Items.main import main
# from Items.models import User
from Items.main.errors import error_response
from Items.main.utils import check_password, update_jwt, get_jwt, verify_jwt
# from Items import db

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@main.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():

    """
    Login function (doesnt need token). If the user registered but not confirmed yet, we lead it to the confirmation page.
    If the user finishes the confirmation, we send it a token.

    Parameters:
        None

    Returns:
        msg - String. The string that indicates no confirmation
        token - Dict. Token for user.

    Raises:
        KeyError - raises an exception
    """
    
    if g.current_user['confirm_email'] == False:
        msg = 'not verify email yet'
        return jsonify(msg)
    
    token = get_jwt(g.current_user)
    return jsonify({'token': token})


@basic_auth.verify_password
def verify_password(username, password):

    """
    check the username and password provided by the user

    Parameters:
        username - String.
        password - String

    Returns:
        Boolean

    Raises:
        KeyError - raises an exception
    """

    user = pyMongo.db.User.find_one({'username': username})
    if user is None:
        return False
    g.current_user = user
    return check_password(g.current_user, password)

@basic_auth.error_handler
def basic_auth_error():
    '''Return an error response in case of authentication failure'''
    return error_response(401)

@token_auth.verify_token
def verify_token(token):

    """
    check whether the user request has a token and validity of the token

    Parameters:
       token - object returned by jwt.decode()
       
    Returns:
        Boolean

    Raises:
        KeyError - raises an exception
    """

    g.current_user = verify_jwt(token) if token else None

    # if g.current_user:
    #     # update the last_seen time after visiting any url
    #     g.current_user.update_jwt()
    #     # db.session.commit()
    
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    '''Return an error response if Token Auth authentication fails'''
    return error_response(401)