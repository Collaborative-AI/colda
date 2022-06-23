from __future__ import annotations

import copy
import collections
from colda.utils.log.base import BaseLog

from colda.utils.log.abstract_log import AbstractLog

from colda.utils.utils import (
    to_string,
)

from colda.utils.dict_helper import DictHelper

from colda.utils.dtypes.api import (
    is_list,
    is_dict_like
)
from typeguard import typechecked


#@typechecked
class WorkflowLog(BaseLog, AbstractLog):
    '''
    Workflow log is used to store the information
    from the workflow stage(train_workflow and
    test_workflow).

    Attributes
    ----------
    None

    Methods
    -------
    get_instance
    store_log
    get_log
    get_all_logs
    '''

    __WorkflowLog_instance = None

    def __init__(self):
        self.__workflow_log = collections.defaultdict(list)

    @classmethod
    def get_instance(cls) -> WorkflowLog:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        WorkflowLog
        '''
        if cls.__WorkflowLog_instance == None:
            cls.__WorkflowLog_instance = WorkflowLog()

        return cls.__WorkflowLog_instance

    def store_log(
        self, 
        user_id: str, 
        task_id: str, 
        msgs: list[str]
    ) -> None:
        '''
        Store msgs to log.

        Parameters
        ----------
        user_id : str
        task_id : str
        msgs : list[str]
        log_category : str='main_test'

        Returns
        -------
        None
        '''
        # generate unique key
        key = DictHelper.generate_unique_dict_key(user_id, task_id)

        if is_list(msgs):
            for msg in msgs:
                msg_str = to_string(msg)
                DictHelper.store_value(
                    key=key,
                    value=msg_str,
                    container=self.__workflow_log,
                    store_type='append'
                )
        elif is_dict_like(msgs):
            DictHelper.store_value(
                key=key,
                value=msgs,
                container=self.__workflow_log,
                store_type='append'
            )
        else:
            '''
            error
            '''

        return 

    def get_log(
        self, user_id: str, task_id: str
    ) -> str:
        '''
        get msgs from log.

        Parameters
        ----------
        user_id : str
        task_id : str
        msgs : list[str]
        log_category : str='main_test'

        Returns
        -------
        None
        '''
        # generate unique key
        key = DictHelper.generate_unique_dict_key(
            user_id=user_id, 
            task_id=task_id
        )

        log = DictHelper.get_value(
            key=key,
            container=self.__workflow_log,
        )

        if is_list(log):
            log = '\n'.join(log)

        return log

    def get_all_logs(self):
        '''
        For unittest, change this function later
        '''
        return copy.deepcopy(self.__workflow_log)

    def log_serialization(self):
        pass



    