from __future__ import annotations

import os
import copy
import json
import collections
import numpy as np

from synspot.algorithm.base import BaseAlgorithm

from synspot.algorithm.utils import parse_idx

from synspot._typing import Role

from typing import Any


class MakeTest(BaseAlgorithm):

    '''
    Utilize the model of every round to get test output of new data of every round
    '''

    @classmethod
    def make_test(
        cls, 
        # root, 
        # self_id, 
        # task_id, 
        # test_id, 
        user_id: str,
        test_id: str,
        max_round: int, 
        matched_identifier: dict[str],
        trained_models_of_each_round: dict[str, Any],
        # from_id, 
        dataset_path: str, 
        data_idx: str, 
        skip_header: int,
        role: Role,
    ) -> dict[str, Any]:

        print('~~matched_identifier', matched_identifier)
        print('~~trained_models_of_each_round', trained_models_of_each_round)
        print('~~dataset_path', dataset_path)
        print('~~data_idx', data_idx)
        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        data_idx = parse_idx(data_idx)
        data = dataset[:, data_idx]

        if role == 'assistor':
        # if from_id is not None:
            # self_from_idx = np.genfromtxt(
            #     os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id)),
            #     delimiter=',').astype(np.int64)
            self_from_idx = matched_identifier
            data = data[self_from_idx]
  
        # print('make_test_data', data)
        # output_path = []
        make_test_res = collections.defaultdict(list)
        outputs = {}
        for i in range(1, max_round + 1):
            rounds_key = f'rounds_{i}'
            # model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(i), 'model.pkl'))
            # print('model', i, model)
            model = trained_models_of_each_round[rounds_key]
            outputs[rounds_key] = model.predict(data)
            for j in range(4):
                # make_test_res[i].append(output[j][0])
                make_test_res[rounds_key].append(copy.deepcopy(outputs[f'rounds_{i}'][j][0]))
                
            # output_path_i = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'round', str(i), 'output')
            # print('output_path_i', output_path_i)
            # makedir_exist_ok(output_path_i)
            # output_path_i = os.path.join(output_path_i, '{}.csv'.format(self_id))
            # np.savetxt(output_path_i, output, delimiter=",")
            # output_path.append(output_path_i)
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=make_test_res,
            log_category='make_test',
        )
        print('make_test_res', role, make_test_res)
        # output_path = '?'.join(output_path)
        # make_test_res = json.dumps(make_test_res)
        # return '200?make_test?{make_test_res}?{output_path}?{res}'.format(make_test_res = make_test_res, output_path = output_path, res=res)
        return (outputs, )
    
