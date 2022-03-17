from .TrainRequest import TrainRequest, Network, PersonalInformation
from .TestRequest import TestRequest
import json
import requests
import threading
import time

class GetNotification():
    __GetNotification_instance = None

    def __init__(self):
        self.__stop_indicator = None

        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.base_url = self.Network_instance.base_url

        self.default_trainRequest = TrainRequest.get_TrainRequest_instance()
        self.default_testRequest = TestRequest.get_TestRequest_instance()

    @classmethod
    def get_GetNotification_instance(cls):
        if cls.__GetNotification_instance == None:
            cls.__GetNotification_instance = GetNotification()

        return cls.__GetNotification_instance

    def __update_notification(self, update_all_notifications_data: dict):

        """
        Handle the short polling response data and call corresponding functions

        :param update_all_notifications_data: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        unread_request_notification = update_all_notifications_data["unread request"]
        unread_match_id_notification = update_all_notifications_data["unread match id"]
        unread_situation_notification = update_all_notifications_data["unread situation"]
        unread_output_notification = update_all_notifications_data["unread output"]

        unread_test_request_notification = update_all_notifications_data["unread test request"]
        unread_test_match_id_notification = update_all_notifications_data["unread test match id"]
        unread_test_output_notification = update_all_notifications_data["unread test output"]

        print("unread_request_notification", unread_request_notification)
        print("unread_match_id_notification", unread_match_id_notification)
        print("unread_situation_notification", unread_situation_notification)
        print("unread_output_notification", unread_output_notification)

        print("unread_test_request_notification", unread_test_request_notification)
        print("unread_test_match_id_notification", unread_test_match_id_notification)
        print("unread_test_output_notification", unread_test_output_notification)

        if unread_request_notification:
            self.default_trainRequest.unread_request(unread_request_notification)

        if unread_match_id_notification:
            self.default_trainRequest.unread_match_id(unread_match_id_notification)

        if unread_situation_notification:
            self.default_trainRequest.unread_situation(unread_situation_notification)

        if unread_output_notification:
            self.default_trainRequest.unread_output(unread_output_notification)

        if unread_test_request_notification:
            self.default_testRequest.unread_test_request(unread_test_request_notification)

        if unread_test_match_id_notification:
            self.default_testRequest.unread_test_match_id(unread_test_match_id_notification)

        if unread_test_output_notification:
            self.default_testRequest.unread_test_output(unread_test_output_notification)

        return


    def start_Collaboration(self):

        """
        Short Polling for new Notifications

        :returns: None

        :exception OSError: Placeholder.
        """
        if self.__stop_indicator == None:
            self.__stop_indicator = False
        user_id = self.PersonalInformation_instance.user_id
        print('ggg',self.base_url,user_id)
        url = self.base_url + "/users/" + user_id + "/notifications/"
        token = self.Network_instance.token
        print("get notification url", url)
        try:
            short_polling_res = requests.get(url, headers={'Authorization': 'Bearer ' + token})
            print("short_polling_res", short_polling_res)
        except:
            print('short_polling_res wrong')

        response_data = json.loads(short_polling_res.text)
        # print("response_data", response_data, type(response_data))

        for item in response_data:
            if item['payload'] >= 1:
                url = self.base_url + "/update_all_notifications"
                data = {
                    "response_data": response_data
                }
                try:
                    update_all_notifications_res = requests.post(url, json=data,
                                                             headers={'Authorization': 'Bearer ' + token})
                except:
                    print('short_polling_res wrong')

                # print("update_all_notifications", update_all_notifications_res)
                update_all_notifications_data = json.loads(update_all_notifications_res.text)
                # assert update_all_notifications_data is not None
                
                # print("update_all_notifications", update_all_notifications_data)

                # for running, comment back
                self.__update_notification(update_all_notifications_data)
                break

                # for unittest
                # return update_all_notifications_data
        
        # for running, comment back
        if not self.__stop_indicator:
            print('lihjai a ')
            timer = threading.Timer(10, self.start_Collaboration)
            timer.start()
        return

    def end_Collaboration(self):
        self.__stop_indicator = True
        time.sleep(15)
        return True

