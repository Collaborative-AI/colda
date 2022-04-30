from __future__ import annotations

import collections
from synspot.utils.log.base import BaseLog

from synspot.utils.log.abstract_log import AbstractLog

from synspot.utils.utils import (
    to_string,
    generate_dict_key
)

from synspot.utils.dict_helper import DictHelper

from typing import (
    Union
)


class AlgorithmLog(BaseLog, AbstractLog):
    __AlgorithmLog_instance = None

    def __init__(self):
        self.__algorithm_log = collections.defaultdict(dict)

    @classmethod
    def get_AlgorithmLog_instance(cls) -> type[AlgorithmLog]:
        if cls.__AlgorithmLog_instance == None:
            cls.__AlgorithmLog_instance = AlgorithmLog()

        return cls.__AlgorithmLog_instance

    def store_log(
        self, 
        user_id: str, 
        task_id: str, 
        msgs: list[str]
    ) -> None:

        key = generate_dict_key(user_id, task_id)
        if not DictHelper.is_key_in_dict(user_id, self.__algorithm_log):
            self.__algorithm_log[user_id] = collections.defaultdict(list)

        if isinstance(msgs, list):
            for msg in msgs:
                msg_str = to_string(msg)
                self.__algorithm_log[user_id][task_id].append(msg_str)
        else:
            pass

        return 

    def get_log(
        self, user_id, task_id
    ) -> str:

        pass

    def get_all_logs(self, user_id):
        pass

    def log_serialization(self):
        pass


