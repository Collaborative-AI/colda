from Items import pyMongo

class test_task:

    @classmethod
    def search_test_task_document(cls, test_id):
        return pyMongo.db.Test_Task.find_one({'test_id': test_id})

    @classmethod
    def create_test_task_document(
        cls, 
        test_id, 
        train_id, 
        test_name, 
        test_description, 
        task_mode, 
        model_name, 
        metric_name, 
        sponsor_id, 
        assistor_id_dict, 
        test_indicator
    ):

        test_task_document = {
            'test_id': test_id,
            'test_indicator': test_indicator,
            "train_id": train_id,
            "test_name": test_name,
            "test_description": test_description,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "sponsor_id": sponsor_id,
            "assistor_id_dict": assistor_id_dict,
        }
        return pyMongo.db.Test_Task.insert_one(test_task_document)

