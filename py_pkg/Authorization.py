import requests
import json
import base64
# import jwt
from Network import Network
from PersonalInformation import PersonalInformation
from apollo_utils import handle_base64_padding
# from Get_Notification import

# from urllib.request import quote, unquote
# import atob

class Authorization():
    __Authorization_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.base_url = self.Network_instance.get_base_url()

    @classmethod
    def get_Authorization_instance(cls):
        if cls.__Authorization_instance == None:
            cls.__Authorization_instance = Authorization()

        return cls.__Authorization_instance

    def userRegister(self, username: str, password: str):
        pass


    def userLogin(self, username: str, password: str):

        """
        Get Token through HTTP Authorization's Basic Auth when first time login. Update __token in Network class

        Parameters:
         username - String. The username of current user
         password - String. The password of current user

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        url = self.base_url + "/tokens"
        print('url', url, username, password)
        token_response = requests.post(url, auth=(username, password))
        print('token_response', token_response)
        token_response_text = json.loads(token_response.text)

        token = token_response_text["token"]        
        # split token (token has 3 parts)
        temp = token.split('.')
        # add padding to base64 string
        temp[1] = handle_base64_padding(temp[1])
        # get user_id
        user_id = str(json.loads(base64.b64decode(temp[1]))['user_id'])
        print('login user_id', user_id)

        # set token
        self.Network_instance.set_token(token)
        # set user_id
        self.PersonalInformation_instance.set_user_id(user_id)

        # # 编码
        # c = base64.b64encode(name.encode())
        # print(c, type(c), type(split[1]))
        # # c = split[1].decode('utf8')
        # # print(c)
        # res = base64.b64decode(unquote(split[1]))
        # print(res)
        # print(token, json.loads(split[1]))
        # url = self.base_url + "/create_new_train_task/"
        # token = self.Network_instance.get_token()
        # print(token)
        # a = 'Bearer ' + token
        # get_train_id_response = requests.get(url, headers = {'Authorization': a})
        # print(get_train_id_response, get_train_id_response.text)
        # get_train_id_response_text = json.loads(get_train_id_response.text)
        #
        # new_task_id = get_train_id_response_text["task_id"]
        #
        # return new_task_id

        return None


    def userLogout(self):
        a = Network.get_Network_instance()
        print(a)
        b = Network.get_Network_instance()
        print(b)
        pass

