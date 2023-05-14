from __future__ import annotations

import json

from error import StatusCodeError

from typing import (
    Union,
    Any
)

from _typing import JSONType

from typeguard import typechecked


#@typechecked
class DP:
    '''
    Data processing
    Parse http response

    Methods
    -------
    load_network_response
    '''

    @classmethod
    def check_network_response(
        cls,
        network_response: JSONType,
        status_code: int=200
    ) -> None:
        '''
        Check status_code of network response

        Parameters
        ----------
        network_response : JSONType
        
        Returns
        -------
        None
        '''
        # print(f'network_response_0000: {network_response}, {network_response.status_code}')
        if network_response.status_code != status_code:
            status_code = network_response.status_code
            network_response = cls.load_network_response(network_response=network_response)
            if 'error_name' in network_response and 'error' in network_response:
                raise StatusCodeError(
                    f"Wrong network response. status code: {status_code}, error_name: {network_response['error_name']}, error: {network_response['error']}"
                )
            else:
                raise StatusCodeError(
                    f"Wrong network response, status code: {status_code}, error: {network_response}"
                )
        return

    @classmethod
    def load_network_response(
        cls,
        network_response: JSONType,
    ) -> Any:
        '''
        parse network response.
        Change JSONType data to dict type data

        Parameters
        ----------
        network_response : JSONType or Http
        
        Returns
        -------
        Any
        '''
        # print('yyy', network_response.json())
        # print(f'network_response_1: {network_response}')
        if hasattr(network_response, 'text'):
            network_response = network_response.text
        # print(f'network_response: {network_response}, {type(network_response)}')
        # print(f'network_response_2: {network_response}')
        try:
            return json.loads(network_response)
        except:
            return network_response