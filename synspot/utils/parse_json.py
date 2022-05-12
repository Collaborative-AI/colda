from __future__ import annotations

import json
import copy
import numpy as np

from synspot._typing import Serializable_Datatype

from typing import (
    Any
)

from synspot.utils.dtypes.api import (
    is_numpy,
    is_dict_like,
    is_list
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

        try:
            json.loads(data)
        except:
            return False
        else:
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
        
        if not is_dict_like(data):
            return copy.deepcopy(data)

        processed_data = {}
        for key, value in data.items():
            processed_data[key] = cls.load_json_recursion(value)    

        return processed_data
    
    @classmethod
    def is_serializable(
        cls,
        data: Any
    ) -> bool:

        # if isinstance(data, (np.ndarray, np.generic)):
        #     return False
        # return True

        try:
            json.dumps(data)
        except:
            return False
        else:
            return True

    @classmethod
    def change_datatype_to_serializable(
        cls,
        data: Any
    ) -> Serializable_Datatype:

        if is_numpy(data):
            return copy.deepcopy(data.tolist())
            
        return data

    @classmethod
    def make_data_serializable(
        cls,
        data: Any
    ) -> Serializable_Datatype:

        '''
        Change all np.array to list
        '''

        if data is None:
            return None

        if cls.is_serializable(data) and not is_dict_like(data):
            return copy.deepcopy(data)
        
        # data = cls.change_datatype_to_serializable(data)

        # processed_data = None
        if is_dict_like(data):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = cls.make_data_serializable(value)
            print('~processed_data', processed_data)    
            return processed_data 
        else:
            return cls.change_datatype_to_serializable(data)
