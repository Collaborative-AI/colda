from __future__ import annotations

import json
import requests
import threading
import time

from colda.workflow.api import (
    TrainMainWorkflow,
    TestMainWorkflow
)

from colda.network.api import Network
from colda.pi.api import PI
from colda.authentication.api import Authentication

from typeguard import typechecked


#@typechecked
class ShortPolling():
    '''
    Short polling to interact with back-end

    Attributes
    ----------
    None

    Methods
    -------
    get_instance
    start_cooperation
    end_cooperation
    '''

    __ShortPolling_instance = None

    def __init__(self):
        self.shortpolling = {
            'running': False
        }

        self.__Network_instance = Network.get_instance()
        self.__PI_instance = PI.get_instance()
        self.__Authentication_instance = Authentication.get_instance()

        self.__default_trainMainWorkflow = TrainMainWorkflow.get_class()
        self.__default_testMainWorkflow = TestMainWorkflow.get_class()

        # The key of the train stage notification
        # returned by the back-end
        self.train_notification_category_name = {
            'unread_request',
            'unread_match_identifier',
            'unread_situation',
            'unread_output',
            'unread_train_stop',
        }

        # The key of the train stage notification
        # returned by the back-end
        self.test_notification_category_name = {
            'unread_test_request',
            'unread_test_match_identifier',
            'unread_test_output',
            'unread_test_stop',
        }

    @classmethod
    def get_instance(cls) -> type[ShortPolling]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[ShortPolling]
        '''
        if cls.__ShortPolling_instance == None:
            cls.__ShortPolling_instance = ShortPolling()

        return cls.__ShortPolling_instance

    def __distribute_notification(
        self, notification_category: dict
    ) -> None:
        '''
        1. Handle the short polling response data
        2. Call corresponding functions

        Parameters
        ----------
        update_all_notifications_data : dict

        Returns
        -------
        None
        '''
        for category_name in notification_category:
            if category_name in self.train_notification_category_name or category_name in self.test_notification_category_name:
                if category_name == 'unread_request':
                    self.__default_trainMainWorkflow.train_assistor_request(
                        notification_category[category_name]['train_id_dicts']
                    )
                elif category_name == 'unread_match_identifier':
                    self.__default_trainMainWorkflow.train_match_identifier(
                        notification_category[category_name]['train_id_dicts']
                    )
                elif category_name == 'unread_situation':
                    self.__default_trainMainWorkflow.train_situation(
                        notification_category[category_name]['train_id_dicts']
                    )
                elif category_name == 'unread_output':
                    self.__default_trainMainWorkflow.train_output(
                        notification_category[category_name]['train_id_dicts']
                    )
                elif category_name == 'unread_train_stop':
                    pass
                elif category_name == 'unread_test_request':
                    self.__default_testMainWorkflow.test_assistor_request(
                        notification_category[category_name]['test_id_dicts']
                    )
                elif category_name == 'unread_test_match_identifier':
                    self.__default_testMainWorkflow.test_match_identifier(
                        notification_category[category_name]['test_id_dicts']
                    )
                elif category_name == 'unread_test_output':
                    self.__default_testMainWorkflow.test_output(
                        notification_category[category_name]['test_id_dicts']
                    )
                elif category_name == 'unread_test_stop':
                    pass
            
                # print("category_name: ", category_name, notification_category[category_name])
        return

    def __polling(self):
        '''
        Short Polling for new Notifications

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if not self.shortpolling['running']:
            print('short polling has already stoped')
            return

        # get basic information
        user_id = self.__PI_instance.user_id
        token = self.__Network_instance.token
        if not token:
            print('Please Login First')
            return

        short_polling_res = self.__Network_instance.get_request_chaining(
            url_prefix='main_flow',
            url_root='get_notifications',
            url_suffix=user_id,
            status_code=200,
        )
        print(f'short_polling_res: {short_polling_res}')
        if 'new_token' in short_polling_res and short_polling_res['new_token'] != None:
            new_token = short_polling_res['new_token']
            self.__Authentication_instance.process_token(new_token)

        notification_category = short_polling_res['notification_result']['category']
        
        # for unittest, comment back
        return notification_category
        
        self.__distribute_notification(notification_category)
        
        timer = threading.Timer(10, self.__polling)
        timer.start()
        return

    def start_cooperation(self):
        '''
        Start short polling
        Set indicator to True

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.shortpolling['running'] == False:
            self.shortpolling['running'] = True
            self.__polling()

        return 

    def end_cooperation(self):
        '''
        End short polling
        Set indicator to False

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.shortpolling['running'] = False
        return True

