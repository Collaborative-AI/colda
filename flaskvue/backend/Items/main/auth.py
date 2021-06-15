from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from Items.models import User
from Items.main.errors import error_response
from Items import db

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    '''check the username and password provided by the user'''
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    print("idididid", g.current_user.id)
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    '''Return an error response in case of authentication failure'''
    return error_response(401)

@token_auth.verify_token
def verify_token(token):
    '''check whether the user request has a token, 
       and validity of the token
    '''

    g.current_user = User.verify_jwt(token) if token else None
    if g.current_user:
        # update the last_seen time after visiting any url
        g.current_user.update_jwt()
        db.session.commit()

    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    '''Return an error response if Token Auth authentication fails'''
    return error_response(401)