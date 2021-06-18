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


@main.route('/check_situation_sponsor/', methods=['POST'])
@token_auth.login_required
def check_situation_sponsor():

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')
    
    task_id = data.get('task_id')

    # check if the current client is the sponsor
    isSponsor = False
    query = Matched.query.filter(Matched.task_id == task_id).first()
    if query.sponsor_id == g.current_user.id:
        isSponsor = True

    cur_rounds = 0
    if isSponsor:
        query = Message.query.filter(Message.sender_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()
        cur_rounds = query.rounds
    else:
        query = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()
        cur_rounds = query.rounds

    # Update the Notification
    user = User.query.get_or_404(g.current_user.id)
    last_situation_read_time = user.last_situation_read_time or datetime(1900, 1, 1)
    
    record = Message.query.filter(Message.recipient_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()

    # If can be omitted
    if last_situation_read_time > record['situation_timestamp']:
        user.last_situation_read_time = record['situation_timestamp']

        # submit to database
        db.session.commit()
        
        # Updata Notification
        user.add_notification('unread situation', user.new_situation()) 
        db.session.commit()

    dict = {}
    if isSponsor:
        dict = {"sponsor": "true"}
    else:
        dict = {"sponsor": "false"}

    dict['rounds'] = cur_rounds
    response = jsonify(dict)

    response.status_code = 204
    
    return response


@main.route('/send_output/', methods=['POST'])
@token_auth.login_required
def send_output():

    data = request.get_json()
    
    if not data:
        return bad_request('You must post JSON data.')
    if 'output' not in data or not data.get('output'):
        return bad_request('output is required.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    output = data.get('output')
    task_id = data.get('task_id')
    recipient_num = data.get('recipient_num')

    # extract sponsor_id
    query = Matched.query.filter(Matched.task_id == task_id).first()

    message = Message()
    message.from_dict(data)
    message.sender_id = g.current_user.id
    message.recipient_id = query.sponsor_id
    message.task_id = task_id
    
    get_round_num = Message.query.filter(Message.sender_id == g.current_user.id, Message.task_id == task_id).order_by(Message.rounds.desc()).first()
    message.rounds = get_round_num.rounds
    
    # Store the output
    message.output = output
    db.session.add(message)

    all_cur_round_messages = Message.query.filter(Message.recipient_id == query.sponsor_id, Message.task_id == task_id, Message.rounds == get_round_num.rounds).all()
    output_upload = 0
    for row in all_cur_round_messages:
        if row.output:
            output_upload += 1

        if output_upload == recipient_num:
            user = User.query.get_or_404(query.sponsor_id)
            # send message notification to the sponsor when all recipient upload the output
            user.add_notification('unread output', user.new_output())
            db.session.commit()

    dict = {"send_output": "successfully"}
    response = jsonify(dict)
    response.status_code = 204
    
    return response

    