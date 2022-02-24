import requests
import json
import base64

# import jwt
from synspot.network import Network
from synspot.personalinformation import PersonalInformation
from synspot.database import Database
from synspot.utils import handle_base64_padding, load_json_data, check_status_code
# from Get_Notification import

# from urllib.request import quote, unquote
# import atob

class Authorization():
    __Authorization_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.Database_instance = Database.get_Database_instance()
        self.base_url = self.Network_instance.base_url

    def __obtain_important_information(self):
        root = self.PersonalInformation_instance.root
        assert root is not None

        return root

    @classmethod
    def get_Authorization_instance(cls):
        if cls.__Authorization_instance == None:
            cls.__Authorization_instance = Authorization()

        return cls.__Authorization_instance

    def userRegister(self, username: str, email:str, password: str):

        url = self.base_url + "/users/"
        data = {
            'username': username,
            'email': email,
            'password': password
        }

        res = None
        try:
            user_register_res = requests.post(url, json=data)
            if check_status_code(user_register_res, 201):
                res = 'Please confirm your email'
            else:
                user_register_res = load_json_data(json_data=user_register_res, json_data_name='user_register_res')
                res = user_register_res['message'] 
                print('Register Instruction', user_register_res)
                return False
        except:
            print('user_register_res wrong')

        return True


    def userLogin(self, username: str, password: str):

        """
        Get Token through HTTP Authorization's Basic Auth when first time login. Update __token in Network class

        :param username: The username of current user
        :param password: The password of current user

        :returns: Boolean

        :exception OSError: Placeholder.
        """

        url = self.base_url + "/tokens"
        print('url', url, username, password)
        try:
            token_response = requests.post(url, auth=(username, password))
        except:
            print('create_new_train_task wrong')
            return False
       
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

        self.Network_instance.token = token
        self.PersonalInformation_instance.user_id = user_id
        
        return True

    def userLogout(self):
        """
        Handle user logout by deleting the information in the instances of Network, 
        PersonalInformation, and Database_class.

        :returns: None

        :exception OSError: Placeholder.
        """
        self.Network_instance.logout()
        self.PersonalInformation_instance.logout()
        self.Database_instance.logout()
        return 

