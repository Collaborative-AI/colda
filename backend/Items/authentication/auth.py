import jwt

from flask import g, current_app
from flask.json import jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from bson.json_util import loads, dumps

from datetime import datetime, timedelta

from Items import pyMongo
from Items.authentication import authentication_bp
from Items.exception import error_response
from Items.utils import check_password

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@authentication_bp.route('/tokens', methods=['POST'])
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
    
    token = jwt_manipulation.get_jwt(g.current_user)
    # print('token is', type(token), token)
    # print('token is 1', token.decode("utf-8"))
    # print('token is 2', dumps({'token': token.decode()}))
    # print('token is 3', jsonify(dumps({'token': token.decode()})))
    if isinstance(token, str):
        response = {
            'token': token
        }
    else:
        response = {
            'token': token.decode("utf-8")
        }
    return jsonify(response)
    # return jsonify({'token': token.decode("utf-8")})

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
    print('password')
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

    print('token is!!!!!', token)

    g.current_user, token_payload = jwt_manipulation.verify_jwt(token) if token else None

    if g.current_user:
        new_token = jwt_manipulation.update_jwt(g.current_user, token_payload)
        g.current_user['new_token'] = new_token
    
    return g.current_user is not None

@token_auth.error_handler
def token_auth_error():
    '''Return an error response if Token Auth authentication fails'''
    return error_response(401)

class jwt_manipulation:

    @classmethod
    def update_jwt(cls, user, token_payload, expires_in=5000):

        token_payload_expiration_time = token_payload.get('exp')

        # float
        current_time = datetime.utcnow().timestamp()
        expiration_time = (datetime.utcnow() + timedelta(seconds=expires_in)).timestamp()

        time_diff = abs(token_payload_expiration_time - current_time)
 
        # if the difference of time is greater than 10 mins, we dont update 
        # the token
        if time_diff > 1000:
            return None
        
        token_payload = {
            'user_id': user['user_id'],
            'user_name': user['name'] if 'name' in user else user['username'],
            'authority_level': user['authority_level'] if 'authority_level' in user else 'user',
            # expiration time
            'exp': expiration_time,
            # create time
            'iat': current_time
        }
        # return jwt.encode(
        #     token_payload,
        #     current_app.config['SECRET_KEY'],
        #     algorithm='HS256').decode('utf-8')
        return jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

    @classmethod
    def get_jwt(cls, user, expires_in=5000):
        current_time = datetime.utcnow().timestamp()
        expiration_time = (datetime.utcnow() + timedelta(seconds=expires_in)).timestamp()

        # float
        token_payload = {
            'user_id': user['user_id'],
            'user_name': user['name'] if 'name' in user else user['username'],
            'authority_level': user['authority_level'] if 'authority_level' in user else 'user',
            # expiration time
            'exp': expiration_time,
            # create time
            'iat': current_time
        }

        # print('type', type(jwt))
        # return jwt.encode(
        #     token_payload,
        #     current_app.config['SECRET_KEY'],
        #     algorithm='HS256').decode('utf-8')
        # a = jwt.encode(
        #     token_payload,
        #     current_app.config['SECRET_KEY'],
        #     algorithm='HS256')
        # print('aaaaaa', a, type(a))

        return jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

    @classmethod
    def verify_jwt(cls, token):
        try:
            token_payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # If the Token expires or is modified by someone, the signature verification will also fail.
            return None, None
        
        user_id = token_payload.get('user_id')
        user_document = pyMongo.db.User.find_one({'user_id': user_id})
        return user_document, token_payload
