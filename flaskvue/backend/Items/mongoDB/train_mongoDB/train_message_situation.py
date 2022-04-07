from Items import pyMongo
from Items.mongoDB import mongoDB

class train_message_situation(mongoDB):

    @classmethod
    def search_train_message_situation_document(cls, situation_id):
        return pyMongo.db.Train_Message_Situation.find_one({'situation_id': situation_id})

    def retrieve_train_message_situation_content():
        pass

    @classmethod
    def create_train_message_situation_document(cls, situation_id, task_id, sender_id, sender_random_id, recipient_id, situation_content):
        indicator, BSON_file = cls.if_file_size_exceed_limit(file=situation_content)
        if not indicator:
            train_message_situation_document = {
                'situation_id': situation_id,
                'task_id': task_id,
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'situation_content': situation_content,
                'is_large_file': False
            }
        elif indicator:
            file_id = cls.store_large_file(BSON_file=BSON_file)
            train_message_situation_document = {
                'situation_id': situation_id,
                'task_id': task_id,
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'situation_content': file_id,
                'is_large_file': True
            }
        return pyMongo.db.Train_Message_Situation.insert_one(train_message_situation_document)

    @classmethod
    # delete train message
    def delete_train_message_situation_document(cls, task_id, base='fs'):
        train_message_output_document = {
            'task_id': task_id,
        }
        documents = pyMongo.db.Train_Message_Situation.find(train_message_output_document)

        for document in documents:
            if document['is_large_file'] == False:
                pyMongo.db.Train_Message_Situation.delete_one({'_id': document['_id']})
            elif document['is_large_file'] == True:
                gridfs_file_id = document['situation_content']
                cls.delete_large_file(file_id=gridfs_file_id, base=base)

        return True