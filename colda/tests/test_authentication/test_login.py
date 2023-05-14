import pytest

from .conftest import Authentication_instance

from .conftest import Network_instance

from error import StatusCodeError


class TestLogin:

    @pytest.mark.usefixtures('Network_instance')
    @pytest.mark.parametrize("username, password, email, expected_res", [
        ('xie1', 'Xie1@123', 'xx', 'done'),
        ('xie2', 'Xie2@123', 'yy', 'done')
    ])
    def test_create_unittest_user(self, Network_instance, username, password, email, expected_res):
        
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        network_response = Network_instance.post_request_chaining(
            data=data,
            url_prefix='helper_api',
            url_root='create_unittest_user',
            url_suffix=None,
            status_code=200
        )
        assert network_response == expected_res

    @pytest.mark.usefixtures('Authentication_instance')
    @pytest.mark.parametrize("username, password, expected_res", [
        ('xie1', 'Xie1@123', None),
        ('xie2', 'Xie2@123', None)
    ])
    def test_login(self, Authentication_instance, username, password, expected_res):

        response = Authentication_instance.user_login(
            username=username, 
            password=password, 
        )
        assert response == expected_res

    @pytest.mark.usefixtures('Authentication_instance')
    @pytest.mark.parametrize("username, password, error_status_code, error_name, error", [
        (
            'xie1', 
            'Xie1@123333', 
            500,
            'ValueError',
            'user cannot found'
        ),
    ])
    def test_login_exception(self, Authentication_instance, username, password, error_status_code, error_name, error):
        msg = f"Wrong network response. status code: {error_status_code}, error_name: {error_name}, error: {error}"
        with pytest.raises(StatusCodeError, match=msg):
            Authentication_instance.user_login(
                username=username, 
                password=password, 
            )
    
    # @pytest.mark.usefixtures('DatabaseOperator_instance')
    # @pytest.mark.parametrize("test_record, expected_res", [
    #     (('test', 'test', 'test1'), ''),
    #     (('test', 'test', 'test2'), 'test')
    # ])
    # def test_get_record(self, DatabaseOperator_instance, test_record, expected_res):
    #     response = DatabaseOperator_instance.get_record(
    #         user_id=test_record[0], 
    #         train_id=test_record[1], 
    #         algorithm_data_name=test_record[2],
    #     )
    #     assert response == expected_res