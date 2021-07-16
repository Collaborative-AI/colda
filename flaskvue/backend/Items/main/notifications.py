# -*- coding: utf-8 -*-
from flask import jsonify, g
from Items.main import main
from Items.main.auth import token_auth
from Items.main.errors import error_response
from Items.models import Notification

@main.route('/notifications/<int:id>', methods=['GET'])
@token_auth.login_required
def get_notification(id):
    '''Return a response'''
    notification = Notification.query.get_or_404(id)
    if g.current_user != notification.user:
        return error_response(403)
    data = notification.to_dict()
    return jsonify(data)