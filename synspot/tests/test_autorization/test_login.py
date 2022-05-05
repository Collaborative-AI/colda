import pytest

from synspot.tests.test_autorization.conftest import Authorization_instance

from synspot.tests.test_autorization.conftest import Network_instance

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

    @pytest.mark.usefixtures('Authorization_instance')
    @pytest.mark.parametrize("username, password, expected_res", [
        ('xie1', 'Xie1@123', True),
        ('xie2', 'Xie2@123', True)
    ])
    def test_login(self, Authorization_instance, username, password, expected_res):

        response = Authorization_instance.userLogin(
            username=username, 
            password=password, 
        )
        assert response == expected_res

    
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