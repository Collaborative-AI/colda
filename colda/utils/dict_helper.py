from __future__ import annotations

import copy
import collections
from multiprocessing.sharedctypes import Value

from typing import (
    Union
)

from colda._typing import (
    DictKey,
    DictValue,
    Dict_Store_Type
)

from colda.error import (
    DuplicateKeyError,
    DictValueNotFound
)

from colda.utils.dtypes.api import (
    is_list,
    to_list,
    to_tuple
)

from typeguard import typechecked


#@typechecked
class DictHelper:
    '''
    Handle dictionary structure mainly
    for following 2 scenarios:
        1. Database
        2. Log

    Attributes
    ----------
    None

    Methods
    -------
    is_key_in_dict
    generate_unique_dict_key
    append_type
    one_access_type
    multiple_access_type
    process_key_recursion
    process_key
    store_value
    get_value_recursion
    get_value
    '''

    @classmethod
    def is_key_in_dict(
        cls,
        key: DictKey, 
        container: dict
    ) -> bool:
        '''
        check if key is in dict

        Parameters
        ----------
        key : DictKey
        container : dict
        
        Returns
        -------
        bool
        '''
        if key in container:
            return True
        return False

    @classmethod
    def generate_unique_dict_key(
        cls, 
        user_id: str, 
        task_id: str,
        supplement_key: Union[str, list[str], None]=None,
    ) -> tuple[str]:
        '''
        generate unique dictionary key to 
        store imformation for each task

        Parameters
        ----------
        user_id : str
        task_id : str
        supplement_key : Union[str, list[str], None]=None
        
        Returns
        -------
        tuple[str]
        '''
        if supplement_key == None:
            return (user_id, task_id)

        key = [user_id, task_id]
        if is_list(supplement_key):
            for val in supplement_key:
                key.append(val)
        else:
            key.append(supplement_key)
        
        return to_tuple(key)

    @classmethod
    def append_type(
        cls,
        key: DictKey, 
        value: Union[dict[DictKey, DictValue], list[DictValue]],
        container: dict[DictKey, DictValue],
    ) -> None:
        '''
        generate unique dictionary key
        to store imformation of each task

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        None
        '''
        # store the value of the current key for the first time
        if not DictHelper.is_key_in_dict(key, container):
            container[key] = copy.deepcopy(value)
        else:
            if isinstance(container[key], dict) and isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    container[key][sub_key] = sub_value
            elif isinstance(container[key], list) and isinstance(value, list):
                for sub_value in value:
                    container[key].append(sub_value)
            else:
                raise ValueError(
                    'value is not matching dict append type, must be list or dict'
                )

        return

    @classmethod
    def one_access_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> Union[bool, type[DuplicateKeyError]]:
        '''
        Generate unique dictionary key
        to store imformation of each task

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        if not DictHelper.is_key_in_dict(key, container):
            container[key] = copy.deepcopy(value)
            return True
        else:
            return DuplicateKeyError

    @classmethod
    def multiple_access_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> Union[bool, type[DuplicateKeyError]]:
        '''
        generate unique dictionary key
        to store imformation of each task

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        container[key] = copy.deepcopy(value)
        return True

    @classmethod
    def process_key_recursion(
        cls,
        key: DictKey,
        container: dict[DictKey, DictValue],
    ) -> tuple[DictKey, dict[DictKey, DictValue]]:
        '''
        generate unique dictionary key
        to store imformation of each task

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        if not is_list(key):
            return key, container

        if len(key) == 1:
            return key[0], container
        
        print('keyyyy', key)
        if not DictHelper.is_key_in_dict(key[0], container):
            container[key[0]] = {}
    
        container = container[key.pop(0)]    
        return cls.process_key(
            key=key,
            container=container
        )

    @classmethod
    def process_key(
        cls,
        key: DictKey,
        container: dict[DictKey, DictValue],
    ) -> tuple[DictKey, dict[DictKey, DictValue]]:
        '''
        Create a temp container to maintain pointer
        at the top of the container

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''

        temp = container
        return cls.process_key_recursion(
            key=key,
            container=temp
        )
        
    @classmethod
    def store_value(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue],
        store_type: Dict_Store_Type='one_access'
    ) -> None:
        '''
        Maintain pointer at the top of the container

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        key, container = cls.process_key(key, container)
        if store_type == 'one_access':
            return cls.one_access_type(key, value, container)
        elif store_type == 'append':
            return cls.append_type(key, value, container)
        elif store_type == 'multiple_access':
            return cls.multiple_access_type(key, value, container)
        else:
            print('store type wrong')
        return

    @classmethod
    def get_value_recursion(
        cls,
        key: DictKey, 
        container: dict[DictKey, DictValue]
    ) -> DictValue:
        '''
        Maintain pointer at the top of the container

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        # print('sub_container1', key, container)
        if len(key) == 1:
            return key[0], container
        
        cur_key = key.pop(0)
        if not DictHelper.is_key_in_dict(cur_key, container):
            return DictValueNotFound, DictValueNotFound
        container = container[cur_key] 
        
        return cls.get_value_recursion(
            key=key,
            container=container
        )
        
    @classmethod
    def get_value(
        cls,
        key: DictKey, 
        container: dict[DictKey, DictValue]
    ) -> DictValue:
        '''
        Maintain pointer at the top of the container

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        if is_list(key):
            temp = container
            key, container = cls.get_value_recursion(
                key=key,
                container=temp
            )

        if not DictHelper.is_key_in_dict(key, container):
            raise DictValueNotFound
        
        return container[key]
    
    @classmethod
    def get_all_key_value_pairs(
        cls,
        container: dict[DictKey, DictValue]
    ) -> dict[DictKey, DictValue]:
        '''
        Maintain pointer at the top of the container

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool
        '''
        return copy.deepcopy(container)