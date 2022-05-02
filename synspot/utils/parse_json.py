from __future__ import annotations

import json

from typing import (
    Any
)


class ParseJson:

    @classmethod
    def is_json(
        cls,
        data: Any
    ) -> bool:

        """
        start task with all assistors

        :param file_address: Integer. Maximum training round
        :param file_content: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        if isinstance(data, list):
            return False
        elif isinstance(data, int):
            return False
        elif isinstance(data, tuple):
            return False    
        elif isinstance(data, dict):
            return False

        try:
            json.loads(data)
        except:
            return False

        return True

    @classmethod
    def load_json_recursion(
        cls,
        data: Any,
    ) -> dict[Any]:

        if data is None:
            return None

        if cls.is_json(data):
            data = json.loads(data)
        
        if not isinstance(data, dict):
            return data

        processed_data = {}
        for key, value in data.items():
            processed_data[key] = cls.load_json_recursion(value)    

        return processed_data