# -*- coding: utf-8 -*-
import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from operator import itemgetter
from Items import db
# import BluePrint
from Items.main import main
from Items.models import User, Message, Matched
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/get_user_history/', methods=['POST'])
@token_auth.login_required
def get_user_history():
    '''哪些用户给我发过私信，按用户分组，返回各用户最后一次发送的私信
    即: (谁) 最后一次 给我发了 (什么私信)'''
    user = User.query.get_or_404(g.current_user.id)
    if g.current_user != user:
        return error_response(403)

    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    

    sponsor_data = Matched.to_collection_dict(
        Matched.query.filter(Message.sponsor_id == g.current_user.id).group_by(Matched.task_id).order_by(Matched.timestamp.desc()), page, per_page,
        'main.get_user_messages_senders', id=g.current_user.id)['items']

    recipient_data = Matched.to_collection_dict(
        Matched.query.filter(Message.recipient_id_pair == g.current_user.id).group_by(Matched.task_id).order_by(Matched.timestamp.desc()), page, per_page,
        'main.get_user_messages_senders', id=g.current_user.id)['items']

    sponsor_result = sorted(sponsor_data, key=itemgetter('timestamp'))
    recipient_result = sorted(recipient_data, key=itemgetter('timestamp'))

    returndict = {'sponsor_result': sponsor_result, 'recipient_result': recipient_result}
    return jsonify(returndict)
