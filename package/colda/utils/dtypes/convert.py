from __future__ import annotations

import copy
import numpy as np
import pandas as pd

from typing import Any

from collections.abc import Iterable

from utils.dtypes.inference import (
    is_numpy,
    is_set
)

from _typing import Serializable_Datatype

from error import DataNotSerializable


def to_list(data: Iterable) -> list:
    '''
    Change iterable data to list
    
    Parameters
    ----------
    data : Any

    Returns
    -------
    list
    '''
    return list(data)

def to_string(
    data: Any
) -> str:
    '''
    Change data to str
    
    Parameters
    ----------
    data : Any

    Returns
    -------
    str
    '''
    return str(data)

def to_tuple(data: Iterable) -> str:
    '''
    Change iterable data to tuple
    
    Parameters
    ----------
    data : Any

    Returns
    -------
    tuple
    '''
    return tuple(data)

def to_serializable(
    data: Any
) -> Serializable_Datatype:
    '''
    Change data to serializable data:
        1. convert numpy type to list
        2. convert set to list

    Parameters
    ----------
    data : Any

    Returns
    -------
    Serializable_Datatype
    '''
    # print(f'smdata: {data}, {type(data)}')
    if is_numpy(data):
        return copy.deepcopy(data.tolist())
    elif is_set(data):
        return copy.deepcopy(list(data))
    else:
        raise DataNotSerializable('Can only convert numpy and set type data')