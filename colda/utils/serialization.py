from __future__ import annotations

import json
import copy
import numpy as np

from typing import (
    Any
)

from utils.dtypes.api import (
    is_numpy,
    is_dict_like,
    is_list,
    is_serializable,
    to_serializable
)

from _typing import Serializable_Datatype

from typeguard import typechecked


#@typechecked
class Serialization:

    @classmethod
    def make_data_serializable(
        cls,
        data: Any
    ) -> Serializable_Datatype:
        '''
        Change data type to serializable data
        type

        Parameters
        ----------
        data : Any

        Returns
        -------
        Serializable_Datatype
        '''
        # if data is None, return None
        if data is None:
            return None

        # if data is serializable, 
        # return deepcopy of it
        if is_serializable(data):
            return copy.deepcopy(data)

        # if the data is dict like and it contains
        # non-serializable data, call recursion
        if is_dict_like(data):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = cls.make_data_serializable(data=value)
            return processed_data 
        # if the data is list and it contains
        # non-serializable data, call recursion
        elif is_list(data):
            processed_data = []
            for item in data:
                processed_data.append(cls.make_data_serializable(data=item))
            return processed_data 
        # data might be empty set, etc.
        else:
            return to_serializable(data)
