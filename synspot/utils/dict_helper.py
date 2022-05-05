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

from synspot.error import DuplicateKeyError

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
        cls, user_id: str, task_id: str
    ) -> tuple[str, str]:

        return (user_id, task_id)

    @classmethod
    def append_type(
        cls,
        key: DictKey, 
        value: Union(dict[DictKey, DictValue], list[DictValue]),
        container: dict[DictKey, DictValue],
    ) -> bool:

        if key not in container:
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
        if key not in container:
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
    def store_value(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue],
        store_type: Dict_Store_Type = 'one_access'
    ) -> None:

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
    def get_value(
        cls,
        key: DictKey, 
        container: dict[DictKey, DictValue]
    ) -> DictValue:
        
        if key not in container:
            '''
            warning: no key in container
            '''
            print(')))', key)
            for key, val in container.items():
                print('^^^^', key, val)
            return 
        
        return container[key]
    
    @classmethod
    def get_all_key_value_pairs(
        cls,
        container: dict[DictKey, DictValue]
    ) -> dict[DictKey, DictValue]:
        return copy.deepcopy(container)