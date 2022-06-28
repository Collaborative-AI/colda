
import pytest

from colda.tests.test_network.conftest import network_instance

from colda.error import StatusCodeError


class TestNetwork:

    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url, expected_url", [
        (('prefix', 'root', 'suffix'), '/prefix/root/suffix'),
        (('prefix', 'root', None), '/prefix/root')
    ])
    def test_process_url(self, network_instance, url, expected_url):
        processed_url = network_instance.process_url(
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2]
        )

        assert processed_url == f'{network_instance.base_url}{expected_url}'
    

    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url, expected_status_code", [
        (('helper_api', 'testing_get', None), 200)
    ])
    def test_get_request(self, network_instance, url, expected_status_code):
        processed_url = network_instance.process_url(
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2]
        ) 

        network_response = network_instance.get_request(
            url=processed_url,
            token='',
            request_name=url[1],
        )
        assert network_response.status_code == expected_status_code
    

    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url, expected_status_code", [
        (('helper_api', 'testing_post', None), 200),
    ])
    def test_post_request(self, network_instance, url, expected_status_code):
        processed_url = network_instance.process_url(
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2]
        ) 

        network_response = network_instance.post_request(
            url=processed_url,
            token='',
            request_name=url[1],
            data=None
        )
        assert network_response.status_code == expected_status_code


    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url, status_code, expected_result", [
        (('helper_api', 'testing_get', None), 200, 'test successfully!'),
        (('helper_api', 'testing_get', None), 201, StatusCodeError),
    ])
    def test_get_request_chaining(self, network_instance, url, status_code, expected_result):
        network_response = network_instance.get_request_chaining(
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2],
            status_code=status_code
        )
        assert network_response == expected_result
    
    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize("url, status_code, expected_result", [
        (('helper_api', 'testing_post', None), 200, 'test successfully!'),
        (('helper_api', 'testing_post', None), 201, StatusCodeError)
    ])
    def test_post_request_chaining(self, network_instance, url, status_code, expected_result):
        network_response = network_instance.post_request_chaining(
            data=None,
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2],
            status_code=status_code
        )
        assert network_response == expected_result