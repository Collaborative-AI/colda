from Items import pyMongo
from Items.mongoDB import mongoDB

class test_message_output(mongoDB):

    @classmethod
    def search_test_message_output_document(cls, output_id):
        return pyMongo.db.Test_Message_Output.find_one({'output_id': output_id})

    @classmethod
    def create_test_message_output_document(cls, output_id, test_id, sender_id, sender_random_id, recipient_id, output_content):
        indicator, BSON_file = cls.if_file_size_exceed_limit(file=output_content)
        if not indicator:
            test_message_output_document = {
                'output_id': output_id,
                'test_id': test_id,
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'output_content': output_content,
                'is_large_file': False
            }
        elif indicator:
            file_id = cls.store_large_file(BSON_file=BSON_file)
            test_message_output_document = {
                'output_id': output_id,
                'test_id': test_id,
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'output_content': file_id,
                'is_large_file': True
            }
        return pyMongo.db.Test_Message_Output.insert_one(test_message_output_document)
    
    @classmethod
    def delete_test_message_output_document(cls, test_id, base='fs'):
        test_message_output_document = {
            'test_id': test_id,
        }
        documents = pyMongo.db.Test_Message_Output.find(test_message_output_document)

        for document in documents:
            if document['is_large_file'] == False:
                pyMongo.db.Test_Message_Output.delete_one({'_id': document['_id']})
            elif document['is_large_file'] == True:
                gridfs_file_id = document['output_content']
                cls.delete_large_file(file_id=gridfs_file_id, base=base)

        return True