# -*- coding: utf-8 -*-
import sys

from flask import request
from flask.json import jsonify

# import BluePrint
from Items.helper_api import helper_api_bp
# from Items.models import User, Matched, Pending
from Items.exception import error_response, bad_request
from Items.authentication import token_auth
from Items.utils import get_log, log, generate_msg
from Items.utils.api import (
    check_if_data_is_valid,
    input_data_err_msg,
    obtain_user_id_from_token, 
    verify_token_user_id_and_function_caller_id
)

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match

@helper_api_bp.route('/get_backend_log/<string:id>', methods=['POST'])
@token_auth.login_required
def get_backend_log(id):
    """
    return log of current task. Must have train_id in data, Might have test_id in data.

    Parameters:
        train_id - String.

    Returns:
        data - Dict[Dict[String, String, List[String]]]. List[String]: ['first log_interval\n', 'second\n', 'third']

    Raises:
        KeyError - raises an exception
    """
    data = request.get_json()
    if not data:
        raise ValueError(input_data_err_msg(sys._getframe().f_code.co_name, 'You must post JSON data.'))
        
    expected_data = {
        'train_id': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    user_id = obtain_user_id_from_token()
    user_document = mongoDB.search_user_document(user_id=id,username=None, email=None, key_indicator='user_id')
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user_document['user_id']):
        return error_response(403)

    train_id = data['train_id']
    train_match_document = train_match.search_train_match_document(train_id=train_id)
    test_id_of_train_id_dict = train_match_document['test_id_of_train_id_dict']
    
    response = {}
    response[train_id] = {
        'id': train_id,
        'test_indicator': 'train',
        'log_file': get_log(user_id, train_id)
    }
    for test_id in test_id_of_train_id_dict:
        response[test_id] = {
            'id': test_id,
            'test_indicator': 'test',
            'log_file': get_log(user_id, test_id)
        }
        
    return jsonify(response)

