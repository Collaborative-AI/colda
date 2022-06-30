import pytest
from colda.tests.test_database.conftest import DatabaseOperator_instance

from colda.error import DuplicateKeyError


class TestTestAssistorMetadataDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (
            ('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'), 
            None
        ),
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected):
        DatabaseOperator_instance.set_database(database_type='test_assistor_metadata')
        response = DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            train_id=test_record[1], 
            mode=test_record[2], 
            task_mode=test_record[3],
            model_name=test_record[4], 
            test_id = test_record[5],
            test_file_path=test_record[6], 
            test_id_column=test_record[7], 
            test_data_column=test_record[8],
        )
        assert response == expected

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record_1, test_record_2", [
        (
            ('test2', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'),
            ('test2', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test')
        )
    ])
    def test_store_record_exception(self, DatabaseOperator_instance, test_record_1, test_record_2):
        DatabaseOperator_instance.set_database(database_type='test_assistor_metadata')
        DatabaseOperator_instance.store_record(
            user_id=test_record_1[0], 
            train_id=test_record_1[1], 
            mode=test_record_1[2], 
            task_mode=test_record_1[3],
            model_name=test_record_1[4], 
            test_id = test_record_1[5],
            test_file_path=test_record_1[6], 
            test_id_column=test_record_1[7], 
            test_data_column=test_record_1[8],
        )
        msg = 'Store once type wrong, you cannot store twice under same key'
        with pytest.raises(DuplicateKeyError, match=msg):
            DatabaseOperator_instance.store_record(
                user_id=test_record_2[0], 
                train_id=test_record_2[1], 
                mode=test_record_2[2], 
                task_mode=test_record_2[3],
                model_name=test_record_2[4], 
                test_id = test_record_2[5],
                test_file_path=test_record_2[6], 
                test_id_column=test_record_2[7], 
                test_data_column=test_record_2[8],
            )

    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (('test', 'test'), ('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', None, None)),
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected):
        DatabaseOperator_instance.set_database(database_type='test_assistor_metadata')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record[0], 
            test_id=test_record[1], 
        )
        assert response == expected