from __future__ import annotations

import json
import requests

from synspot.utils import ParseJson

from typing import (
    Union,
    Any,
)

JSONType = Union[
    dict[str, Any],
    list[dict],
    list[Any]
]

class Network():
    __Network_instance = None

    def __init__(self):
        self.__token = None
        # self.__baseURL = 'http://3.15.30.244'
        # self.__baseURL = 'http://localhost:5000'
        # self.__baseURL = 'http://127.0.0.1:5000'
        self.__baseURL = 'http://3.145.140.55'

    @classmethod
    def get_Network_instance(cls) -> type[Network]:
        if cls.__Network_instance == None:
            cls.__Network_instance = Network()

        return cls.__Network_instance

    @property
    def base_url(self) -> str:
        """
        Get base url that is the ipv4 address of AWS server and return base url

        :returns: base url, a string of server ipv4 address

        :exception OSError: Placeholder.
        """
        return self.__baseURL

    @property
    def token(self) -> str:
        """
        Return the token

        :returns: token - string.

        :exception OSError: Placeholder.
        """
        # print("zz", self.__token)
        return self.__token

    @token.setter
    def token(self, token: str) -> bool:
        """
        Set token to new token

        :param token: string. Token sent by the server

        :returns: None

        :exception OSError: Placeholder.
        """
        self.__token = token
        # print("new_token", self.__token)
        return True

    def logout(self) -> None:
        """
        Handle user logout by setting the __token to None

        :returns: None

        :exception OSError: Placeholder.
        """
        try:
            self.__token = None
        except:
            print('Logout procedure wrong')
        return

    def add_prefix_to_url(
        self, prefix: str, url: str
    ) -> str:

        """
        Add prefix to url. Currently, prefix is the blueprint in backend(flask)

        :returns: String

        :exception OSError: Placeholder.
        """
        return '/' + prefix + url

    def add_suffix_to_url(
        self, url: str, suffix: str
    ) -> str:

        """
        Add suffix to url. Currently, suffix is user_id

        :returns: String

        :exception OSError: Placeholder.
        """
        return url + '/' + suffix

    def process_url(
        self, 
        prefix: str, 
        url: str, 
        suffix: str = None
    ) -> str:

        """
        Process url

        :returns: String

        :exception OSError: Placeholder.
        """
        if suffix == None:
            return self.add_prefix_to_url(prefix, url)
        return self.add_suffix_to_url(self.add_prefix_to_url(prefix, url), suffix)

    def get_request(
        self, url: str, token: str, request_name: str
    ) -> JSONType:

        try:
            request_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
        except:
            print(f'{request_name} request wrong!')
        
        return request_response

    def post_request(
        self, 
        url: str, 
        token: str, 
        request_name: str, 
        data: dict[str, Union(list[str], str)]
    ) -> JSONType:

        try:
            request_response = requests.post(
                url, 
                json=data, 
                headers={'Authorization': 'Bearer ' + token}
            )
        except:
            print(f'{request_name} request wrong!')

        return request_response

    
    def load_network_response(
        self,
        network_response: JSONType
    ) -> dict[str, Union(list[str], str)]:

        """
        start task with all assistors

        :param file_address: Integer. Maximum training round
        :param file_content: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        if hasattr(network_response, 'text'):
            network_response = network_response.text

        network_response = ParseJson.load_json_recursion(network_response)
        
        # if isinstance(json_data, dict):
        #     print('json_data', json_data.keys())
        # assert json_data is not None

        # if testing_key_value_pair:
        #     for item in testing_key_value_pair:
        #         key, value = item[0], item[1]
        #         print('key_value', key, value)
        #         # assert key in json_data.keys()
        #         if value:
        #             # assert json_data[key] == value
        #             pass
        return network_response