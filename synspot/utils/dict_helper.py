from __future__ import annotations

import copy
import collections

from typing import (
    Union
)

from synspot._typing import (
    DictKey,
    DictValue,
    Dict_Store_Type
)

from synspot.error import (
    DuplicateKeyError,
    DictValueNotFound
)

from synspot.utils.dtypes.api import is_list


class DictHelper:

    @classmethod
    def is_key_in_dict(
        cls,
        key: DictKey, 
        container: dict
    ) -> bool:

        if key in container:
            return True
        return False

    @classmethod
    def generate_dict_key(
        cls, 
        user_id: str, 
        task_id: str,
        *args,
    ) -> tuple[str, str]:

        key = [(user_id, task_id)]
        for val in args:
            key.append(val)
        return key

    @classmethod
    def append_type(
        cls,
        key: DictKey, 
        value: Union(dict[DictKey, DictValue], list[DictValue]),
        container: dict[DictKey, DictValue],
    ) -> bool:

        if not DictHelper.is_key_in_dict(key, container):
            container[key] = copy.deepcopy(value)
        else:
            if isinstance(container[key], dict) and isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    container[key][sub_key] = sub_value
            elif isinstance(container[key], list) and isinstance(value, list):
                for sub_value in value:
                    container[key].append(sub_value)
        return True

    @classmethod
    def one_access_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> Union[bool, type[DuplicateKeyError]]:

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

        container[key] = copy.deepcopy(value)
        return True

    @classmethod
    def process_key_recursion(
        cls,
        key: DictKey,
        container: dict[DictKey, DictValue],
    ) -> tuple[DictKey, dict[DictKey, DictValue]]:

        if not is_list(key):
            return key, container

        if len(key) == 1:
            return key[0], container
            
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
        Maintain pointer at the top of the container
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
        store_type: Dict_Store_Type = 'one_access'
    ) -> None:

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
        '''
        print('sub_container1', key, container)
        if len(key) == 1:
            return key[0], container
        
        cur_key = key.pop(0)
        if not DictHelper.is_key_in_dict(key, container):
            '''
            warning: no key in container
            '''
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            for key, val in container.items():
                print('---', key)
            return DictValueNotFound
        container = container[cur_key] 
        print('sub_container', container)
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
        
        if is_list(key):
            temp = container
            key, container = cls.get_value_recursion(
                key=key,
                container=temp
            )
            print('container', container)

        print('____', key, container, container[key])
        if not DictHelper.is_key_in_dict(key, container):
            '''
            warning: no key in container
            '''
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            print('warning: no key in container)')
            for key, val in container.items():
                print('^^^^', key)
            return DictValueNotFound
        
        return container[key]
    
    @classmethod
    def get_all_key_value_pairs(
        cls,
        container: dict[DictKey, DictValue]
    ) -> dict[DictKey, DictValue]:

        return copy.deepcopy(container)