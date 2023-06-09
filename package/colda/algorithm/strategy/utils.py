from __future__ import annotations

import json

from algorithm.strategy.dp import DP

from functools import wraps

from typing import Callable

from typeguard import typechecked

from _typing import Serializable_Datatype


# @typechecked
def algorithm_process(
    func: Callable
) -> Callable:
    '''
    Wrapper that has following properties:
        1. Process the input that pass into
        all the algorithm methods. Mainly change
        list to np.array
        2. Process the output that generated from
        all the algorithm methods. Mainly change
        np.array to list

    Parameters
    ----------
    func : Callable

    Returns
    -------
    JSONType
    '''
    @wraps(func)
    def wrapper(
        *args, **kwargs
    ) -> Serializable_Datatype:
        '''
        Notes
        -------
        *args used to handle self,
        **kwargs used to handle parameters
        '''
        kwargs = DP.process_input(**kwargs)
        res = func(*args, **kwargs)  
        res = DP.process_output(res)
        return res

    return wrapper