from __future__ import annotations

import json
import requests
import threading
import time

from workflow.api import (
    TrainMainWorkflow,
    TestMainWorkflow
)
from network.api import Network
from pi.api import PI
from authentication.api import Authentication

from typeguard import typechecked


#@typechecked
class ShortPolling():
    '''
    Short polling to interact with back-end

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
        self.throw_exception = False

        self.__Network_instance = Network.get_instance()
        self.__PI_instance = PI.get_instance()
        self.__Authentication_instance = Authentication.get_instance()

        self.__default_trainMainWorkflow = TrainMainWorkflow.get_class()
        self.__default_testMainWorkflow = TestMainWorkflow.get_class()

        # The key of the all stage notification
        # returned by the back-end
        self.notification_category_name = {
            'unread_request': 1,
            'unread_match_identifier': 2,
            'unread_situation': 3,
            'unread_output': 4,
            'unread_train_stop': 5,
            'unread_test_request': 6,
            'unread_test_match_identifier': 7,
            'unread_test_output': 8,
            'unread_test_stop': 9,
        }

    @classmethod
    def get_instance(cls) -> type[ShortPolling]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        type[ShortPolling]
        '''
        if cls.__ShortPolling_instance == None:
            cls.__ShortPolling_instance = ShortPolling()

        return cls.__ShortPolling_instance

    def handle_thread_exception(self, args):
        self.shortpolling['running'] = False
        print('handle_thread_exception')
        print(f'Thread failed: {args}')
        return

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
        print(f'notification_category: {notification_category}')
        notification_category = sorted(notification_category.items(), key=lambda x:self.notification_category_name[x[0]])
        for notification in notification_category:
            key = notification[0]
            value = notification[1]
            if key in self.notification_category_name:
                if key == 'unread_request':
                    self.__default_trainMainWorkflow.train_assistor_request(
                        value['train_id_dicts']
                    )
                elif key == 'unread_match_identifier':
                    self.__default_trainMainWorkflow.train_match_identifier(
                        value['train_id_dicts']
                    )
                elif key == 'unread_situation':
                    self.__default_trainMainWorkflow.train_situation(
                        value['train_id_dicts']
                    )
                elif key == 'unread_output':
                    return self.__default_trainMainWorkflow.train_output(
                        value['train_id_dicts']
                    )
                elif key == 'unread_train_stop':
                    pass
                elif key == 'unread_test_request':
                    self.__default_testMainWorkflow.test_assistor_request(
                        value['test_id_dicts']
                    )
                elif key == 'unread_test_match_identifier':
                    self.__default_testMainWorkflow.test_match_identifier(
                        value['test_id_dicts']
                    )
                elif key == 'unread_test_output':
                    self.__default_testMainWorkflow.test_output(
                        value['test_id_dicts']
                    )
                elif key == 'unread_test_stop':
                    pass
            
                # print("category_name: ", category_name, notification_category[category_name])
        return None

    def start_cooperation(self):
        '''
        infinite loop for sponsor training and
        sponsor testing

        Returns
        -------
        None
        '''
        while True:
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
            # print(f'short_polling_res: {short_polling_res}')
            if 'new_token' in short_polling_res and short_polling_res['new_token'] != None:
                new_token = short_polling_res['new_token']
                self.__Authentication_instance.process_token(new_token)

            notification_category = short_polling_res['notification_result']['category']
            distribute_res = self.__distribute_notification(notification_category)
            # 对sponsor来说, 如果是train或者test结束了，中断while loop
            if distribute_res == 'train task finished':
                print('Training task finished')
                return distribute_res
            elif distribute_res == 'test task finished':
                print('Testing task finished')
                return distribute_res

            # sleep 10 seconds
            # time.sleep(2)

    # def start_cooperation(self):
    #     '''
    #     Start short polling
    #     Set indicator to True

    #     Returns
    #     -------
    #     None
    #     '''
    #     # print("self.shortpolling['running']", self.shortpolling['running'])
    #     if self.shortpolling['running'] == False:
    #         self.shortpolling['running'] = True
    #         self.__polling()
    #         print('cooperation starts')
    #     else:
    #         print('short polling has already started')
    #     return 

    def end_cooperation(self):
        '''
        End short polling
        Set indicator to False

        Returns
        -------
        None
        '''
        self.shortpolling['running'] = False
        print('cooperation ends')
        return


    def __unittest_polling(self):
        '''
        Short Polling for new Notifications

        Returns
        -------
        None
        '''
        # print('new polling')
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
        # print(f'short_polling_res: {short_polling_res}')
        if 'new_token' in short_polling_res and short_polling_res['new_token'] != None:
            new_token = short_polling_res['new_token']
            self.__Authentication_instance.process_token(new_token)

        notification_category = short_polling_res['notification_result']['category']
        
        # for unittest, comment back
        return notification_category
        
        self.__distribute_notification(notification_category)

        threading.excepthook = self.handle_thread_exception
        timer = threading.Timer(10, self.__polling)
        timer.start()
        return