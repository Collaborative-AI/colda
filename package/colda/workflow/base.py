from __future__ import annotations

import time
import warnings
import threading

from network.api import Network

from pi.api import PI

from database.strategy.api import DatabaseOperator

from algorithm.strategy.api import BaseAlgorithmStrategy

from utils.log.api import GetWorkflowLog

from error import (
    StatusCodeWarning,
    StatusCodeError,
    DictValueNotFound,
    StopWarning
)

from typing import (
    final,
    Union,
    Any,
    Final,
)

from _typing import (
    Serializable_Datatype,
    Stage,
    Train_Database_Type,
    Test_Database_Type,
    Identifier_Type
)

from typeguard import typechecked


#@typechecked
class BaseWorkflow:
    '''
    Base class for workflow

    Attributes
    ----------
    _skip_header
    _initial_round_num
    _url_prefix
    _max_round

    Methods
    -------
    None
    '''

    _skip_header: Final[int] = 1
    _initial_round_num: Final[int] = 1
    _url_prefix: Final[str] = 'main_flow'
    _helper_api = 'helper_api'
    # _max_round: Final[int] = 3
    # _max_round = 2
    
    @final
    @classmethod
    def _get_request_chaining(
        cls, 
        task_id: str,
        url_prefix: str,
        url_root: str,
        url_suffix: str=None,
        status_code: int=200,
    ) -> Any:
        '''
        http get request

        Parameters
        ----------
        task_id : str
        url_prefix : str
        url_root : str
        url_suffix : str
        status_code : int

        Returns
        -------
        Any
        '''
        request_response = Network.get_instance().get_request_chaining(
            url_prefix=url_prefix,
            url_root=url_root,
            url_suffix=url_suffix,
            status_code=status_code,
        )

        # TODO: modify later, error handler
        # if request_response == StatusCodeError:
        #     warnings.warn(
        #         f"{task_id}'s network get request to {url_root} goes wrong", 
        #         StatusCodeWarning
        #     )
        
        return request_response

    @final
    @classmethod
    def _post_request_chaining(
        cls, 
        task_id: str,
        data: dict[str, Serializable_Datatype],
        url_prefix: str,
        url_root: str,
        url_suffix: str=None,
        status_code: int=200,
    ) -> Any:
        '''
        http post request

        Parameters
        ----------
        task_id : str
        data : dict[str, Serializable_Datatype]
        url_prefix : str
        url_root : str
        url_suffix : str
        status_code : int

        Returns
        -------
        Any
        '''
        request_response = Network.get_instance().post_request_chaining(
            data=data,
            url_prefix=url_prefix,
            url_root=url_root,
            url_suffix=url_suffix,
            status_code=status_code
        )

        # TODO: modify later, error handler
        # if request_response == StatusCodeError:
        #     warnings.warn(
        #         f"{task_id}'s network get request to {url_root} goes wrong", 
        #         StatusCodeWarning
        #     )

        return request_response

    @final
    @classmethod
    def _store_log(
        cls,
        user_id: str,
        task_id: str,
        msgs: list[str],
    ) -> None:
        '''
        Store workflow log

        Parameters
        ----------
        user_id : str
        task_id : str
        msgs : list[str]

        Returns
        -------
        None
        '''
        GetWorkflowLog.get_instance().store_log(
            user_id=user_id,
            task_id=task_id,
            msgs=msgs
        )
        return

    @final
    @classmethod
    def _store_database_record(
        cls,
        database_type: Union[Train_Database_Type, Test_Database_Type],
        **kwargs,
    ) -> None:
        '''
        Handle 2 things:
            1. set database strategy object
            2. store record to corresponding db

        Parameters
        ----------
        database_type : Union[Train_Database_Type, Test_Database_Type]
        **kwargs : Any

        Returns
        -------
        None
        '''
        DatabaseOperator.get_instance().set_database(
            database_type=database_type
        )

        DatabaseOperator.get_instance().store_record(
            **kwargs
        )
        return 
    
    @final
    @classmethod
    def _get_database_record(
        cls,
        database_type: Union[Train_Database_Type, Test_Database_Type],
        **kwargs,
    ) -> tuple[Any]:
        '''
        Handle 2 things:
            1. set database strategy object
            2. get record from corresponding db

        Parameters
        ----------
        database_type : Union[Train_Database_Type, Test_Database_Type]
        **kwargs : Any

        Returns
        -------
        None
        '''
        DatabaseOperator.get_instance().set_database(
            database_type=database_type
        )

        return DatabaseOperator.get_instance().get_record(
            **kwargs
        )

    @final
    @classmethod
    def _encrypt_identifier(
        cls,
        dataset_path: str,
        id_idx: str,
        skip_header: int
    ) -> list[Identifier_Type]:
        '''
        Call corresponding function in algorithm part

        Parameters
        ----------
        dataset_path : str
        id_idx : str
        skip_header : int

        Returns
        -------
        list[Identifier_Type]
        '''
        encrypted_identifer = BaseAlgorithmStrategy().make_hash(
                dataset_path=dataset_path, 
                id_idx=id_idx, 
                skip_header=skip_header
            )
        return encrypted_identifer
    
    @final
    @classmethod
    def _match_identifier(
        cls,
        self_id_data: list[str],
        from_id_data: list[str]
    ) -> list[str]:
        '''
        Call corresponding function in algorithm part

        Parameters
        ----------
        self_id_data: list[str],
        from_id_data: list[str]

        Returns
        -------
        list[str]
        '''
        matched_identifier = BaseAlgorithmStrategy().make_match_idx(
            self_id_data=self_id_data,
            from_id_data=from_id_data
        )
        return matched_identifier

    @final
    @classmethod
    def _async_checker(
        cls,
        database_type: str,
        user_id: str,
        task_id: str,
        algorithm_data_name: str,
        stage: Stage,
        waiting_start_time: type[time.time()]
    ) -> bool:

        if stage == 'train':
            res = cls._get_database_record(
                database_type=database_type,
                user_id=user_id,
                train_id=task_id,
                algorithm_data_name=algorithm_data_name
            )
        elif stage == 'test':
            res = cls._get_database_record(
                database_type=database_type,
                user_id=user_id,
                test_id=task_id,
                algorithm_data_name=algorithm_data_name
            )
        # print('((((((', res, type(res))
        print(f'async: {algorithm_data_name}')
        if res == DictValueNotFound:

            waiting_current_time = time.time()
            time_interval = waiting_current_time - waiting_start_time
            if time_interval > 30 * 60:
                warnings.warn(
                    'Sorry, the test stopped due to slow computation'
                )
                return False

            args = [
                database_type,
                user_id,
                task_id,
                algorithm_data_name,
                waiting_start_time
            ]
            threading.Timer(
                15, 
                cls._async_checker, 
                args
            )

        return True

    

