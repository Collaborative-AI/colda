""" basic inference routines """

from collections import abc
from numbers import Number
import re
from typing import Pattern
import warnings

import numpy as np
import pandas as pd

from pandas.api.types import is_dict_like as pandas_is_dict_like
from pandas.api.types import is_integer as pandas_is_integer
from pandas.api.types import is_list_like as pandas_is_list_like
# from pandas.api.types import is_integer as pandas_is_integer

def is_numpy(obj) -> bool:
    return isinstance(obj, (np.ndarray, np.generic))

def is_dict_like(obj) -> bool:
    return pandas_is_dict_like(obj)

def is_list_like(obj) -> bool:
    return pandas_is_list_like(obj)

def is_tuple(obj) -> bool:
    return isinstance(obj, tuple)

def is_list(obj) -> bool:
    return isinstance(obj, list)