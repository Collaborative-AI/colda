import copy
from parso import parse
import pytest

from colda.utils.api import DictHelper

from colda.error import DictValueNotFound


class TestDictHelper:

    @pytest.mark.parametrize("user_id, task_id, supplement_key, expected", [
        ('key1', None, None, ('key1', )),
        ('key1', 'key2', None, ('key1', 'key2')),
        ('key1', 'key2', 'key3', ('key1', 'key2', 'key3')),
        ('key1', 'key2', ['key3'], ('key1', 'key2', 'key3'))
    ])
    def test_generate_dict_root_key(self, user_id, task_id, supplement_key, expected):
        assert expected == DictHelper.generate_dict_root_key(
            user_id=user_id,
            task_id=task_id,
            supplement_key=supplement_key
        ) 

    @pytest.mark.parametrize("key, container, parse_mode, expected", [
        (['key1', 'key2'], {}, 'store', ('key2', {})),
        (['key1'], {}, 'store', ('key1', {})),
    ])
    def test_parse_key_store(self, key, container, parse_mode, expected):
        res = DictHelper._DictHelper__parse_key(
            key=key,
            container=container,
            parse_mode=parse_mode
        )
        assert res == expected 
    
    @pytest.mark.parametrize("key, container, parse_mode", [
        ([5], {}, 'get'),
        (['key1', 'key5'], {}, 'get'),
    ])
    def test_parse_key_get_exception(self, key, container, parse_mode):
        msg = 'Key not in container'
        with pytest.raises(DictValueNotFound, match=msg):
            DictHelper._DictHelper__parse_key(
                key=key,
                container=container,
                parse_mode=parse_mode
            )
        return

    @pytest.mark.parametrize("key, value, container, expected", [
        (['key1', 'key2', 'key3'], 'test', {}, {'key1': {'key2': {'key3': 'test'}}}),
        (['key6'], 5, {}, {'key6': 5}),
        (('key6', ), 5, {}, {('key6',): 5})
    ])
    def test_store_value(self, key, value, container, expected):
        DictHelper.store_value(
            key=key,
            value=value,
            container=container
        )
        assert container == expected 


    @pytest.mark.parametrize("key, value, container, expected", [
        (['key1', 'key2', 'key3'], 'test', {}, 'test'),
        (['key6'], 5, {}, 5),
    ])
    def test_get_value(self, key, value, container, expected):
        temp = copy.deepcopy(key)
        DictHelper.store_value(
            key=key,
            value=value,
            container=container
        )
        
        value_res = DictHelper.get_value(
            key=temp,
            container=container
        )
        assert value_res == expected 