from __future__ import annotations

import requests

from colda.utils.api import (
    del_instance,
    Constant,
    Serialization
)

from colda.network.dp import DP

from colda.network.base import BaseNetwork

from typing import Union

from colda._typing import JSONType

from typeguard import typechecked


#@typechecked
class Network(BaseNetwork):
    '''
    Handle network http requests

    Attributes
    ----------
    base_url
    token

    Methods
    -------
    get_instance
    process_url
    get_request
    post_request
    get_request_chaining
    post_request_chaining
    logout
    '''

    __Network_instance = None

    def __init__(self):
        self.__token = ''
        self.__baseURL = 'http://127.0.0.1:5000'
        # self.__baseURL = 'http://colda-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com/'

    @classmethod
    def get_instance(cls) -> Network:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        Network
        '''
        if cls.__Network_instance == None:
            cls.__Network_instance = Network()

        return cls.__Network_instance

    @property
    def base_url(self) -> str:
        '''
        Get the ipv4 address of AWS server

        Parameters
        ----------
        None

        Returns
        -------
        str
            the ipv4 address of AWS server
        '''
        return self.__baseURL

    @property
    def token(self) -> str:
        '''
        Get the token

        Parameters
        ----------
        None

        Returns
        -------
        str
            token
        '''
        return self.__token

    @token.setter
    def token(self, token: str) -> None:
        '''
        Set token to new token

        Parameters
        ----------
        token : str

        Returns
        -------
        None
        '''
        self.__token = token
        return 

    def __add_prefix_to_url(
        self, url_prefix: str, url_root: str
    ) -> str:
        '''
        Add prefix to url_root. 

        Parameters
        ----------
        url_prefix : str
        url_root : str

        Returns
        -------
        str
        '''
        return f'/{url_prefix}/{url_root}'

    def __add_suffix_to_url(
        self, url_root: str, url_suffix: str
    ) -> str:
        '''
        Add suffix to url_root

        Parameters
        ----------
        url_root : str
        url_suffix : str
        
        Returns
        -------
        str
        '''
        return f'{url_root}/{url_suffix}'

    def process_url(
        self, 
        url_prefix: str, 
        url_root: str, 
        url_suffix: str = None
    ) -> str:
        '''
        Add prefix and suffix to url_root

        Parameters
        ----------
        url_prefix : str
        url_root : str
        url_suffix : str
        
        Returns
        -------
        str
        '''
        if url_suffix == None:
            return self.base_url + self.__add_prefix_to_url(url_prefix, url_root)
        return self.base_url + self.__add_suffix_to_url(
            self.__add_prefix_to_url(url_prefix, url_root), 
            url_suffix
        )

    def get_request(
        self, 
        url: str, 
        token: str, 
        request_name: str
    ) -> JSONType:
        '''
        Initiate a http get network request.
        Get the data returned by the http get network request.

        Parameters
        ----------
        url : str
        token : str
        request_name : str
            request_name is used for debugging
        
        Returns
        -------
        JSONType
        '''
        try:
            request_response = requests.get(
                url, 
                headers = {'Authorization': 'Bearer ' + token}
            )
        except Exception as e:
            print(f'{request_name} request wrong! {e}')
            raise e
        else:
            return request_response

    def post_request(
        self, 
        url: str, 
        token: str, 
        request_name: str, 
        data: dict[str, Union[list[str], str]]
    ) -> JSONType:
        '''
        Initiate a http post network request.
        Get the data returned by the http post network request.

        Parameters
        ----------
        url : str
        token : str
        request_name : str
            request_name is used for debugging
        data : dict[str, Union[list[str], str]]
            data that needs to be sent to the backend
        
        Returns
        -------
        JSONType
        '''
        try:
            request_response = requests.post(
                url, 
                json=data, 
                headers={'Authorization': 'Bearer ' + token}
            )
        except Exception as e:
            print(f'{request_name} request wrong! {e}')
            raise Exception
        else:
            return request_response

    def get_request_chaining(
        self, 
        url_prefix: str,
        url_root: str,
        url_suffix: str,
        status_code: int = 200, 
    ) -> dict[str, Union(list[str], str)]:
        '''
        Handle the http get request flow:
            1. generate url
            2. http get request
            3. parse http get response

        Parameters
        ----------
        data : JSONType
        url_prefix : str
        url_root : str
        url_suffix : str
        status_code : int
        
        Returns
        -------
        dict
        '''
        url = self.process_url(
            url_prefix=url_prefix, 
            url_root=url_root, 
            url_suffix=url_suffix
        )

        network_response = self.get_request(
            url=url,
            token=self.__token,
            request_name=url_root
        )
        
        DP.check_network_response(
            network_response=network_response, 
            status_code=status_code
        )

        return DP.load_network_response(
            network_response=network_response
        )

    def post_request_chaining(
        self,  
        data: dict[str, Union[list[str], str]],
        url_prefix: str,
        url_root: str,
        url_suffix: str,
        status_code: int = 200,
    ) -> dict[str, Union[list[str], str]]:
        '''
        Handle the http post request flow:
            1. generate url
            2. http post request
            3. parse http post response

        Parameters
        ----------
        data : JSONType
        url_prefix : str
        url_root : str
        url_suffix : str
        status_code : int

        Returns
        -------
        dict
        '''
        url = self.process_url(
            url_prefix=url_prefix, 
            url_root=url_root, 
            url_suffix=url_suffix
        )
        
        data = Serialization.make_data_serializable(data=data)

        network_response = self.post_request(
            url=url,
            token=self.__token,
            request_name=url_root,
            data=data
        )

        DP.check_network_response(
            network_response=network_response, 
            status_code=status_code
        )

        return DP.load_network_response(
            network_response=network_response
        )
    
    @classmethod
    def logout(cls) -> None:
        '''
        Clean Network data when logout

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        '''
        del_instance(
            objectInstance=cls.__Network_instance
        )

        return