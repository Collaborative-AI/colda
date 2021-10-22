# from Network import Network
from Authorization import Authorization
from PersonalInformation import PersonalInformation
from TrainRequest import TrainRequest
from TestRequest import TestRequest
import threading
# import jwt

class global_class:
    _instance_lock = threading.Lock()

    def __new__(cls):
        if not hasattr(global_class, "_instance"):
            with global_class._instance_lock:
                if not hasattr(global_class, "_instance"):
                    global_class._instance = super(global_class, cls).__new__(cls)
        return global_class._instance

    def __init__(self):
        # self.__Network_instance = None
        # self.__PersonalInformation_instance = None
        self.__TrainRequest_instance = None
        self.__TestRequest_instance = None
        self.__Authorization_instance = None






    def get_TestRequest_instance(self):
        if self.__TestRequest_instance == None:
            self.__TestRequest_instance = TestRequest()

        return self.__TestRequest_instance


