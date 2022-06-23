from __future__ import annotations

import numpy as np
import pandas as pd

from pandas.api.types import is_dict_like as pandas_is_dict_like
from pandas.api.types import is_integer as pandas_is_integer
from pandas.api.types import is_list_like as pandas_is_list_like
from pandas.api.types import is_float as pandas_is_float

from typing import Any

from typeguard import typechecked


#@typechecked
def is_numpy(obj: Any) -> bool:
    '''
    Check if obj is numpy
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return isinstance(obj, (np.ndarray, np.generic))

#@typechecked
def is_dict_like(obj: Any) -> bool:
    '''
    Check if obj is dict like
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return pandas_is_dict_like(obj)

#@typechecked
def is_list_like(obj: Any) -> bool:
    '''
    Check if obj is list like
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return pandas_is_list_like(obj)

#@typechecked
def is_tuple(obj: Any) -> bool:
    '''
    Check if obj is tuple
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return isinstance(obj, tuple)

#@typechecked
def is_list(obj: Any) -> bool:
    '''
    Check if obj is list
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return isinstance(obj, list)

#@typechecked
def is_integer(obj: Any) -> bool:
    '''
    Check if obj is integer
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return pandas_is_integer(obj)

#@typechecked
def is_float(obj: Any) -> bool:
    '''
    Check if obj is float
    
    Parameters
    ----------
    obj : Any

    Returns
    -------
    bool
    '''
    return pandas_is_float(obj)



