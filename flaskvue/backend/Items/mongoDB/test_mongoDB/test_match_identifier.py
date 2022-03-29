from Items import pyMongo

class test_match_identifier:

    @classmethod
    def search_test_match_identifier_document(cls, identifier_id):
        return pyMongo.db.Test_Match_Identifier.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_test_match_identifier_document(cls, identifier_id, identifier_content):
        test_match_identifier_document = {
            'identifier_id': identifier_id,
            'identifier_content': identifier_content,
        }
        return pyMongo.db.Test_Match_Identifier.insert_one(test_match_identifier_document)
