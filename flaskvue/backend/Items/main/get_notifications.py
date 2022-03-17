# -*- coding: utf-8 -*-
import json
import copy
import collections
from collections import defaultdict

from flask import Flask, session, request, g, current_app
from flask.helpers import url_for
from flask.json import jsonify
from datetime import datetime
from Items.main.utils import log, generate_msg

# from Items import db
from Items import pyMongo
# import BluePrint
from Items.main import main, stop
# from Items.models import User, Message, Matched, Notification, Stop
from Items.main.errors import error_response, bad_request
from Items.main.utils import obtain_user_id_from_token, add_new_token_to_response
from Items.main.utils import verify_token_user_id_and_function_caller_id
from Items.main.auth import token_auth

@main.route('/get_notifications/<string:id>/', methods=['GET'])
@token_auth.login_required
def get_notifications(id):
    """
    Return a new notification

    Parameters:
       user_id - String. 
       
    Returns:
        Dict[Dict[Dict]]

    Raises:
        KeyError - raises an exception
    """

    user_id = obtain_user_id_from_token()
    user = mongoDB.search_user_document(user_id=id)
    # check if the caller of the function and the id is the same
    if not verify_token_user_id_and_function_caller_id(user_id, user['user_id']):
        return error_response(403)

    notification_document = pyMongo.db.Notification.find_one({'user_id': user_id})
    category = notification_document['category']

    # If there is no new notification return a null dict
    if len(category) == 0:
        response = {
            'notification_result': {
                'category': {}
            }
        }
        return jsonify(response)

    # If there is new notification, return the notification document and set the category to {}
    notification_document = pyMongo.db.Notification.find_one_and_update({'user_id': user_id}, {'$set':{'category': {}}})
    response = {
        'notification_result': copy.deepcopy(notification_document)
    }
    return jsonify(response)

    # return_dict = {
    #     "unread request": {}, 
    #     "unread match id": {}, 
    #     "unread situation": {}, 
    #     "unread output": {}, 
    #     "unread test request": {}, 
    #     "unread test match id": {}, 
    #     "unread test output": {}, 
    #     "unread train stop": {}, 
    #     "unread test stop": {}
    # }

    # train_notification = {
    #     "unread request",
    #     "unread match id",
    #     "unread situation", 
    #     "unread output", 
    # }

    # test_notification = {
    #     "unread test request", 
    #     "unread test match id", 
    #     "unread test output"
    # }


    # notification_document = pyMongo.db.Notification.find_one_and_update({'user_id': user_id}, {'$set':{'category': {}}})

    # category = notification_document['category']
    # for category_name in category:
    #     category_count = category[category_name]['category_count']
    #     if category_count >= 1:
    #         if category_name in train_notification:
    #             task_id_dict = category[category_name]['task_id_dict']
    #             return_dict[category_name]['task_id_dict'] = copy.deepcopy(task_id_dict)
    #         elif category_name in test_notification:
    #             test_id_dict = category[category_name]['test_id_dict']
    #             return_dict[category_name]['test_id_dict'] = copy.deepcopy(test_id_dict)
    
    # return_dict = add_new_token_to_response(return_dict)
    # return return_dict


    
# @main.route('/update_all_notifications/', methods=['POST'])
# @token_auth.login_required
# def update_all_notifications():

#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'response_data' not in data or not data.get('response_data'):
#         return bad_request('response_data is required.')

