
import pytest

from .conftest import network_instance

from error import StatusCodeError


class TestNetwork:

    '''
    Must run backend before testing
    '''
    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url_prefix, url_root, expected", [
        ('helper_api', 'testing_get', 'test successfully!'),
    ])
    def test_get_request(self, network_instance, url_prefix, url_root, expected):
        res = network_instance.get_request_chaining(
            url_prefix=url_prefix,
            url_root=url_root,
        )
        print('sss', res)
        assert res == expected
    
    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("data, url_prefix, url_root, expected", [
        ({}, 'helper_api', 'testing_post', 'test successfully!'),
    ])
    def test_post_request(self, network_instance, data, url_prefix, url_root, expected):
        res = network_instance.post_request_chaining(
            data=data,
            url_prefix=url_prefix,
            url_root=url_root,
        )

        assert res == expected
    

    