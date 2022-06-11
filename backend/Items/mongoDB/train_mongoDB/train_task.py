from Items import pyMongo

class train_task():

    @classmethod
    def search_train_task_document(cls, train_id):
        return pyMongo.db.Train_Task.find_one({'train_id': train_id})

    @classmethod
    def create_train_task_document(
        cls, 
        train_id, 
        task_name, 
        task_description, 
        task_mode, 
        model_name, 
        metric_name, 
        sponsor_id, 
        assistor_id_dict, 
        test_indicator,
        test_id_of_train_id_dict
    ):

        train_task_document = {
            "train_id": train_id,
            'test_indicator': test_indicator,
            "task_name": task_name,
            "task_description": task_description,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "sponsor_id": sponsor_id,
            "assistor_id_dict": assistor_id_dict,
            "test_id_of_train_id_dict": test_id_of_train_id_dict,
        }
        print('train_task_documentss', train_task_document)
        return pyMongo.db.Train_Task.insert_one(train_task_document)
        
    @classmethod
    def update_train_task_document_test_id_of_train_id_dict(cls, train_id, test_id):
        print('update_train_task_document_test_id_of_train_id_dict', test_id)
        return pyMongo.db.Train_Task.update_one({'train_id': train_id}, {'$set':{
                   'test_id_of_train_id_dict.' + test_id: None,
               }})