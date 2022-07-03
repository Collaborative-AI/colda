from __future__ import annotations

from colda.workflow.train_workflow.train_base import TrainBaseWorkflow

from colda.pi.api import get_user_id

from typing import Any

from typeguard import typechecked


#@typechecked
class TrainAssistorMatchIdentifier(TrainBaseWorkflow):
    '''
    Handle train assistor match identifier stage.

    Attributes
    ----------
    None

    Methods
    -------
    train_assistor_match_identifier
    '''

    @classmethod
    def train_assistor_match_identifier(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute train assistor match identifier logic.

        Parameters
        ----------
        train_id: str 
        train_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        user_id = get_user_id()

        msgs = [
            "---- 3. Unread Match ID", 
            "3.1 Update the match id notification",
            "3.2 unread_match_identifier_assistor",
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        data = {
            "train_id": train_id,
        }
        get_identifier_content_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_identifier_content',
            url_suffix=user_id,
            status_code=200
        )
        
        msgs = ["3.3 Assistor gets matched id file"]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        # handle the response from request, assistor only has one match_id_file. 
        sponsor_random_id_to_identifier_content_dict = get_identifier_content_response[
            'sponsor_random_id_to_identifier_content_dict'
        ]
        # get the first key of sponsor_random_id_to_identifier_content_dict
        sponsor_random_id = next(iter(sponsor_random_id_to_identifier_content_dict))
        sponsor_encrypted_identifer = sponsor_random_id_to_identifier_content_dict[sponsor_random_id]
        
        assistor_encrypted_identifier = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='assistor_encrypted_identifier',
        )
        # print('assistor_encrypted_identifier', assistor_encrypted_identifier)
        assistor_matched_identifer = super()._match_identifier(
            self_id_data=assistor_encrypted_identifier,
            from_id_data=sponsor_encrypted_identifer
        )

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='assistor_matched_identifer',
            algorithm_data=assistor_matched_identifer
        )

        # make_match_idx_done = make_match_idx(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # # assert make_match_idx_done is not None
        # _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # # assert make_match_idx_done is not None

        msgs = [
            "3.5 Assistor matches id to index", 
            "---- 3. Unread Match ID Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        print(f'Assistor: Training train_id: {train_id} is running')
        print('Assistor stage 2: match identifier done')
        return True
    
