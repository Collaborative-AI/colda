from gettext import find
from unittest import skip
import numpy as np
import requests
import threading
import json
import os
import time
import argparse
import subprocess

from synspot.workflow.abstract_workflow import AbstractTrainMainWorkflow

from ..utils import log_helper, load_json_data, load_file, save_file, handle_Algorithm_return_value, check_sponsor_class, obtain_notification_information


from typing import (
    Tuple
)


class TrainMainWorkflow(AbstractTrainMainWorkflow):
    __TrainMainWorkflow_instance = None

    def __init__(self):
        
        self.maxRound = 2
        self.skip_header_default = 1
        self.initial_round = 1
        self.test_indicator = 'train'
        # self.assistor_task_mode = 'regression'
        # self.exe_position = self.PersonalInformation_instance.exe_position
        # self.root = self.PersonalInformation_instance.root

    @classmethod
    def get_TrainMainWorkflow_instance(cls):
        if cls.__TrainMainWorkflow_instance == None:
            cls.__TrainMainWorkflow_instance = TrainMainWorkflow()

        return cls.__TrainMainWorkflow_instance        

    def find_assistor(
        self, 
        maxRound: int, 
        assistors: list, 
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        train_target_column: str, 
        task_mode: str, 
        model_name: str, 
        metric_name: str, 
        task_name: str = None, 
        task_description: str = None
    ) -> None:
        
        """
        start task with all assistors

        :param maxRound: Integer. Maximum training round
        :param assistors: List. The List of assistors' usernames
        :param train_file_path: String. Input path address of training data path
        :param train_id_column: String. ID column of Input File
        :param train_data_column: String. Data column of Input File
        :param train_target_column: String. Target column of Input File
        :param task_mode: String. Classification or Regression
        :param model_name: String. Specific model, such as ``LinearRegression``, ``DecisionTree``.
        :param metric_name: String. Metric to measure the result, such as ``MAD``, ``RMSE``, ``R2``.
        :param task_name: None or String. The name of current task.
        :param task_description: None or String. The description of current task

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        return TrainSponsorFindAssistor.find_assistor(
            maxRound=self.maxRound,
            assistors=assistors,
            train_file_path=train_file_path,
            train_id_column=train_id_column,
            train_data_column=train_data_column,
            train_target_column=train_target_column,
            task_mode=task_mode,
            model_name=model_name,
            metric_name=metric_name,
            task_name=task_name,
            task_description=task_description
        )
        

    def train_assistor_request(self, task_id_dict: dict):

        """
        Handle the unread request for three default mode: ["passive", "active", "auto"]

        :param task_id_dict: Dictionary.

        :returns: String. 'unread_request successfully'

        :exception OSError: Placeholder.
        """

        # obtain some important information
        user_id, root, token = self.__obtain_important_information()
        
        

    def train_match_identifier(self, task_id_dict: dict):

        """
        Handle the unread_match_identifier. Consider sponsor and assistor, different functions will be called

        :param task_id_dict: Dictionary.

        :returns: String. 'unread match id done'

        :exception OSError: Placeholder.
        """

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        # cur_unread_match_identifier_Taskid_dict = unread_match_identifier_notification["check_dict"]
        for task_id in task_id_dict:
            sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict_value=task_id_dict[task_id])
            msg = ["---- 3. Unread Match ID\n", "3.1 Update the match id notification\n"]
            log_helper(msg, root, user_id, task_id)

            if role == check_sponsor_class.sponsor:
                msg = ["3.2 unread_match_identifier_sponsor\n"]
                log_helper(msg, root, user_id, task_id)

                self.unread_match_identifier_sponsor(task_id)
            elif role == check_sponsor_class.assistor:
                msg = ["3.2 unread_match_identifier_assistor\n"]
                log_helper(msg, root, user_id, task_id)

                self.unread_match_identifier_assistor(task_id)

        return 'unread match id done'

    def train_sponsor_match_identifier(self, task_id: str):

        """
        Handle the unread_match_identifier of sponsor.

        :param task_id: String.

        :returns: String. 'unread_match_identifier_sponsor successfully'

        :exception OSError: Placeholder.
        """

        # obtain some information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        

    def train_assistor_match_identifier(self, task_id: str):

        """
        Handle the unread_match_identifier of assistor.

        :param task_id: String.

        :returns: String. 'unread_match_identifier_assistor successfully'

        :exception OSError: Placeholder.
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        

    def train_situation(self, task_id_dict: dict):

        """
        Handle the unread_situation. Two situations needed to be considered: sponsor and assistor

        :param task_id_dict: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        # obtain important information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        for task_id in task_id_dict:
            sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict_value=task_id_dict[task_id])
            msg = ["---- 4. Unread Situation\n", "4.1 Update the situation notification\n"]
            log_helper(msg, root, user_id, task_id)

            if role == check_sponsor_class.sponsor:
                self.unread_situation_sponsor(task_id, cur_rounds_num)
            elif role == check_sponsor_class.assistor:
                self.unread_situation_assistor(task_id, cur_rounds_num)

        return 'unread situation done'


    def train_sponsor_situation(self, task_id: str, rounds: int):

        """
        Handle the unread situation of sponsor.

        :param task_id: String. The task needed to be handled.
        :param rounds: Integer. Current round.

        :returns: None

        :exception OSError: Placeholder.
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)
        
        

    def train_assistor_situation(self, task_id: str, rounds: int):

        """
        Handle the unread situation of assistor.

        :param task_id: String. The task needed to be handled.
        :param rounds: Integer. Current round.
 
        :returns: None

        :exception OSError: Placeholder.
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

       

    def train_output(self, task_id_dict: dict):

        """
        Handle the unread_output.

        :param task_id_dict: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)
        for task_id in task_id_dict:
            sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict_value=task_id_dict[task_id])
            msg = ["---- 5. Unread Output\n", "5.1 Update the output notification\n"]
            log_helper(msg, root, user_id, task_id)

            self.unread_output_singleTask(task_id, cur_rounds_num)
            
        return 'unread output done'

    

    def stop_train(self, unread_train_stop_notification: dict):
        """
        Stop Train and delete related files

        :param unread_train_stop_notification: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        return






