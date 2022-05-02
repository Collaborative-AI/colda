from __future__ import annotations

import collections
from synspot.utils.log.base import BaseLog

from synspot.utils.log.abstract_log import AbstractLog

from synspot.utils.utils import (
    to_string,
)

from synspot.utils.dict_helper import DictHelper


class WorkflowLog(BaseLog, AbstractLog):
    __WorkflowLog_instance = None

    def __init__(self):
        self.__workflow_log = collections.defaultdict(list)

    @classmethod
    def get_instance(cls) -> type[WorkflowLog]:
        if cls.__WorkflowLog_instance == None:
            cls.__WorkflowLog_instance = WorkflowLog()

        return cls.__WorkflowLog_instance

    def store_log(
        self, 
        user_id: str, 
        task_id: str, 
        msgs: list[str]
    ) -> None:

        key = DictHelper.generate_dict_key(user_id, task_id)
        if not DictHelper.is_key_in_dict(key, self.__workflow_log):
            self.__workflow_log[key] = collections.defaultdict(list)

        if isinstance(msgs, list):
            for msg in msgs:
                msg_str = to_string(msg)
                DictHelper.store_value(
                    key=key,
                    value=msg_str,
                    container=self.__workflow_log,
                    store_type='append'
                )
        else:
            '''
            error
            '''            
            pass

        return 

    def get_log(
        self, user_id: str, task_id: str
    ) -> str:

        key = DictHelper.generate_dict_key(user_id, task_id)
        log = DictHelper.get_value(
            key=key,
            container=self.__workflow_log,
        )

        log = '\n'.join(log)
        return log

    def get_all_logs(self, user_id):
        pass

    def log_serialization(self):
        pass



    