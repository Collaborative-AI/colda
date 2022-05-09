from __future__ import annotations

from tabnanny import check
import requests

from synspot.utils import ParseJson

from synspot.network.utils import check_status_code

from typing import (
    Union,
    Any,
)

from synspot._typing import JSONType

import warnings

from synspot.error import (
    StatusCodeWarning,
    StatusCodeError
)


class Network():
    __Network_instance = None

    def __init__(self):
        self.__token = ''
        # self.__baseURL = 'http://3.15.30.244'
        # self.__baseURL = 'http://localhost:5000'
        self.__baseURL = 'http://127.0.0.1:5000'
        # self.__baseURL = 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com/'

    @classmethod
    def get_instance(cls) -> type[Network]:
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

    def add_prefix_to_url(
        self, url_prefix: str, url_root: str
    ) -> str:

        """
        Add prefix to url. Currently, prefix is the blueprint in backend(flask)

        :returns: String

        :exception OSError: Placeholder.
        """

        return f'/{url_prefix}/{url_root}'

    def add_suffix_to_url(
        self, url_root: str, url_suffix: str
    ) -> str:

        """
        Add suffix to url. Currently, suffix is user_id

        :returns: String

        :exception OSError: Placeholder.
        """
        # return url + '/' + suffix
        return f'{url_root}/{url_suffix}'

    def process_url(
        self, 
        url_prefix: str, 
        url_root: str, 
        url_suffix: str = None
    ) -> str:

        """
        Process url

        :returns: String

        :exception OSError: Placeholder.
        """
        if url_suffix == None:
            return self.base_url + self.add_prefix_to_url(url_prefix, url_root)
        return self.base_url + self.add_suffix_to_url(self.add_prefix_to_url(url_prefix, url_root), url_suffix)

    def get_request(
        self, 
        url: str, 
        token: str, 
        request_name: str
    ) -> JSONType:

        # , headers = {'Authorization': 'Bearer ' + token}
        try:
            request_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
            # request_response = requests.get(url)
        except Exception as e:
            print(f'{request_name} request wrong! {e}')
        else:
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
        except Exception as e:
            print(f'{request_name} request wrong! {e}')
        else:
            return request_response


    def load_network_response(
        self,
        network_response: JSONType,
    ) -> dict[str, Union(list[str], str)]:

        """
        start task with all assistors

        :param file_address: Integer. Maximum training round
        :param file_content: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """
        
        # print('pre_network_response', network_response.json())

        if hasattr(network_response, 'text'):
            network_response = network_response.text

        
        network_response = ParseJson.load_json_recursion(network_response)
        # print('post_network_response', network_response)
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

    def get_request_chaining(
        self, 
        url_prefix: str,
        url_root: str,
        url_suffix: str,
        status_code: int = 200, 
    ) -> Union(dict[str, Union(list[str], str)], type[StatusCodeError]):

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
        
        print('get_response', network_response)
        if not check_status_code(network_response, status_code):
            return StatusCodeError

        return self.load_network_response(network_response)

    def post_request_chaining(
        self,  
        data: dict[str, Union(list[str], str)],
        url_prefix: str,
        url_root: str,
        url_suffix: str,
        status_code: int = 200,
    ) -> Union(dict[str, Union(list[str], str)], type[StatusCodeError]):

        url = self.process_url(
            url_prefix=url_prefix, 
            url_root=url_root, 
            url_suffix=url_suffix
        )
        # print('##post_url1', url, data)
        data = ParseJson.make_data_serializable(data)
        # print('##post_url2', data)

        network_response = self.post_request(
            url=url,
            token=self.__token,
            request_name=url_root,
            data=data
        )

        if not check_status_code(network_response, status_code):
            return StatusCodeError

        return self.load_network_response(network_response)


    
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