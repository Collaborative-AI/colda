from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime

from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Notification, Matched, Message
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth

@main.route('/update_output_notification/', methods=['POST'])
@token_auth.login_required
def update_output_notification():

    data = request.get_json()
    
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id_list' not in data or not data.get('task_id_list'):
        return bad_request('task_id_list is required.')

    task_id_list = data.get('task_id_list')

    # Update the Notification 
    user = User.query.get_or_404(g.current_user.id)
    last_output_read_time = user.last_output_read_time or datetime(1900, 1, 1)

    lastest_time = float("-inf")
    for i in range(len(task_id_list)):
        record = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id_list[i]).order_by(Message.output_timestamp.desc()).first()
        if record['output_timestamp'] > lastest_time:
            lastest_time = record['output_timestamp']

    return_dict = {}
    for i in range(len(task_id_list)):
        query = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id_list[i]).order_by(Message.rounds.desc()).first()
        cur_rounds = query.rounds
        return_dict[str(task_id_list[i])] = cur_rounds

    # If can be omitted
    if lastest_time > last_output_read_time:
        user.last_output_read_time = lastest_time

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread output', user.new_output()) 
        db.session.commit()
    
    response = jsonify(return_dict)

    response.status_code = 204
    
    return response

@main.route('/users/<int:id>/output/', methods=['GET'])
@token_auth.login_required
def get_user_output(id):

    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)

    task_id = request.args.get('task_id', 0, type=int)
    # recipient_num = request.args.get('recipient_num', 0, type=int)
    rounds = request.args.get('rounds', 0, type=int)

    data = {}
    query = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id, Message.rounds == rounds).order_by(Message.rounds.desc()).all()

    output_files = []
    recipient_random_ids = []
    for row in query:
        if row.output:

            output_files.append(row.output)
            # recipient_random_id = Matched.query.filter(Matched.recipient_id_pair == row.sender_id, Message.task_id == task_id).first()
            # recipient_random_ids.append(recipient_random_id)
            recipient_random_ids.append(row.sender_random_id)

    data = {
        'output': [item for item in output_files],
        'recipient_random_id_pair': [item for item in recipient_random_ids]
    }

    return jsonify(data)  