import sys
import bson
from gridfs import GridFS
from io import BytesIO

from Items import pyMongo

class mongoDB():

    @classmethod
    def encode_file_to_BSON_file(cls, file):
        if isinstance(file, bson.BSON):
            return file
        return bson.BSON.encode({'file': file})
    
    @classmethod
    def decode_BSON_file_to_file(cls, BSON_file):
        if not isinstance(BSON_file, bson.BSON):
            return BSON_file
        return bson.BSON(BSON_file).decode()

    @classmethod
    def if_file_size_exceed_limit(cls, file):
        BSON_file = cls.encode_file_to_BSON_file(file)
        # check size of file.
        # if size surpasses the limit, return False and BSON_file
        if sys.getsizeof(BSON_file) > 16000000:
            return True, BSON_file
        return False, None
    
    @classmethod
    def store_large_file(cls, BSON_file, filename='None'):
        if not isinstance(BSON_file, bson.BSON):
            BSON_file = cls.encode_file_to_BSON_file(BSON_file)

        print('hhhh', type(BSON_file))
        fileobj = BytesIO(BSON_file)
        file_id = pyMongo.save_file(filename=filename, fileobj=fileobj, base='fs')
        return file_id

    @classmethod
    def retrieve_large_file(cls, base='fs', file_id=None, filename=None):
        gridfs = GridFS(pyMongo.db, base)
        if filename:
            gridfile = gridfs.find_one({"filename": filename})
        elif file_id:
            gridfile = gridfs.find_one({"_id": file_id})
        else:
            return False
        
        return bson.BSON(gridfile.read()).decode()['file']

    @classmethod
    def delete_large_file(cls, file_id, base='fs'):
        gridfs = GridFS(pyMongo.db, base)
        gridfile = gridfs.delete({"_id": file_id})
        return gridfile

    @classmethod
    def update_notification_document(
        cls, 
        user_id, 
        notification_name, 
        train_id, 
        sender_random_id, 
        role, 
        cur_rounds_num, 
        test_indicator, 
        test_id=None
    ):

        if not isinstance(user_id, str):
            return False
        elif not isinstance(notification_name, str):
            return False
        elif not isinstance(train_id, str):
            return False
        elif not isinstance(sender_random_id, str):
            return False
        elif not isinstance(role, str):
            return False
        elif not isinstance(cur_rounds_num, int):
            return False
        elif not isinstance(test_indicator, str):
            return False

        if pyMongo.db.Notification.find_one({'user_id': user_id}) == None:
            pyMongo.db.Notification.insert_one({'user_id': user_id})

        if test_indicator == 'train':
            base_key = f'category.{notification_name}.train_id_dicts.{train_id}'
            print('base_key$$$', base_key)
            return pyMongo.db.Notification.update_one({'user_id': user_id}, {'$set':{
                f'{base_key}.sender_random_id': sender_random_id,
                f'{base_key}.role': role,
                f'{base_key}.cur_rounds_num': cur_rounds_num,
            }})
        elif test_indicator == 'test':
            base_key = f'category.{notification_name}.test_id_dicts.{test_id}'
            return pyMongo.db.Notification.update_one({'user_id': user_id}, {'$set':{
                f'{base_key}.sender_random_id': sender_random_id,
                f'{base_key}.role': role,
                f'{base_key}.cur_rounds_num': cur_rounds_num,
                f'{base_key}.train_id': train_id,
            }})
        
        
    @classmethod
    def search_user_document(
        cls, 
        user_id, 
        username, 
        email, 
        key_indicator
    ):
        if key_indicator == 'user_id':
            return pyMongo.db.User.find_one({'user_id': user_id})
        elif key_indicator == 'username':
            return pyMongo.db.User.find_one({'username': username})
        elif key_indicator == 'email':
            return pyMongo.db.User.find_one({'email': email})

    @classmethod
    def create_user_document(cls, user_document):
        return pyMongo.db.User.insert_one(user_document)
    
    @classmethod
    def update_user_document(cls, user_id):
        pass

    @classmethod
    def search_pending_document(cls, user_id):
        return pyMongo.db.Pending.find_one({'user_id': user_id})
    
    @classmethod
    def create_pending_document(cls, user_id):
        pending_document = {
            'user_id': user_id,
            'task_dict': {}
        }
        return pyMongo.db.Pending.insert_one(pending_document)

    @classmethod
    def update_pending_document(cls, user_id, task_id, test_indicator):
        if cls.search_pending_document(user_id) == None:
            cls.create_pending_document(user_id)
        print('id, test_indicator', id, test_indicator)
        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$set':{
            f'task_dict.{task_id}.test_indicator': test_indicator
        }})
    
    @classmethod
    def delete_pending_document_field(cls, user_id, task_id):
        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$unset':{
            f'task_dict.{task_id}': ""
        }})
    
    @classmethod
    def create_stop_document(cls, task_id, cur_rounds_num, assistor_situation_don):
        pass

    
