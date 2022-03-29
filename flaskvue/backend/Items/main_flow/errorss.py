from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from Items.main_flow import main_flow_bp

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    print('responseaaa', response)
    response.status_code = status_code
    return response

def bad_request(message):
    '''400： Wrong Request'''
    return error_response(400, message)

# Capture the global status code and perform custom exception handling
@main_flow_bp.app_errorhandler(404)
def not_found_error(error):
    print('main_flow_bp')
    return error_response(404, 'main_flow_bp')

@main_flow_bp.app_errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return error_response(500)