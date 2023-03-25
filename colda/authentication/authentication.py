from __future__ import annotations

import requests
import json
import base64

from network.api import Network
from pi.api import PI

from utils.log.algorithm_log import AlgorithmLog
from utils.log.workflow_log import WorkflowLog

from database.database_factory import (
    TrainSponsorMetadataDatabase,
    TrainAssistorMetadataDatabase,
    TrainAlgorithmDatabase,
    TestSponsorMetadataDatabase,
    TestAssistorMetadataDatabase,
    TestAlgorithmDatabase,
    DefaultMetadataDatabase
)

from authentication.utils import del_instance

from authentication.utils import handle_base64_padding

from authentication.base import AuthenticationBase

from network.api import DP

from typeguard import typechecked


#@typechecked
class Authentication(AuthenticationBase):
    '''
    Verify user identity

    Methods
    -------
    user_register
    user_login
    user_logout
    '''

    __authentication_instance = None

    def __init__(self):
        self.Network_instance = Network.get_instance()
        self.PI_instance = PI.get_instance()

        self.base_url = self.Network_instance.base_url

    @classmethod
    def get_instance(cls) -> Authentication:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        Authentication
        '''
        if cls.__authentication_instance == None:
            cls.__authentication_instance = Authentication()

        return cls.__authentication_instance

    def process_token(
        self, token: str
    ) -> None:
        '''
        Process token from backend and Set correlated attributes

        Parameters
        ----------
        token : str

        Returns
        -------
        None
        '''
        # split token (token has 3 parts)
        temp = token.split('.')
        # add padding to base64 string
        temp[1] = handle_base64_padding(temp[1])
        # get user_id
        user_id = str(json.loads(base64.b64decode(temp[1]))['user_id'])

        self.Network_instance.token = token
        self.PI_instance.user_id = user_id
        return

    def user_register(
        self, 
        username: str, 
        email:str, 
        password: str
    ) -> None:
        '''
        register new user

        Parameters
        ----------
        username : str
        email : str
        password : str

        Returns
        -------
        None
        '''
        data = {
            'username': username,
            'email': email,
            'password': password
        }
        res = self.Network_instance.post_request_chaining(
            data=data,
            url_prefix='user',
            url_root='users',
            url_suffix=None,
            status_code=201
        )
        print('register successfully')
        return

    def user_login(
        self, 
        username: str,
        password: str
    ) -> None:
        '''
        user login
        Get Token when first time login. Update __token in Network class

        Parameters
        ----------
        username : str
        password : str

        Returns
        -------
        None
        '''
        url = self.Network_instance.process_url(
            url_prefix='auth', 
            url_root='tokens',
            url_suffix=None,
        )

        try:
            network_response = requests.post(url, auth=(username, password))
        except Exception:
            raise Exception

        DP.check_network_response(
            network_response=network_response, 
        )

        network_response = DP.load_network_response(
            network_response=network_response
        )

        token = network_response["token"] 
        self.process_token(token)
        assert token is not None
        print(f'login successfully, current username is: {username}')
        return

    def user_logout(self):
        '''
        user logout
        clean related class

        Returns
        -------
        None
        '''
        Network.delete()
        PI.delete()
        AlgorithmLog.delete() 
        WorkflowLog.delete()
        TrainSponsorMetadataDatabase.delete()   
        TrainAssistorMetadataDatabase.delete()
        TrainAlgorithmDatabase.delete()
        TestSponsorMetadataDatabase.delete()
        TestAssistorMetadataDatabase.delete()  
        TestAlgorithmDatabase.delete()
        DefaultMetadataDatabase.delete()

        print('logout done')
        return 

