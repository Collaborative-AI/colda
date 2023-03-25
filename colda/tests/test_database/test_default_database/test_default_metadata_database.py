import pytest
from .conftest import DatabaseOperator_instance

class TestDefaultMetadataDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (('user', 'auto', 'classification', 'linear'), None),
        (('user', 'manual', 'regression', 'gradient_boosting'), None)
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected):
        print('store', id(DatabaseOperator_instance))
        DatabaseOperator_instance.set_database(database_type='default_metadata')
        assert expected == DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            default_mode=test_record[1], 
            default_task_mode=test_record[2], 
            default_model_name=test_record[3], 
        )
    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (('user'), ('manual', 'regression', 'gradient_boosting', None, None, None)),
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected):
        print('get', id(DatabaseOperator_instance))
        DatabaseOperator_instance.set_database(database_type='default_metadata')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record, 
        )
        assert response == expected