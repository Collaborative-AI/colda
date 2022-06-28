from __future__ import annotations

import json

from colda.error import StatusCodeError

from typing import (
    Union,
    Any
)

from colda._typing import JSONType

from typeguard import typechecked


#@typechecked
class DP:
    '''
    Data processing
    Parse http response

    Attributes
    ----------
    None

    Methods
    -------
    load_network_response
    '''

    @classmethod
    def check_network_response(
        cls,
        network_response: JSONType,
        status_code: int
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
        if network_response.status_code != status_code:
            raise StatusCodeError(
                'Network response has wrong status code'
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
        network_response : JSONType
        
        Returns
        -------
        Any
        '''
        if hasattr(network_response, 'text'):
            network_response = network_response.text

        return json.loads(network_response)