from __future__ import annotations

import collections
from synspot.utils.log.base import BaseLog

from synspot.utils.log.abstract_log import AbstractLog

from synspot.utils.utils import (
    to_string,
)

from synspot.utils.dict_helper import DictHelper

from typing import (
    Union
)

from synspot.utils.dtypes.api import (
    is_list,
    is_dict_like
)


class AlgorithmLog(BaseLog, AbstractLog):
    __AlgorithmLog_instance = None

    def __init__(self):
        self.__algorithm_log = collections.defaultdict(list)

    @classmethod
    def get_instance(cls) -> type[AlgorithmLog]:
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

        key = DictHelper.generate_dict_key(user_id, task_id, log_category)

        if is_list(msgs):
            for msg in msgs:
                msg_str = to_string(msg)
                DictHelper.store_value(
                    key=key,
                    value=msg_str,
                    container=self.__algorithm_log,
                    store_type='append'
                )
        elif is_dict_like(msgs):
            DictHelper.store_value(
                key=key,
                value=msgs,
                container=self.__algorithm_log,
                store_type='append'
            )
        else:
            '''
            error
            '''

        return 

    def get_log(
        self, 
        user_id: str, 
        task_id: str,
        log_category: str='main_test',
    ) -> str:

        key = DictHelper.generate_dict_key(user_id, task_id, log_category)
        
        log = DictHelper.get_value(
            key=key,
            container=self.__algorithm_log,
        )

        log = '\n'.join(log)
        return log

    def get_all_logs(self, user_id):
        pass

    def log_serialization(self):
        pass


