# -*- coding: utf-8 -*-
import re
from bson import ObjectId
from bson.json_util import loads, dumps
from werkzeug.security import generate_password_hash, check_password_hash

from flask.json import jsonify
from flask.helpers import url_for
from flask import request, g, render_template, flash

# from Items import db
from Items import pyMongo
from Items.user import user_bp
from Items.exception import bad_request, error_response
from Items.authentication import token_auth, basic_auth
from Items.utils import obtain_user_id_from_token
from Items.utils import log, generate_msg, validate_password, send_email, generate_confirmation_token, confirm_token
from Items.utils import generate_password, verify_token_user_id_and_function_caller_id
from Items.mongoDB import mongoDB

@user_bp.route('/users', methods=['POST'])
def create_user():

    """
    Register new user

    Parameters:
        username - String. The id of task
        email - String. The matching id file sent by sponsor
        password - String.

    Returns:
        data - Dict. 

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
      return bad_request('No data. Please import JSON data')

    message = {}
    if 'username' not in data or not data.get('username', None) or (' ' in data.get('username')):
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)) or (' ' in data.get('email')):
        message['email'] = 'Please provide a valid email address.'
    if 'password' not in data or not data.get('password', None) or (' ' in data.get('password')):
        message['password'] = 'Please provide a valid password.'
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password_hash = generate_password(password)

    user_document = pyMongo.db.User.find_one({'username': username})
    if user_document:
        message['username'] = 'Please use a different username.'
    # user_document = pyMongo.db.User.find_one({'email': email})
    # if user_document:
    #     message['email'] = 'Please use a different email address.'
    
    validate_password_indicator, return_message = validate_password(password)
    print('register', validate_password_indicator, return_message)
    if not validate_password_indicator:
        message['password'] = return_message
    if message:
        return bad_request(message)
    
    newObjectId = ObjectId()
    user_document = {
        '_id': newObjectId,
        'user_id': str(newObjectId),
        'username': username,
        'email': email,
        'password_hash': password_hash,
        'name': None,
        'location': None,
        'about_me': None,
        'authority_level': 'user',
        'confirm_email': False,
        'participated_train_task': {},
    }
    pyMongo.db.User.insert_one(user_document)

    token = generate_confirmation_token(email)
    confirm_url = url_for('user.confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(email, subject, html)

    return_dict = {}
    return_dict['token'] = token
    return_dict['message'] = 'create successfully'
    response = jsonify(return_dict)
    response.status_code = 201
    return response

@user_bp.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):

    """
    Confirm the link in the email 

    Parameters:
       token - instance of URLSafeTimedSerializer.
       
    Returns:
        msg - String. Depends on different situation

    Raises:
        KeyError - raises an exception
    """

    email = confirm_token(token)
    user = pyMongo.db.User.find_one({'email': email})

    msg = ''
    if user:
        if user['confirm_email'] == False:
            if user['email'] == email:
                pyMongo.db.User.update_one({'email': email}, {'$set':{
                    'confirm_email': True
                }})
                msg = 'You have confirmed your account. Thanks!'
            else:
                msg = 'The confirmation link is invalid or has expired.'
        else:
            msg = 'Account already confirmed. Please login.'
    else:
        msg = 'The confirmation link is invalid or has expired.'

    return render_template('confirm.html', msg=msg)

@user_bp.route('/resend/', methods=['POST'])
def resend():
    
    """
    Resend the email link

    Parameters:
        username - String.
       
    Returns:
        'Resend successfully!'

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'username' not in data or not data.get('username'):
        return bad_request('username is required.')

    username = data.get('username')

    user_document = mongoDB.search_user_document(user_id=None, username=username)
    email = user_document['email']

    token = generate_confirmation_token(email)
    confirm_url = url_for('user.confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(email, subject, html)

    response = {
        'message': 'Resend successfully!'
    }
    return jsonify(response)

@user_bp.route('/forgot', methods=['POST'])
def forgot():
    
    """
    Reset the password

    Parameters:
        username - String.
        email - String.
       
    Returns:
        'A password reset email has been sent via email.'

    Raises:
        KeyError - raises an exception
    """

    data = request.get_json()
    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'
    
    username = data.get('username')
    email = data.get('email')

    user_document = mongoDB.search_pending_document(user_id=None, username=username)
    if not user_document:
        message['username'] = 'Please type in the correct username.'
    if user_document['email'] != email:
        message['email'] = 'Please type in the correct username and email'
        message['username'] = 'Please type in the correct username and email'
    if message:
        return bad_request(message)

    token = generate_confirmation_token(email)
    reset_url = url_for('user.forgot_new', token=token, _external=True)
    html = render_template('reset.html',
                            username=username,
                            reset_url=reset_url)
    subject = "Reset your password"
    send_email(email, subject, html)

    response = {
        'message': 'A password reset email has been sent via email.'
    }
    return jsonify(response)


@user_bp.route('/forgot/new/<token>', methods=['GET', 'POST'])
def forgot_new(token):

    """
    backend function to handle resetting the password

    Parameters:
        username - String.
        email - String.
       
    Returns:
        'A password reset email has been sent via email.'

    Raises:
        KeyError - raises an exception
    """

    if request.method == 'POST':
        # would have a "\" append in the end
        token = request.form['token'][:-1]

    email = confirm_token(token)
    if email == False:
        flash('Token has expired')
        return 'Token has expired'

    # form = ChangePasswordForm()
    # if form.validate_on_submit():
    user_document = pyMongo.db.User.find_one({'email': email})
    if not user_document:
        flash('Cannot Find the User according to email')
        return 'Cannot Find the User according to email'
    
    if request.method == 'POST':
 
        password = request.form['newPassword']

        validate_password_indicator, return_message = validate_password(password)
        if not validate_password_indicator:
            msg = ('New password must follow the following instructions:\n' + ' At least 8 characters. At most 25 characters\n'
                + 'A mixture of both uppercase and lowercase letters\n' + 'A mixture of letters and numbers' + 'Inclusion of at least one special character, e.g., ! @')
            confirm_url = url_for('user.forgot_new', token=token, msg=msg, _external=True)
            return render_template('forgot_new.html', confirm_url=confirm_url)

 
        user_password_hash = generate_password_hash(password)
        pyMongo.db.User.update_one({'email': email}, {'$set':{
            'password_hash': user_password_hash
        }})

        flash('Password successfully changed.')
        return 'Password successfully changed.'
    else:
        print('123token', token)
        msg = 'Hello ' + user_document['username']
        confirm_url = url_for('user.forgot_new', token=token, _external=True)
        print("/forgot/new/<token>_confirm_url", confirm_url)
        return render_template('forgot_new.html', confirm_url=confirm_url, msg=msg, token=token)

@user_bp.route('/users/<string:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):

    """
    Get information of user itself

    Parameters:
        id - String. user id queried by the function caller
       
    Returns:
        Dict or None

    Raises:
        KeyError - raises an exception
    """

    user_id = obtain_user_id_from_token()
    if verify_token_user_id_and_function_caller_id(user_id, id):
        current_user_information = g.current_user
        # delete ObjectID to jsonify
        del current_user_information['_id']
        response = {
            'user': current_user_information
        }
        return jsonify(response)
        # return jsonify(dumps(response))
    return None

@user_bp.route('/users/<string:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    elif 'username' not in data or not data.get('username', None) or (' ' in data.get('username')):
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)) or (' ' in data.get('email')):
        message['email'] = 'Please provide a valid email address.'

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    username = data.get('username')
    email = data.get('email')
    
    message = {}
    if mongoDB.search_user_document(user_id=None, username=username):
        message['username'] = 'Please use a different username.'
    if pyMongo.db.User.find_one({'email': email}):
        message['email'] = 'Please use a different email address.'

    if message:
        return bad_request(message)

    response = {

    }
    return jsonify(response)


@user_bp.route('/users/<string:id>', methods=['DELETE'])
@token_auth.login_required
def delete_user(id):
    '''
      Delete a User. Implement Later
    '''
    return "Welcome to Delete!"