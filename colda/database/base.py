from __future__ import annotations

import copy

from typing import (
    final,
    Any
)

from colda.error import DictValueNotFound

from colda.utils.dtypes.api import is_numpy

from typeguard import typechecked


#@typechecked
class BaseDatabase:
    """
    Base class for Algorithm
    """

    # TODO: implement methods
    @final
    def placeholder(self):
        pass

   
    @final
    @classmethod
    def dict_value_not_found(cls) -> type[DictValueNotFound]:
        return DictValueNotFound

    @final
    @classmethod
    def if_db_response_valid(
        cls, *args
    ) -> bool:
        if cls.dict_value_not_found() in args:
            return False
        return True
