from Items import pyMongo

class train_message_output():

    @classmethod
    def search_train_message_output_document(cls, output_id):
        return pyMongo.db.Train_Message_Output.find_one({'output_id': output_id})

    @classmethod
    def create_train_message_output_document(cls, output_id, sender_id, sender_random_id, recipient_id, output_content):
        train_message_output_document = {
            'output_id': output_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'output_content': output_content
        }
        return pyMongo.db.Train_Message_Output.insert_one(train_message_output_document)

