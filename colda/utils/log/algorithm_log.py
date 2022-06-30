from __future__ import annotations

import copy
import collections
from colda.utils.log.base import BaseLog

from colda.utils.log.abstract_log import AbstractLog

from colda.utils.dict_helper import DictHelper

from typing import (
    Union
)

from colda.utils.dtypes.api import (
    is_list,
    is_dict_like
)

from typeguard import typechecked


#@typechecked
class AlgorithmLog(BaseLog, AbstractLog):
    '''
    Algorithm log is used to store the information
    from the algorithm stage.

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

    __AlgorithmLog_instance = None

    def __init__(self):
        self.__algorithm_log = collections.defaultdict(list)

    @classmethod
    def get_instance(cls) -> AlgorithmLog:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        AlgorithmLog
        '''
        if cls.__AlgorithmLog_instance == None:
            cls.__AlgorithmLog_instance = AlgorithmLog()

        return cls.__AlgorithmLog_instance

    def store_log(
        self, 
        user_id: str, 
        task_id: str, 
        msgs: list[str],
        log_category: str='main_test',
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
        key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=task_id, 
            suppliment_key=log_category
        )
        
        DictHelper.store_value(
            key=key,
            value=msgs,
            container=self.__algorithm_log,
            store_type='append'
        )

        return 

    def get_log(
        self, 
        user_id: str, 
        task_id: str,
        log_category: str='main_test',
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
        key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=task_id, 
            suppliment_key=log_category
        )
        
        log = DictHelper.get_value(
            key=key,
            container=self.__algorithm_log,
        )

        if is_list(log):
            log = '\n'.join(log)

        return log

    def get_all_logs(self):
        '''
        For unittest, change this function later
        '''
        return copy.deepcopy(self.__algorithm_log)

    def log_serialization(self):
        pass


