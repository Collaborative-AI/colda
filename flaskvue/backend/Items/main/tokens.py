# -*- coding: utf-8 -*-
from flask import jsonify, g
from Items import db
from Items.main import main
from Items.main.auth import basic_auth, token_auth


@main.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_jwt()
    db.session.commit()
    return jsonify({'token': token})
