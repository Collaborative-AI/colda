from Items import pyMongo

class test_message:
    
    @classmethod
    def search_test_message_document(cls, test_id):
        return pyMongo.db.Test_Message.find_one({'test_id': test_id})
        
    @classmethod
    def create_test_message_document(cls, test_id, cur_rounds_num):
        test_message_document = {
            'test_id': test_id,
            'cur_rounds_num': cur_rounds_num,
        }
        return pyMongo.db.Test_Message.insert_one(test_message_document)

    @classmethod
    def update_test_message_document(cls, test_id, cur_rounds_num, assistor_id, output_id):
        if cls.search_test_message_document(test_id=test_id) == None:
            cls.create_test_message_document(test_id=test_id, cur_rounds_num=cur_rounds_num)

        return pyMongo.db.Test_Message.update_one({'test_id': test_id}, {'$set':{
                   'rounds_' + str(cur_rounds_num) + '.output_dict.' + assistor_id + '.output_id': output_id
               }})