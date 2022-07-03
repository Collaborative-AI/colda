from __future__ import annotations

import copy
import collections
from multiprocessing.sharedctypes import Value

from typing import (
    Union
)

from parso import parse

from colda._typing import (
    DictKey,
    DictValue,
    Dict_Store_Type,
    Parse_Mode
)

from colda.error import (
    DuplicateKeyError,
    DictValueNotFound
)

from colda.utils.dtypes.api import (
    is_dict_like,
    is_list,
    is_tuple,
    to_list,
    to_tuple
)

from collections.abc import Iterable

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
    generate_dict_root_key
    store_value
    get_value
    get_all_key_value_pairs
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
    def generate_dict_root_key(
        cls, 
        user_id: str, 
        task_id: str=None,
        supplement_key: Union[str, list[str], None]=None,
    ) -> tuple[DictKey]:
        '''
        Generate unique dictionary key to 
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
        if task_id == None:
            return (user_id, )
        elif supplement_key == None:
            return (user_id, task_id)

        key = [(user_id, task_id)]
        if is_list(supplement_key):
            for val in supplement_key:
                key.append(val)
        else:
            key.append(supplement_key)
        
        return key
    
    @classmethod
    def generate_dict_supplement_key(
        cls, 
        root_key: tuple[DictKey], 
        supplement_key: Union[str, list[str], None]=None,
    ) -> tuple[DictKey]:
        '''
        Generate unique dictionary key to 
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
        key = [root_key]
        if is_list(supplement_key):
            for val in supplement_key:
                key.append(val)
        else:
            key.append(supplement_key)
        
        return key

    @classmethod
    def __append_type(
        cls,
        key: DictKey, 
        value: Union[dict[DictKey, DictValue], list[DictValue]],
        container: dict[DictKey, DictValue],
    ) -> None:
        '''
        The current container can can append the value 
        to the current key. 
        If the container[key] has already stored value, 
        the new value must be same type as the type of
        container[key]

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
            if is_dict_like(container[key]) and is_dict_like(value):
                for sub_key, sub_value in value.items():
                    container[key][sub_key] = sub_value
            elif is_list(container[key]) and is_list(value):
                for sub_value in value:
                    container[key].append(sub_value)
            else:
                raise ValueError(
                    'value is not matching dict append type, must be list or dict'
                )
        return

    @classmethod
    def __store_once_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> None:
        '''
        The current container can only store the value 
        to the current key once.

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        None
        '''
        if DictHelper.is_key_in_dict(key, container):
            raise DuplicateKeyError(
                'Store once type wrong, you cannot store twice under same key'
            )

        container[key] = copy.deepcopy(value)
        return 
        
    @classmethod
    def __store_multiple_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> None:
        '''
        The current container can store the value 
        to the current key mutiple times(Overwrite old value).

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        None
        '''
        container[key] = copy.deepcopy(value)
        return

    @classmethod
    def __parse_key_recursion(
        cls,
        key: DictKey, 
        container: dict[DictKey, DictValue],
        parse_mode: Parse_Mode
    ) -> DictValue:
        '''
        Handle the situation that user wants to get/store
        value in multi-layer dict. 
        Do the recursion until the we reach the
        final key.

        Parameters
        ----------
        key : DictKey
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        DictValue

        Examples
        --------
        >>> key = ['1', '2']
        >>> container = {'1': {'2': '3'}}
        >>> DictHelper.get_value_recursion(key, container)
        key '2'
        container {'2': '3'}
        '''
        # print('keyeee', key, type(key))
        # single key
        if len(key) == 1:
            if not DictHelper.is_key_in_dict(key[0], container) and parse_mode == 'get':                    
                raise DictValueNotFound(
                    f'Key not in container: {key[0]}'
                )
            return key[0], container
        
        cur_key = key.pop(0)
        if not DictHelper.is_key_in_dict(cur_key, container):
            if parse_mode == 'store':
                # if the parse_mode is store,
                # we need to initiate container
                # to empty dict
                container[cur_key] = {}
            else:
                raise DictValueNotFound(
                    f'Key not in container: {cur_key}'
                )
        container = container[cur_key] 
        
        return cls.__parse_key_recursion(
            key=key,
            container=container,
            parse_mode=parse_mode
        )

    @classmethod
    def __parse_key(
        cls,
        key: Union[tuple[DictKey], Iterable[DictKey]],
        container: dict[DictKey, DictValue],
        parse_mode: Parse_Mode,
    ) -> tuple[DictKey, dict[DictKey, DictValue]]:
        '''
        Handle the situation that user wants to get/store
        value in multi-layer dict. 
        Create a temp container to maintain pointer
        at the top of the container.
        
        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        bool

        Notes
        -----
        Remember to maintain the container pointer at the top:
        temp = container
        '''
        if is_tuple(key):
            if not DictHelper.is_key_in_dict(key, container) and parse_mode == 'get':                    
                raise DictValueNotFound('Key not in container')
            return key, container
        temp = container
        return cls.__parse_key_recursion(
            key=key,
            container=temp,
            parse_mode=parse_mode,
        )
        
    @classmethod
    def store_value(
        cls,
        key: Union[tuple[DictKey], Iterable[DictKey]], 
        value: DictValue,
        container: dict[DictKey, DictValue],
        store_type: Dict_Store_Type='store_once'
    ) -> None:
        '''
        Store value in dict

        Parameters
        ----------
        key : DictKey
        value : Union[dict[DictKey, DictValue], list[DictValue]]
        container : dict[DictKey, DictValue]
        store_type : Dict_Store_Type
            We have different store type to handle different situations

        Returns
        -------
        None
        '''
        key, container = cls.__parse_key(
            key=key, 
            container=container,
            parse_mode='store'
        )
        if store_type == 'store_once':
            return cls.__store_once_type(
                key=key, 
                value=value, 
                container=container
            )
        elif store_type == 'append':
            return cls.__append_type(
                key=key, 
                value=value, 
                container=container
            )
        elif store_type == 'store_multiple':
            return cls.__store_multiple_type(
                key=key, 
                value=value, 
                container=container
            )
        else:
            raise ValueError('store type wrong')

    @classmethod
    def get_value(
        cls,
        key: Union[tuple[DictKey], Iterable[DictKey]], 
        container: dict[DictKey, DictValue]
    ) -> DictValue:
        '''
        Get value corresponding to the key in dict.
        
        Parameters
        ----------
        key : DictKey
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        DictValue
        '''
        key, container = cls.__parse_key(
            key=key,
            container=container,
            parse_mode='get'
        )
        
        return container[key]
    
    @classmethod
    def get_all_key_value_pairs(
        cls,
        container: dict[DictKey, DictValue]
    ) -> dict[DictKey, DictValue]:
        '''
        Return all data in current container

        Parameters
        ----------
        container : dict[DictKey, DictValue]
        
        Returns
        -------
        dict
        '''
        return copy.deepcopy(container)