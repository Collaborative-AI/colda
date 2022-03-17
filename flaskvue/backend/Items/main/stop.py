import json

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.utils import log, generate_msg

from Items import db
# import BluePrint
from Items.main import main
# from Items.models import User, Message, Matched, Stop
from Items.main.errors import error_response, bad_request
from Items.main.auth import token_auth


@main.route('/stop_train_task/<string:id>', methods=['POST'])
@token_auth.login_required
def stop_train_task(id):

    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'task_id' not in data or not data.get('task_id'):
        return bad_request('task_id is required.')

    task_id = data.get('task_id')
    print("----------1")
    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    most_recent_round = 0
    query = Message.query.filter(Message.task_id == task_id, Message.test_indicator == "train").order_by(Message.rounds.desc()).first()
    if query is not None:
        most_recent_round = query.rounds

    # get sponsor id
    get_all_sponsor_assistors = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").all()
    sponsor_id = None
    if get_all_sponsor_assistors:
        sponsor_id = get_all_sponsor_assistors[0].sponsor_id
    
    print("----------2", sponsor_id)

    if int(sponsor_id) == g.current_user.id:
        Message.query.filter(Message.task_id == task_id, Message.test_indicator == "train", Message.rounds == most_recent_round).delete()
        db.session.commit()
        
        Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").update({"Terminate": "true"})
        db.session.commit()

        
        # add stop_deleted_user_id == sponsor to assistor
        for row in get_all_sponsor_assistors:
            if row.assistor_id_pair != sponsor_id:
                
                stop = Stop()
                stop.stop_informed_user_id = row.assistor_id_pair
                stop.stop_deleted_user_id = sponsor_id
                stop.stop_round = most_recent_round
                stop.task_id = task_id
                stop.test_indicator = "train"

                db.session.add(stop)
                db.session.commit()
                user = User.query.get_or_404(row.assistor_id_pair)
                # send unread train stop notification to current assistor
                user.add_notification('unread train stop', user.stop_train_task()) 
                db.session.commit()

        # add stop_deleted_user_id == assistor to sponsor
        # Use 2 for loop because I do not want to search User DB everytime. We only need user who is sponsor
        user = User.query.get_or_404(sponsor_id)
        for row in get_all_sponsor_assistors:
            if row.assistor_id_pair != sponsor_id:

                stop = Stop()
                stop.stop_informed_user_id = sponsor_id
                stop.stop_deleted_user_id = row.assistor_id_pair
                stop.stop_round = most_recent_round
                stop.task_id = task_id
                stop.test_indicator = "train"

                db.session.add(stop)
                db.session.commit()
                print("yiyiyiyiyiyiyiyiyiy")
                # send unread train stop notification to sponsor of current task
        user.add_notification('unread train stop', user.stop_train_task()) 
        db.session.commit()


        response = jsonify({"sponsor delete successfully": "successfully", "check sponsor": "true", "most recent round": most_recent_round})
        return response

    else:
        print("----------3")
        Message.query.filter(Message.task_id == task_id, Message.test_indicator == "train", Message.rounds == most_recent_round, Message.sender_id == g.current_user.id).delete()
        db.session.commit()
        
        Message.query.filter(Message.task_id == task_id, Message.test_indicator == "train", Message.rounds == most_recent_round, Message.assistor_id == g.current_user.id).delete()
        db.session.commit()
        
        Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == g.current_user.id, Matched.test_indicator == "train").update({"Terminate": "true"})
        db.session.commit()

        stop = Stop()
        stop.stop_informed_user_id = g.current_user.id
        stop.stop_deleted_user_id = sponsor_id
        stop.stop_round = most_recent_round
        stop.task_id = task_id
        stop.test_indicator = "train"

        db.session.add(stop)
        db.session.commit()
        # send unread train stop notification to current assistor
        user = User.query.get_or_404(g.current_user.id)
        user.add_notification('unread train stop', user.stop_train_task()) 
        db.session.commit()


        stop = Stop()
        stop.stop_informed_user_id = sponsor_id
        stop.stop_deleted_user_id = g.current_user.id
        stop.stop_round = most_recent_round
        stop.task_id = task_id
        stop.test_indicator = "train"

        db.session.add(stop)
        db.session.commit()
        # send unread train stop notification to sponsor of current task
        user = User.query.get_or_404(sponsor_id)
        user.add_notification('unread train stop', user.stop_train_task()) 
        db.session.commit()

        print("----------4")
        response = jsonify({"assistor delete successfully": "successfully", "check sponsor": "false", "most recent round": most_recent_round})
        return response



@main.route('/stop_test_task/<string:id>', methods=['POST'])
@token_auth.login_required
def stop_test_task(id):
    
    data = request.get_json()

    if not data:
        return bad_request('You must post JSON data.')
    if 'test_id' not in data or not data.get('test_id'):
        return bad_request('test_id is required.')

    test_id = data.get('test_id')
    user_id = obtain_user_id_from_token()
    user = pyMongo.db.User.find_one({'user_id': id})
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    print("----------1")
    most_recent_round = 0
    # query = Message.query.filter(Message.test_id == test_id, Message.test_indicator == "test").order_by(Message.rounds.desc()).first()
    # if query is not None:
    #     most_recent_round = query.rounds

    # get sponsor id
    get_all_sponsor_assistors = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").all()
    sponsor_id = None
    if get_all_sponsor_assistors:
        sponsor_id = get_all_sponsor_assistors[0].sponsor_id
    
    print("----------2", sponsor_id)

    if int(sponsor_id) == g.current_user.id:
        Message.query.filter(Message.test_id == test_id, Message.test_indicator == "test", Message.rounds == most_recent_round).delete()
        db.session.commit()
        
        Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == "test").update({"Terminate": "true"})
        db.session.commit()

        
        # add stop_deleted_user_id == sponsor to assistor
        for row in get_all_sponsor_assistors:
            if row.assistor_id_pair != sponsor_id:
                
                stop = Stop()
                stop.stop_informed_user_id = row.assistor_id_pair
                stop.stop_deleted_user_id = sponsor_id
                stop.stop_round = most_recent_round
                stop.test_id = test_id
                stop.test_indicator = "test"

                db.session.add(stop)
                db.session.commit()
                user = User.query.get_or_404(row.assistor_id_pair)
                # send unread train stop notification to current assistor
                user.add_notification('unread test stop', user.stop_test_task()) 
                db.session.commit()

        # add stop_deleted_user_id == assistor to sponsor
        # Use 2 for loop because I do not want to search User DB everytime. We only need user who is sponsor
        user = User.query.get_or_404(sponsor_id)
        for row in get_all_sponsor_assistors:
            if row.assistor_id_pair != sponsor_id:

                stop = Stop()
                stop.stop_informed_user_id = sponsor_id
                stop.stop_deleted_user_id = row.assistor_id_pair
                stop.stop_round = most_recent_round
                stop.test_id = test_id
                stop.test_indicator = "test"

                db.session.add(stop)
                db.session.commit()
                print("yiyiyiyiyiyiyiyiyiy")
                # send unread train stop notification to sponsor of current task
        user.add_notification('unread test stop', user.stop_test_task()) 
        db.session.commit()

        response = jsonify({"test stop successfully": "successfully"})
        return response


    
      
    
