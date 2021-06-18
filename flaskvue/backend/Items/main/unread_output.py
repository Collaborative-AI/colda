from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/update_output_notification/', methods=['POST'])
@token_auth.login_required
def update_output_notification():

    data = request.get_json()
    
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data.get('task_id')

    # Update the Notification 
    user = User.query.get_or_404(g.current_user.id)
    last_output_read_time = user.last_output_read_time or datetime(1900, 1, 1)
    record = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id).order_by(Message.output_timestamp.desc()).first()

    # If can be omitted
    if last_output_read_time > record['output_timestamp']:
        user.last_output_read_time = record['output_timestamp']

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread output', user.new_output()) 
        db.session.commit()

        