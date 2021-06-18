from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Message, Matched
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

    cur_rounds = 0
    query = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()
    cur_rounds = query.rounds

    # If can be omitted
    if last_output_read_time > record['output_timestamp']:
        user.last_output_read_time = record['output_timestamp']

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread output', user.new_output()) 
        db.session.commit()
    
    dict = {}

    dict['rounds'] = cur_rounds
    response = jsonify(dict)

    response.status_code = 204
    
    return response

@main.route('/users/<int:id>/output/', methods=['GET'])
@token_auth.login_required
def get_user_match_id(id):

    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    task_id = request.args.get('task_id', 0, type=int)
    recipient_num = request.args.get('recipient_num', 0, type=int)

    data = {}
    query = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).all()

    output_files = []
    recipient_random_ids = []
    for row in query:
        if row.output:

            output_files.append(row.output)
            recipient_random_id = Matched.query.filter(Matched.recipient_id_pair == row.sender_id, Message.task_id == task_id).first()
            recipient_random_ids.append(recipient_random_id)
        
        if len(output_files) == recipient_num:
            break

    data = {
        'output': [item for item in output_files],
        'recipient_random_id_pair': [item for item in recipient_random_ids]
    }


    return jsonify(data)  