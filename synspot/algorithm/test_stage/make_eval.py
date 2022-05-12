from __future__ import annotations

import numpy as np
import os
import copy
import json
import collections

from synspot.algorithm.base import BaseAlgorithm

from synspot.algorithm.utils import (
    log, 
    parse_idx
)

from synspot.algorithm.metric import Metric

from typing import Any

from synspot._typing import Role


class MakeEval(BaseAlgorithm):

    '''
    Evaluate the xx of each round on the new data
    '''

    @classmethod
    def make_eval(
        cls, 
        # root: str, 
        # self_id: str, 
        # task_id: str, 
        user_id: str,
        test_id: str, 
        max_round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: str, 
        metric_name: str, 
        sponsor_test_cooperative_model_output_every_round: dict[str, Any],
        assistor_test_cooperative_model_output_every_round: dict[str, Any],
        trained_result_rounds_0: Any,
        trained_alpha_every_round: dict[str, Any],
        matched_identifier: dict[str, Any],
        role: Role
        # task_path: str
    ) -> list:

        print('sponsor_test_cooperative_model_output_every_round',sponsor_test_cooperative_model_output_every_round)
        print('assistor_test_cooperative_model_output_every_round', assistor_test_cooperative_model_output_every_round)
        print('trained_result_rounds_0', trained_result_rounds_0)
        print('trained_alpha_every_round', trained_alpha_every_round)
        print('matched_identifier', matched_identifier)
        print('dataset_path', dataset_path)
        # task_path = os.path.join(root, self_id, 'task', task_id)
        # result = np.genfromtxt(os.path.join(task_path, 'train', 'round', '0', 'result.csv'), delimiter=',')
        result = trained_result_rounds_0
        if len(result.shape) == 0:
            result = result.reshape(-1)
        if len(result.shape) == 1:
            result = result.reshape(1, -1)

        if role == 'sponsor':
        # if dataset_path is not None and target_idx is not None:
            dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
            target_idx = parse_idx(target_idx)
            target = dataset[:, target_idx]
            metric = Metric(task_mode, metric_name)
            result = result.repeat(target.shape[0], axis=0)
            eval = metric.eval(result, target)
            msg = 'Test Round: 0, {}'.format(eval)
            # log(msg, root, self_id, task_id, test_id)

        # result_path = []

        # for i in range(1, max_round + 1):
        #     sponsor_test_result_path = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output',
        #                                             '{}.csv'.format(self_id))
        #     if not os.path.exists(sponsor_test_result_path):
        #         print('testss', i, sponsor_test_result_path)
        #         return "300?make_eval sponsor cannot find test output file"
        
        make_eval_res = collections.defaultdict(dict)
        for i in range(1, max_round + 1):
            rounds_key = f'rounds_{i}'
            # output_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output')
            # output_i = np.genfromtxt(os.path.join(output_path_i, '{}.csv'.format(self_id)), delimiter=',')
            output_i = sponsor_test_cooperative_model_output_every_round[rounds_key]
            output_i = output_i.reshape(output_i.shape[0], -1)
            count_i = np.ones((output_i.shape[0], 1))
            # output_files = os.listdir(output_path_i)
            '''
            每个assistor在当前round的test结果
            '''
            # for j in range(len(output_files)):
            #     from_id_j = os.path.splitext(output_files[j])[0]
            #     if from_id_j != self_id:
            #         output_i_j = np.genfromtxt(os.path.join(output_path_i, output_files[j]), delimiter=',')
            #         output_i_j = output_i_j.reshape(output_i_j.shape[0], -1)
            #         self_from_idx_j = np.genfromtxt(
            #             os.path.join(task_path, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id_j)),
            #             delimiter=',').astype(np.int64)
            #         output_i[self_from_idx_j,] = output_i[self_from_idx_j,] + output_i_j
            #         count_i[self_from_idx_j,] = count_i[self_from_idx_j,] + 1

            for assistor_random_id, tested_cooperative_model_output_every_round in assistor_test_cooperative_model_output_every_round.items():
                # from_id_j = os.path.splitext(output_files[j])[0]
                # if from_id_j != self_id:
                output_i_j = tested_cooperative_model_output_every_round[rounds_key]
                output_i_j = output_i_j.reshape(output_i_j.shape[0], -1)
                self_from_idx_j = matched_identifier[assistor_random_id]
                output_i[self_from_idx_j,] = output_i[self_from_idx_j,] + output_i_j
                count_i[self_from_idx_j,] = count_i[self_from_idx_j,] + 1

            output_i = output_i / count_i
            # alpha = np.genfromtxt(os.path.join(task_path, 'train', 'round', str(i), 'alpha.csv'), delimiter=',')
            alpha = trained_alpha_every_round[rounds_key]
            result = result + alpha * output_i
            # result_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'result.csv')
            # result_path.append(result_path_i)
            # np.savetxt(result_path_i, result, delimiter=",")
            # if dataset_path is not None and target_idx is not None:
            if role == 'sponsor':
                metric = Metric(task_mode, metric_name)
                eval, eval_dict = metric.eval(result, target)
                make_eval_res[rounds_key] = copy.deepcopy(eval_dict)
                msg = 'Test Round: {}, {}'.format(i, eval)
                # log(msg, root, self_id, task_id, test_id)

        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=make_eval_res,
            log_category='make_eval',
        )
        # result_path = '?'.join(result_path)
        # make_eval_res = json.dumps(make_eval_res)
        # return '200?make_eval?{make_eval_res}?{result_path}'.format(make_eval_res = make_eval_res, result_path = result_path)
        return (make_eval_res, )