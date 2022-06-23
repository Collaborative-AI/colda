from __future__ import annotations

import numpy as np
import pandas as pd

from pandas.api.types import is_dict_like as pandas_is_dict_like
from pandas.api.types import is_integer as pandas_is_integer
from pandas.api.types import is_list_like as pandas_is_list_like
from pandas.api.types import is_float as pandas_is_float

from typing import Any

from collections.abc import Iterable


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
    str
    '''
    hasattr(name, '__iter__')
    return tuple(data)