#     response_data = data.get('response_data')
    
    

    # user = User.query.get_or_404(g.current_user.id)
    # for i in range(len(response_data)):
    #     sender_random_id_list = response_data[i]["sender_random_id_list"]
    #     task_id_list = response_data[i]["task_id_list"]
        
    #     if int(response_data[i]["payload"]) != 0:
    #         if response_data[i]["name"] == "unread train stop":
    #             stop_deleted_user_id_and_round_list = sender_random_id_list
    #             print("unread train stop", task_id_list, stop_deleted_user_id_and_round_list)
                
    #             task_id_to_deleted_user_id = defaultdict(list)
    #             most_recent_round = defaultdict(list)
                
    #             lastest_time = datetime(1900, 1, 1)
    #             for j in range(len(task_id_list)):
    #                 task_id_to_deleted_user_id[task_id_list[j]].append(stop_deleted_user_id_and_round_list[0][j])
    #                 most_recent_round[task_id_list[j]].append(stop_deleted_user_id_and_round_list[1][j])

    #                 record = Stop.query.filter(Stop.stop_informed_user_id == g.current_user.id, Stop.task_id == task_id_list[j], Stop.test_indicator == "train").order_by(Stop.timestamp.desc()).all()
    #                 # get the latest output timestamp
    #                 if record[0].timestamp > lastest_time:
    #                     lastest_time = record[0].timestamp

    #             last_unread_stop_train_task_read_time = user.last_unread_stop_train_task_read_time or datetime(1900, 1, 1)          
    #             if lastest_time > last_unread_stop_train_task_read_time:
    #                 user.last_unread_stop_train_task_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread train stop', user.stop_train_task()) 
    #                 db.session.commit()

    #             return_dict["unread train stop"]["task_id_to_deleted_user_id"] = task_id_to_deleted_user_id
    #             return_dict["unread train stop"]["most_recent_round"] = most_recent_round

    #         elif response_data[i]["name"] == "unread test stop":
    #             test_id_list = task_id_list
    #             stop_deleted_user_id_and_round_list = sender_random_id_list
    #             print("unread train stop", test_id_list, stop_deleted_user_id_and_round_list)
                
    #             task_id_to_deleted_user_id = defaultdict(list)
    #             most_recent_round = defaultdict(list)
                
    #             lastest_time = datetime(1900, 1, 1)
    #             for j in range(len(test_id_list)):
    #                 task_id_to_deleted_user_id[test_id_list[j]].append(stop_deleted_user_id_and_round_list[0][j])
    #                 most_recent_round[test_id_list[j]].append(stop_deleted_user_id_and_round_list[1][j])

    #                 record = Stop.query.filter(Stop.stop_informed_user_id == g.current_user.id, Stop.test_id == test_id_list[j], Stop.test_indicator == "test").order_by(Stop.timestamp.desc()).all()
    #                 # get the latest output timestamp
    #                 if record[0].timestamp > lastest_time:
    #                     lastest_time = record[0].timestamp

    #             last_unread_stop_test_task_read_time = user.last_unread_stop_test_task_read_time or datetime(1900, 1, 1)          
    #             if lastest_time > last_unread_stop_test_task_read_time:
    #                 user.last_unread_stop_test_task_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread test stop', user.stop_test_task()) 
    #                 db.session.commit()

    #             return_dict["unread test stop"]["task_id_to_deleted_user_id"] = task_id_to_deleted_user_id
    #             return_dict["unread test stop"]["most_recent_round"] = most_recent_round


    #         elif response_data[i]["name"] == "unread request":
    #             print("unread request", task_id_list)
    #             check_dict = {}
    #             info_dict = collections.defaultdict(dict)
    #             lastest_time = datetime(1900, 1, 1)
    #             for j in range(len(task_id_list)):
    #                 record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id_list[j], Matched.test_indicator == "train").order_by(Matched.request_timestamp.desc()).all()
    #                 # get the latest output timestamp
    #                 if record[0].request_timestamp > lastest_time:
    #                     lastest_time = record[0].request_timestamp
    #                 check_dict[task_id_list[j]] = 1
    #                 print(type(info_dict[task_id_list[j]]))
    #                 info_dict[task_id_list[j]]['task_mode'] = record[0].task_mode
    #                 info_dict[task_id_list[j]]['model_name'] = record[0].model_name
    #                 info_dict[task_id_list[j]]['metric_name'] = record[0].metric_name
    #             # Update the Notification

    #             last_requests_read_time = user.last_requests_read_time or datetime(1900, 1, 1)          
    #             if lastest_time > last_requests_read_time:
    #                 user.last_requests_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread request', user.new_request()) 
    #                 db.session.commit()

    #             return_dict["unread request"]["check_dict"] = check_dict
    #             return_dict["unread request"]["info_dict"] = info_dict

    #         elif response_data[i]["name"] == "unread match id":    
    #             print("unread match id", task_id_list)
    #             check_dict = {}
    #             lastest_time = datetime(1900, 1, 1)

    #             for j in range(len(task_id_list)):
    #                 # check if the current client is the sponsor
    #                 isSponsor = False
    #                 query = Matched.query.filter(Matched.task_id == task_id_list[j]).first()
                    
    #                 if query:
    #                     print("match_id_query", query)
    #                     print("match_id_query.sponsor_id", query.sponsor_id, type(query.sponsor_id))
    #                     print("g.current_user.id", g.current_user.id, type(g.current_user.id))
    #                     if int(query.sponsor_id) == g.current_user.id:
    #                         isSponsor = True

    #                     record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.task_id == task_id_list[j], Matched.test_indicator == "train").order_by(Matched.match_id_timestamp.desc()).all()

    #                     # get the latest output timestamp
    #                     if record[0].match_id_timestamp > lastest_time:
    #                         lastest_time = record[0].match_id_timestamp
                        
    #                     print("isSponsor", isSponsor)
    #                     if isSponsor:
    #                         print("sponsor")
    #                         check_dict[task_id_list[j]] = 1
    #                     else:
    #                         print("assistor")
    #                         check_dict[task_id_list[j]] = 0

    #             # Update the Notification

    #             last_matched_file_read_time = user.last_matched_file_read_time or datetime(1900, 1, 1)
    #             if lastest_time > last_matched_file_read_time:
    #                 user.last_matched_file_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread match id', user.new_match_id()) 
    #                 db.session.commit()
                    
    #             return_dict["unread match id"]["check_dict"] = check_dict

    #         elif response_data[i]["name"] == "unread situation":
    #             print("unread situation", task_id_list)
    #             check_dict = {}
    #             rounds_dict = {}
    #             lastest_time = datetime(1900, 1, 1)

    #             stop_task = True
    #             for j in range(len(task_id_list)):
    #                 # check if the current client is the sponsor
    #                 isSponsor = False
    #                 query = Matched.query.filter(Matched.task_id == task_id_list[j]).first()
    #                 if query:
    #                     if int(query.sponsor_id) == g.current_user.id:
    #                         isSponsor = True
                        
    #                     record = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id_list[j], Message.situation != None, Message.test_indicator == "train").order_by(Message.situation_timestamp.desc()).first()
    #                     # print("]]]]]]]]]]]]", record, record.rounds)
    #                     if record:
    #                         cur_rounds = record.rounds
    #                         rounds_dict[task_id_list[j]] = cur_rounds

    #                         if isSponsor:
    #                             check_dict[task_id_list[j]] = 1
    #                         else:
    #                             check_dict[task_id_list[j]] = 0

    #                         # get the latest output timestamp
    #                         if record.situation_timestamp > lastest_time:
    #                             lastest_time = record.situation_timestamp

                        
    #             print("stop_task/////////////////////", stop_task)
                            

    #             # Update the Notification

    #             last_situation_read_time = user.last_situation_read_time or datetime(1900, 1, 1)
    #             if lastest_time > last_situation_read_time:
    #                 stop_task = False
    #                 print("------------", "@@@@@@@@", lastest_time, last_situation_read_time)
    #                 user.last_situation_read_time = lastest_time

    #                 # submit to database
    #                 db.session.commit()
                    
    #                 # Updata Notification
    #                 user.add_notification('unread situation', user.new_situation()) 
    #                 db.session.commit()

    #                 print("zzzzzzz")


    #             if stop_task:
    #                 user.add_notification('unread situation', user.new_situation()) 
    #                 db.session.commit()

    #                 return_dict["unread situation"]["check_dict"] = {}
    #                 return_dict["unread situation"]["rounds_dict"] = {}
    #             else:
    #                 return_dict["unread situation"]["check_dict"] = check_dict
    #                 return_dict["unread situation"]["rounds_dict"] = rounds_dict

    #         elif response_data[i]["name"] == "unread output":
    #             print("unread output", task_id_list)
    #             task_id_list = set(task_id_list)

    #             lastest_time = datetime(1900, 1, 1)
    #             rounds_dict = {}

    #             stop_task = True
    #             for j in task_id_list:
    #                 record = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == j, Message.output != None, Message.test_indicator == "train").order_by(Message.output_timestamp.desc()).first()
    #                 if record:
    #                     cur_rounds = record.rounds
    #                     rounds_dict[j] = cur_rounds

    #                     if record.output_timestamp > lastest_time:
    #                         lastest_time = record.output_timestamp


    #             # Update the Notification 

    #             last_output_read_time = user.last_output_read_time or datetime(1900, 1, 1)
    #             if lastest_time > last_output_read_time:
    #                 stop_task = False
    #                 user.last_output_read_time = lastest_time

    #                 # submit to database
    #                 db.session.commit()
                    
    #                 # Updata Notification
    #                 user.add_notification('unread output', user.new_output()) 
    #                 db.session.commit()

    #             if stop_task:
    #                 user.add_notification('unread output', user.new_output()) 
    #                 db.session.commit()
    #                 return_dict["unread output"]["rounds_dict"] = {}
    #             else:
    #                 return_dict["unread output"]["rounds_dict"] = rounds_dict

    #         elif response_data[i]["name"] == "unread test request":
    #             test_id_list = task_id_list
    #             print("unread test request", test_id_list)
    #             check_dict = {}
    #             test_id_to_task_id = {}
    #             lastest_time = datetime(1900, 1, 1)
    #             info_dict = collections.defaultdict(dict)

    #             for j in range(len(test_id_list)):
    #                 record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id_list[j], Matched.test_indicator == "test").order_by(Matched.request_timestamp.desc()).all()
    #                 # get the latest output timestamp
    #                 if record[0].request_timestamp > lastest_time:
    #                     lastest_time = record[0].request_timestamp
    #                 check_dict[test_id_list[j]] = 1
    #                 test_id_to_task_id[test_id_list[j]] = record[0].task_id
    #                 info_dict[test_id_list[j]]['task_mode'] = record[0].task_mode
    #                 info_dict[test_id_list[j]]['model_name'] = record[0].model_name
    #                 info_dict[test_id_list[j]]['metric_name'] = record[0].metric_name
    #             # Update the Notification

    #             last_test_requests_read_time = user.last_test_requests_read_time or datetime(1900, 1, 1)          
    #             if lastest_time > last_test_requests_read_time:
    #                 user.last_test_requests_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread test request', user.new_test_request()) 
    #                 db.session.commit()

    #             return_dict["unread test request"]["check_dict"] = check_dict
    #             return_dict["unread test request"]["test_id_to_task_id"] = test_id_to_task_id
    #             return_dict["unread test request"]["info_dict"] = info_dict

    #         elif response_data[i]["name"] == "unread test match id":   
    #             test_id_list = task_id_list 
    #             print("unread test match id", test_id_list)
    #             check_dict = {}
    #             test_id_to_task_id = {}
    #             max_rounds = {}

    #             lastest_time = datetime(1900, 1, 1)

    #             for j in range(len(test_id_list)):
    #                 # check if the current client is the sponsor
    #                 isSponsor = False
    #                 query = Matched.query.filter(Matched.test_id == test_id_list[j]).first()
    #                 task_id_of_test_id = query.task_id

    #                 if query:
    #                     print("test match_id_query", query)
    #                     print("test match_id_query.sponsor_id", query.sponsor_id, type(query.sponsor_id))
    #                     print("test g.current_user.id", g.current_user.id, type(g.current_user.id))
    #                     if int(query.sponsor_id) == g.current_user.id:
    #                         isSponsor = True

    #                     record = Matched.query.filter(Matched.assistor_id_pair == g.current_user.id, Matched.test_id == test_id_list[j], Matched.test_indicator == "test").order_by(Matched.match_id_timestamp.desc()).all()

    #                     print("$$$$$$$", task_id_of_test_id)
    #                     max_round_query = Message.query.filter(Message.assistor_id == g.current_user.id, Message.task_id == task_id_of_test_id,  Message.test_indicator == "train").order_by(Message.rounds.desc()).first()

    #                     # get the latest output timestamp
    #                     if record[0].match_id_timestamp > lastest_time:
    #                         lastest_time = record[0].match_id_timestamp
                        
    #                     print("isSponsor", isSponsor)
    #                     if isSponsor:
    #                         print("sponsor")
    #                         check_dict[test_id_list[j]] = 1
    #                     else:
    #                         print("assistor")
    #                         check_dict[test_id_list[j]] = 0

    #                     test_id_to_task_id[test_id_list[j]] = record[0].task_id

    #                     if not max_round_query:
    #                         max_rounds[test_id_list[j]] = 0
    #                     else:
    #                         max_rounds[test_id_list[j]] = max_round_query.rounds
                           

    #             # Update the Notification

    #             last_test_matched_file_read_time = user.last_test_matched_file_read_time or datetime(1900, 1, 1)
    #             if lastest_time > last_test_matched_file_read_time:
    #                 user.last_test_matched_file_read_time = lastest_time
    #                 # submit to database
    #                 db.session.commit()
    #                 # Updata Notification
    #                 user.add_notification('unread test match id', user.new_test_match_id()) 
    #                 db.session.commit()
                    
    #             return_dict["unread test match id"]["check_dict"] = check_dict
    #             return_dict["unread test match id"]["test_id_to_task_id"] = test_id_to_task_id
    #             return_dict["unread test match id"]["max_rounds"] = max_rounds

    #         elif response_data[i]["name"] == "unread test output":
    #             test_id_list = task_id_list
    #             print("unread test output", test_id_list)
    #             test_id_list = set(test_id_list)
    #             check_dict = {}
    #             test_id_to_task_id = {}
    #             stop_test = True
    #             lastest_time = datetime(1900, 1, 1)
                
    #             for j in test_id_list:
    #                 record = Message.query.filter(Message.assistor_id == g.current_user.id, Message.test_id == j, Message.test_indicator == "test").order_by(Message.output_timestamp.desc()).first()
    #                 if record:
    #                     cur_rounds = record.rounds
    #                     check_dict[j] = 1

    #                     if record.output_timestamp > lastest_time:
    #                         lastest_time = record.output_timestamp
    #                     test_id_to_task_id[j] = record.task_id


    #             # Update the Notification 

    #             last_test_output_read_time = user.last_test_output_read_time or datetime(1900, 1, 1)
    #             if lastest_time > last_test_output_read_time:
    #                 stop_test = False
    #                 user.last_test_output_read_time = lastest_time

    #                 # submit to database
    #                 db.session.commit()
                    
    #                 # Updata Notification
    #                 user.add_notification('unread test output', user.new_test_output()) 
    #                 db.session.commit()

    #             if stop_test:
    #                 user.add_notification('unread test output', user.new_test_output()) 
    #                 db.session.commit()

    #                 return_dict["unread test output"]["check_dict"] = {}
    #                 return_dict["unread test output"]["test_id_to_task_id"] = {}
    #             else:
    #                 return_dict["unread test output"]["check_dict"] = check_dict
    #                 return_dict["unread test output"]["test_id_to_task_id"] = test_id_to_task_id
    # # print("return_dict", return_dict)

    # notifications = user.notifications.filter(
    #     Notification.timestamp > 0).order_by(Notification.timestamp.asc())
    # return_dict['Updated Notification'] = [n.to_dict() for n in notifications]


