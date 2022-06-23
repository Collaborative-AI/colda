import pytest
from colda.tests.test_database.conftest import DatabaseOperator_instance


class TestTrainSponsorMetadataDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        (('user', 'test', 'test', 'test'), 
        "DefaultMetadataDatabase stores user successfully!"),
        (('user', 'test', 'test2', 'test2'), 
        "DefaultMetadataDatabase stores user successfully!")
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='default_metadata')
        response = DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            default_mode=test_record[1], 
            default_task_mode=test_record[2], 
            default_model_name=test_record[3], 
        )
        assert response == expected_res

    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        ('user', ('test', 'test2', 'test2', None, None, None)),
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='default_metadata')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record, 
        )
        assert response == expected_res