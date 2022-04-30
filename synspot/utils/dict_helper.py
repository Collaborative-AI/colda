import copy
import collections

from typing import (
    Any,
    Hashable,
    TypeVar,
    Literal,
    Union
)

DictKey = TypeVar('DictKey', bound=Hashable)
DictValue = TypeVar("DictValue", bound=Any)
Store_Type = Literal['append', 'one_access']


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
    ) -> None:

        if key not in container:
            container[key] = copy.deepcopy(value)
        else:
            if isinstance(container[key], dict) and isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    container[key][sub_key] = sub_value
            elif isinstance(container[key], list) and isinstance(value, list):
                for sub_value in value:
                    container[key].append(sub_value)
        return

    @classmethod
    def one_access_type(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue]
    ) -> None:
        if key not in container:
            container[key] = copy.deepcopy(value)
        else:
            print('error')
        return None

    @classmethod
    def store_value(
        cls,
        key: DictKey, 
        value: DictValue,
        container: dict[DictKey, DictValue],
        store_type: Store_Type = 'one_access'
    ) -> None:

        if store_type == 'one_access':
            cls.one_access_type(key, value, container)
        elif store_type == 'append':
            cls.append_type(key, value, container)
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
            warning
            '''
            pass
        return container[key]
    
    @classmethod
    def get_all_key_value_pairs(
        cls,
        container: dict[DictKey, DictValue]
    ) -> dict[DictKey, DictValue]:
        return copy.deepcopy(container)