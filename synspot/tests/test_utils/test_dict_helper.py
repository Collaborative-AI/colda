
import copy
import pytest

from synspot.utils import DictHelper


class TestDictHelper:

    @pytest.mark.parametrize("key, container, expected", [
        (['key1', 'key2', 'key3'], {}, {'key1': {'key2': {}}}),
        (['key1'], {}, {})
    ])
    def test_process_key(self, key, container, expected):
        key_res, container_res = DictHelper.process_key(
            key=key,
            container=container
        )
        print('**', key, container)
        assert container == expected 


    @pytest.mark.parametrize("key, value, container, expected", [
        (['key1', 'key2', 'key3'], 'test', {}, {'key1': {'key2': {'key3': 'test'}}}),
        (['key6'], 5, {}, {'key6': 5})
    ])
    def test_store_value(self, key, value, container, expected):
        res = DictHelper.store_value(
            key=key,
            value=value,
            container=container
        )
        assert container == expected 


    @pytest.mark.parametrize("key, value, container, expected", [
        (['key1', 'key2', 'key3'], 'test', {}, 'test'),
        # (['key6'], 5, {}, 5)
    ])
    def test_get_value(self, key, value, container, expected):
        temp = copy.deepcopy(key)
        res = DictHelper.store_value(
            key=key,
            value=value,
            container=container
        )
        print('kllklk', temp, container)
        value_res = DictHelper.get_value(
            key=temp,
            container=container
        )
        print('kllklk2', value_res)
        assert value_res == expected 