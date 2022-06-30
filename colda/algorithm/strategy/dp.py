import numpy as np

import copy

from colda.algorithm.model.api import Model

from colda.utils.api import Serialization

from colda.utils.dtypes.api import (
    is_numpy,
    is_list,
    is_tuple,
    is_dict_like,
    is_integer,
    is_float,
    to_list
)

from colda._typing import Serializable_Datatype

from typing import (
    Tuple,
    Any,
    Union
)

from typeguard import typechecked


#@typechecked
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
        res: tuple[Any],
    ) -> Serializable_Datatype:  
        '''
        Process the output that generated from
        all the algorithm methods. 
        
        All the output are tuple form. We first
        change the tuple to list form, then process
        the each element in the list

        Parameters
        ----------
        res : tuple[Any]

        Returns
        -------
        Serializable_Datatype
        '''
        if is_tuple(res):
            res = to_list(res)
        else:
            raise ValueError(
                'Output from Algorithm part must be tuple'
            )

        if len(res) == 1:
            return Serialization.make_data_serializable(data=res[0])

        for i in range(len(res)):
            # If the output is model, we only need to store it
            # in db dict. We do not need to transfer it.
            if type(res[i]) != Model:
                res[i] = Serialization.make_data_serializable(data=res[i])
            
        return res




