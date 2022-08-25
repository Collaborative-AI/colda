from __future__ import annotations

# -*- coding: utf-8 -*-
import copy

from flask import g
from flask.json import jsonify
from bson.json_util import loads, dumps


# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main_flow import main_flow_bp
from Items.exception import error_response, bad_request
from Items.utils import obtain_user_id_from_token, add_new_token_to_response
from Items.utils import verify_token_user_id_and_function_caller_id, log, generate_msg
from Items.authentication import token_auth

from Items.mongoDB import mongoDB


@main_flow_bp.route('/get_notifications/<string:id>/', methods=['GET'])
@token_auth.login_required
def get_notifications(id):
    """
    Return a new notification

    Parameters:
       user_id - String. 
       
    Returns:
        Dict[Dict[Dict]]

    Raises:
        KeyError - raises an exception
    """

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # print('5124', user_document['username'])
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    notification_document = pyMongo.db.Notification.find_one({'user_id': user_id})
    # print('notification_document', notification_document, user_id)
    if notification_document is None:
        response = {
            'notification_result': {
                'category': {}
            }
        }
        return jsonify(response)

    category = notification_document['category']

    # If there is no new notification return a null dict
    if len(category) == 0:
        response = {
            'notification_result': {
                'category': {}
            }
        }
        return jsonify(response)

    # If there is new notification, return the notification document and set the category to {}
    notification_document = pyMongo.db.Notification.find_one_and_update({'user_id': user_id}, {'$set':{'category': {}}})
    del notification_document['_id']
    response = {
        'notification_result': copy.deepcopy(notification_document)
    }
    if 'new_token' in g.current_user and g.current_user['new_token'] != None:
        response = add_new_token_to_response(response)

    # print('cat1', type(response))
    # print('cat1res', response)
    return jsonify(response)