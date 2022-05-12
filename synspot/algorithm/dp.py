import numpy as np

import copy

from synspot.utils import ParseJson

from synspot.utils.dtypes.api import (
    is_numpy,
    is_list,
    is_tuple,
    is_dict_like,
    is_integer,
    is_float
)

from synspot._typing import Serializable_Datatype

from typing import (
    Tuple,
    Any,
    Union
)


class DP:

    '''
    class for data processing
    '''

    @classmethod
    def process_input_recursion(
        cls,
        data: Any,
    ):

        '''
        Change list to np.array
        '''
        
        if data is None:
            return None
        
        if is_dict_like(data):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = cls.process_input_recursion(value)    
        elif is_list(data):
            processed_data = []
            for i in range(len(data)):
                processed_data.append(cls.process_input_recursion(data[i])) 
            # if not is_numpy(processed_data):
            #     print('processed_data', processed_data, type(processed_data), type(processed_data[0])) 
            processed_data = np.array(processed_data, dtype=type(processed_data[0]))
            # print(f'new_type: {type(processed_data[0])}')
        else:
            return data

        return copy.deepcopy(processed_data)

    @classmethod
    def process_input(
        cls,
        **kwargs
    ):
        for key, val in kwargs.items():
            print('~~~!@~!', key, val)
            kwargs[key] = cls.process_input_recursion(val)
        
        return kwargs

    @classmethod
    def process_output(
        cls,
        res: Union[Any, Tuple[Any]],
    ) -> Serializable_Datatype:  

        if is_tuple(res):
            res = list(res)

        if len(res) == 1:
            return ParseJson.make_data_serializable(res[0])

        for i in range(len(res)):
            res[i] = ParseJson.make_data_serializable(res[i])
            
        return res




