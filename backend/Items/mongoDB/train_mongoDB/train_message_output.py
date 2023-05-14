from Items import pyMongo
from Items.mongoDB import mongoDB

class train_message_output(mongoDB):

    @classmethod
    def search_train_message_output_document(cls, output_id):
        return pyMongo.db.Train_Message_Output.find_one({'output_id': output_id})

    @classmethod
    def create_train_message_output_document(
        cls, 
        output_id, 
        train_id, 
        sender_id, 
        sender_random_id, 
        recipient_id, 
        output_content
    ):

        indicator, BSON_file = cls.if_file_size_exceed_limit(file=output_content)
        if not indicator:
            train_message_output_document = {
                'output_id': output_id,
                'train_id': train_id, 
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'output_content': output_content,
                'is_large_file': False
            }
        elif indicator:
            file_id = cls.store_large_file(BSON_file=BSON_file)
            train_message_output_document = {
                'output_id': output_id,
                'train_id': train_id, 
                'sender_id': sender_id,
                'sender_random_id': sender_random_id,
                'recipient_id': recipient_id,
                'output_content': file_id,
                'is_large_file': True,
            }
        return pyMongo.db.Train_Message_Output.insert_one(train_message_output_document)

    @classmethod
    def delete_train_message_output_document(cls, train_id, base='fs'):
        train_message_output_document = {
            'train_id': train_id,
        }
        documents = pyMongo.db.Train_Message_Output.find(train_message_output_document)

        for document in documents:
            if document['is_large_file'] == False:
                pyMongo.db.Train_Message_Output.delete_one({'_id': document['_id']})
            elif document['is_large_file'] == True:
                gridfs_file_id = document['output_content']
                cls.delete_large_file(file_id=gridfs_file_id, base=base)

        return True