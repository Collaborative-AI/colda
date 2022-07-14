from __future__ import annotations

import time
import requests

from colda.workflow.train_workflow.train_base import TrainBaseWorkflow

from colda.workflow.utils import obtain_notification_information

from colda.pi.api import get_user_id

from typing import Any

from typeguard import typechecked


#@typechecked
class TrainAssistorSituation(TrainBaseWorkflow):
    '''
    Handle train assistor situation stage.

    Methods
    -------
    train_assistor_situation
    '''

    @classmethod
    def train_assistor_situation(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute train assistor situation logic.
        1. Assistor get training target from sponsor
        2. Assistor trains the model
        3. Assistor sends the model output back to sponsor

        Parameters
        ----------
        train_id: str 
        train_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        user_id = get_user_id()
        sender_random_id, role, cur_rounds_num = obtain_notification_information(
            notification_dict=train_id_dict
        )

        msgs = [
            "---- 4. Unread Situation", 
            "4.1 Update the situation notification"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        data = {
            "train_id": train_id,
            "rounds": cur_rounds_num
        }
        get_situation_content_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_situation_content',
            url_suffix=user_id,
            status_code=200
        )
        # print('get_situation_content_response', get_situation_content_response)
        # handle response from above request
        situation_content = get_situation_content_response['situation_content']
        sender_random_id = get_situation_content_response['sender_random_id']

        if super()._async_checker(
            database_type='train_algorithm', 
            user_id=user_id, 
            task_id=train_id,
            algorithm_data_name='assistor_matched_identifer',
            stage='train',
            waiting_start_time=time.time()
        ) == False:
            return

        return cls.train_cooperative_model(
            user_id=user_id,
            train_id=train_id,
            rounds=cur_rounds_num,
            sender_random_id=sender_random_id,
            situation_content=situation_content,
        )

    @classmethod
    def train_cooperative_model(
        cls, 
        user_id: str,
        train_id: str, 
        rounds: int, 
        sender_random_id: str, 
        situation_content: Any
    ) -> None:
        ''' 
        Function to avoid async case.
        When assistor gets the situation content sent
        by sponsor, the assistor may not complete its
        match identifier stage. We need to wait till
        the matching stage complete.

        Parameters
        ----------
        user_id : str
        train_id : str
        rounds : int
        sender_random_id : str
        situation_content : Any

        Returns
        -------
        None
        '''
        train_assistor_metadata = super()._get_database_record(
            database_type='train_assistor_metadata',
            user_id=user_id,
            train_id=train_id
        )
        train_id = train_assistor_metadata[0]
        mode = train_assistor_metadata[1]
        task_mode = train_assistor_metadata[2] 
        model_name = train_assistor_metadata[3] 
        train_file_path = train_assistor_metadata[4] 
        train_id_column = train_assistor_metadata[5] 
        train_data_column = train_assistor_metadata[6]
        task_name = train_assistor_metadata[7] 
        task_description = train_assistor_metadata[8]

        assistor_matched_identifer = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='assistor_matched_identifer'
        )
        
        trained_cooperative_model, trained_cooperative_model_output = super()._train_cooperative_model(
            dataset_path=train_file_path,
            data_idx=train_data_column,
            skip_header=super()._skip_header,
            task_mode=task_mode,
            model_name=model_name,
            cur_round_residual=situation_content,
            role='assistor',
            matched_identifier=assistor_matched_identifer,
        )
        # print('trained_cooperative_model_output', trained_cooperative_model_output)
        # Store trained_cooperative_model for further testing
        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name=['trained_cooperative_model', f'rounds_{rounds}'],
            algorithm_data=trained_cooperative_model
        )
        
        msgs = [
            f'4.4 Assistor round {rounds} training done'
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        data = {
            "train_id": train_id,
            "output_content": trained_cooperative_model_output
        }
        send_output_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='send_output',
            url_suffix=user_id,
            status_code=200
        )

        msgs = [
            '4.5 Assistor sends output', 
            '---- 4. Unread Situation Done', 
            '---- Train stage done'
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        print(f'Assistor: Training train_id: {train_id} is running')
        print('Assistor stage 3: situation done')
        return True