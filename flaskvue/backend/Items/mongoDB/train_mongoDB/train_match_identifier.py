from Items import pyMongo

class train_match_identifier():

    @classmethod
    def search_train_match_identifier_document(cls, identifier_id):
        return pyMongo.db.Train_Match_Identifier.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_train_match_identifier_document(cls, identifier_id, identifier_content):
        train_match_identifier_document = {
            'identifier_id': identifier_id,
            'identifier_content': identifier_content,
        }
        return pyMongo.db.Train_Match_Identifier.insert_one(train_match_identifier_document)