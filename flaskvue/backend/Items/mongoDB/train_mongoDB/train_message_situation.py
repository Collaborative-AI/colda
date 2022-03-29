from Items import pyMongo

class train_message_situation():

    @classmethod
    def search_train_message_situation_document(cls, situation_id):
        return pyMongo.db.Train_Message_Situation.find_one({'situation_id': situation_id})

    @classmethod
    def create_train_message_situation_document(cls, situation_id, sender_id, sender_random_id, recipient_id, situation_content):
        train_message_situation_document = {
            'situation_id': situation_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'situation_content': situation_content
        }
        return pyMongo.db.Train_Message_Situation.insert_one(train_message_situation_document)
