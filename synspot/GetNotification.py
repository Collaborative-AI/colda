from .workflow.train_workflow import TrainRequest, Network, PersonalInformation
from .workflow.test_workflow import TestRequest
from .authorization import Authorization
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
        self.Authorization_instance = Authorization.get_Authorization_instance()
        self.base_url = self.Network_instance.base_url

        self.default_trainRequest = TrainRequest.get_TrainRequest_instance()
        self.default_testRequest = TestRequest.get_TestRequest_instance()

        self.train_notification_category_name = {
            'unread_request',
            'unread_match_identifierentifier',
            'unread_situation',
            'unread_output',
            'unread_train_stop',
        }

        self.test_notification_category_name = {
            'unread_test_request',
            'unread_test_match_identifierentifier',
            'unread_test_output',
            'unread_test_stop',
        }
    @classmethod
    def get_GetNotification_instance(cls):
        if cls.__GetNotification_instance == None:
            cls.__GetNotification_instance = GetNotification()

        return cls.__GetNotification_instance

    def __distribute_notification(self, notification_category: dict):

        """
        Handle the short polling response data and call corresponding functions

        :param update_all_notifications_data: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        for category_name in notification_category:
            if category_name in self.train_notification_category_name or category_name in self.test_notification_category_name:
                if category_name == 'unread_request':
                    self.default_trainRequest.unread_request(notification_category[category_name]['task_id_dict'])
                elif category_name == 'unread_match_identifier':
                    self.default_trainRequest.unread_match_identifier(notification_category[category_name]['task_id_dict'])
                elif category_name == 'unread_situation':
                    self.default_trainRequest.unread_situation(notification_category[category_name]['task_id_dict'])
                elif category_name == 'unread_output':
                    self.default_trainRequest.unread_output(notification_category[category_name]['task_id_dict'])
                elif category_name == 'unread_train_stop':
                    pass
                elif category_name == 'unread_test_request':
                    self.default_testRequest.unread_test_request(notification_category[category_name]['test_id_dict'])
                elif category_name == 'unread_test_match_identifier':
                    self.default_testRequest.unread_test_match_identifier(notification_category[category_name]['test_id_dict'])
                elif category_name == 'unread_test_output':
                    self.default_testRequest.unread_test_output(notification_category[category_name]['test_id_dict'])
                elif category_name == 'unread_test_stop':
                    pass
            

                print("category_name: ", category_name, notification_category[category_name])

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

        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url='/users', suffix=user_id)

        token = self.Network_instance.token
        if not token:
            print('Please Login First')
            return

        try:
            short_polling_res = requests.get(url, headers={'Authorization': 'Bearer ' + token})
            print("short_polling_res", short_polling_res)
        except:
            print('short_polling_res wrong')

        # update new token if response_data['new_token'] is not None
        response_data = json.loads(short_polling_res.text)
        if 'new_token' in response_data and response_data['new_token'] != None:
            new_token = response_data['new_token']
            self.Authorization_instance.process_token(new_token)

        notification_category = response_data['notification_result']['category']
        self.__distribute_notification(notification_category)

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

