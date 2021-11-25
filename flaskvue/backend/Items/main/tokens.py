# -*- coding: utf-8 -*-
from flask import jsonify, g
from Items import db
from Items.main import main
from Items.main.auth import basic_auth, token_auth


@main.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    """
    Login function (doesnt need token). If the user registered but not confirmed yet, we lead it to the confirmation page.
    If the user finishes the confirmation, we send it a token.

    Parameters:
        None

    Returns:
        msg - String. The string that indicates no confirmation
        token - Dict. Token for user.

    Raises:
        KeyError - raises an exception
    """
    
    if g.current_user.confirmed == 'false':
        msg = 'not verify email yet'
        return jsonify(msg)
        
    token = g.current_user.get_jwt()
    db.session.commit()
    return jsonify({'token': token})