from Items.mongoDB.test_mongoDB import *
from Items.mongoDB.train_mongoDB import *




    # class Strategy(ABC):
#     """
#     The Strategy interface declares operations common to all supported versions
#     of some algorithm.

#     The Context uses this interface to call the algorithm defined by Concrete
#     Strategies.
#     """

#     @classmethod
#     @abstractmethod
#     def add_notification_document(cls):
#         pass
      
#     @classmethod
#     @abstractmethod
#     def create_pending_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def create_stop_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_situation_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_output_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_match_document(cls):
#         pass

#     @classmethod
#     @abstractmethod
#     def add_match_file_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_task_document(cls):
#         pass




# class mongoDB_strategy_interface():
#     """
#     The Context defines the interface of interest to clients.
#     """

#     def __init__(self) -> None:
#         self._mongoDB_strategy = None

#     @property
#     def mongoDB_strategy(self) -> Strategy:
#         """
#         The Context maintains a reference to one of the Strategy objects. The
#         Context does not know the concrete class of a strategy. It should work
#         with all strategies via the Strategy interface.
#         """

#         return self._mongoDB_strategy

#     @mongoDB_strategy.setter
#     def mongoDB_strategy(self, mongoDB_strategy: Strategy) -> None:
#         """
#         Usually, the Context allows replacing a Strategy object at runtime.
#         """

#         self._mongoDB_strategy = mongoDB_strategy

#     def add_user(self):
#         return

#     def add_notification_document(self, user_id, notification_name, task_id, test_id, 
#                                   sender_random_id, role, cur_rounds_num):
#         if not isinstance(user_id, str):
#             return False
#         elif not isinstance(notification_name, str):
#             return False
#         elif task_id and not isinstance(task_id, str):
#             return False
#         elif test_id and not isinstance(test_id, str):
#             return False
#         elif not isinstance(sender_random_id, str):
#             return False
#         elif not isinstance(role, str):
#             return False
#         elif not isinstance(cur_rounds_num, int):
#             return False
#         # cant send to task_id and test_id together
#         elif task_id and test_id:
#             return False
        
#         return self._mongoDB_strategy.add_notification_document(user_id, notification_name, task_id, test_id, 
#                                                                 sender_random_id, role, cur_rounds_num)
    
#     def create_pending_document(self):
#         pass
    
#     def create_stop_document(self):
#         pass
    
#     def add_message_document(self):
#         pass

#     def add_message_situation_document(self):
#         pass
    
#     def add_message_output_document(self):
#         pass
    
#     def add_match_file_document(self, user_id, notification_name, task_id, test_id, 
#                                 sender_random_id, role, cur_rounds_num):

#         return self._mongoDB_strategy.add_match_file_document(user_id, notification_name, task_id, test_id, 
#                                                               sender_random_id, role, cur_rounds_num)
        
  
#     def add_task_document(self, user_id, notification_name, task_id, test_id, 
#                                 sender_random_id, role, cur_rounds_num):
                              
#         return self._mongoDB_strategy.add_match_file_document(user_id, notification_name, task_id, test_id, 
#                                                               sender_random_id, role, cur_rounds_num)
    
    


