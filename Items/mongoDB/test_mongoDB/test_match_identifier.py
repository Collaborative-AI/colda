from Items import pyMongo
from Items.mongoDB import mongoDB

class test_match_identifier(mongoDB):

    @classmethod
    def search_test_match_identifier_document(cls, identifier_id):
        return pyMongo.db.Test_Match_Identifier.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_test_match_identifier_document(cls, identifier_id, identifier_content):
        indicator, BSON_file = cls.if_file_size_exceed_limit(file=identifier_content)
        if not indicator:
            test_match_identifier_document = {
                'identifier_id': identifier_id,
                'identifier_content': identifier_content,
                'is_large_file': False
            }
        elif indicator:
            file_id = cls.store_large_file(BSON_file=BSON_file)
            test_match_identifier_document = {
                'identifier_id': identifier_id,
                'identifier_content': file_id,
                'is_large_file': True
            }
        return pyMongo.db.Test_Match_Identifier.insert_one(test_match_identifier_document)
