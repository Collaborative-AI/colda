from __future__ import annotations

import copy

from typing import (
    final,
    Any
)

from synspot.error import DictValueNotFound

from synspot.utils.dtypes.api import is_numpy


class BaseDatabase:
    """
    Base class for Algorithm
    """

    # TODO: implement methods
    @final
    def placeholder(self):
        pass
    # def get_all_records(self, temp_database) -> dict[tuple[str, str], Any]:
    #     return copy.deepcopy(temp_database) 
   
    @final
    @classmethod
    def dict_value_not_found(cls) -> type[DictValueNotFound]:
        return DictValueNotFound
    
    # @final
    # @classmethod
    # def handle_db_return_datatype(
    #     cls,
    #     *args
    # ) -> None:

    #     args = [val.tolist() if is_numpy(val) else val for val in args]
    #     return args

    @final
    @classmethod
    def if_db_response_valid(
        cls, *args
    ) -> bool:
        # print('if_response_valid', args)

        # args = cls.handle_db_return_datatype(*args)
        # print('if_response_valid', args)
        if cls.dict_value_not_found() in args:
            return False
        return True
