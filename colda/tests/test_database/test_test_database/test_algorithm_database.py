import pytest
from colda.tests.test_database.conftest import DatabaseOperator_instance

class TestTestAlgorithmDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        (('test', 'test', 'test1', ''), None),
        (('test', 'test', 'test2', 'test'), None)
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='test_algorithm')
        response = DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            test_id=test_record[1], 
            algorithm_data_name=test_record[2],
            algorithm_data=test_record[3]
        )
        assert response == expected_res

    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        (('test', 'test', 'test1'), ''),
        (('test', 'test', 'test2'), 'test')
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='test_algorithm')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record[0], 
            test_id=test_record[1], 
            algorithm_data_name=test_record[2],
        )
        assert response == expected_res