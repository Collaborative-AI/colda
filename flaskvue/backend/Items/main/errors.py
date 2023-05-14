from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from Items import db

# import BluePrint
from Items.main import main

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    '''400： Wrong Request'''
    return error_response(400, message)

# Capture the global status code and perform custom exception handling
@main.app_errorhandler(404)
def not_found_error(error):
    return error_response(404)


@main.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response(500)