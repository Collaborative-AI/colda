from __future__ import annotations

import os
import numpy as np

from synspot.algorithm.base import BaseAlgorithm

from synspot.algorithm.utils import parse_idx

from synspot.algorithm.model.models import Model

from typing import Any

from synspot._typing import Role


class MakeTrain(BaseAlgorithm):
    
    '''
    Train the model
    '''

    @classmethod
    def make_train(
        cls,
        # root: str, 
        # self_id: str, 
        # task_id: str, 
        # round: str, 
        dataset_path: str, 
        data_idx: str, 
        skip_header: int, 
        task_mode: str, 
        model_name: str, 
        cur_round_residual: Any,
        role: Role,
        matched_identifier: Any = None,
    ) -> tuple[Any, np.ndarray]:

        # return "300?make_train assistor cannot find match idx file"
        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        data_idx = parse_idx(data_idx)
        data = dataset[:, data_idx]
        data = data.reshape(data.shape[0], -1)
        # target = np.genfromtxt(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual',
        #                                     '{}.csv'.format(self_id)), delimiter=',')
        # target = cur_round_residual
        cur_round_residual = cur_round_residual.reshape(cur_round_residual.shape[0], -1)

        # assostor
        if role == 'assistor':
        # if from_id is not None:
            # match_idx_file_location = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx',
            #                                     '{}.csv'.format(from_id))
            # if not os.path.exists(match_idx_file_location):
            #     return "300?make_train assistor cannot find match idx file"
            
            # self_from_idx = np.genfromtxt(
            #     os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx', '{}.csv'.format(from_id)),
            #     delimiter=',').astype(np.int64)

            # self_from_idx = matched_identifier
            data = data[matched_identifier]
        model = Model(task_mode, model_name)
        model.fit(data, cur_round_residual)
        # save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))
        trained_output = model.predict(data)
        # output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
        # makedir_exist_ok(output_path)
        # output_path = os.path.join(output_path, '{}.csv'.format(self_id))
        # np.savetxt(output_path, output, delimiter=",")
        # output = output.tolist()
        return model, trained_output
