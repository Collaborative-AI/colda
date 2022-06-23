from __future__ import annotations

import copy
import numpy as np
import pandas as pd

from typing import Any

from collections.abc import Iterable

from colda.utils.dtypes.inference import (
    is_numpy,
    is_set
)

from colda._typing import Serializable_Datatype


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
    if is_numpy(data):
        return copy.deepcopy(data.tolist())
    elif is_set(data):
        return copy.deepcopy(list(data))

    return data