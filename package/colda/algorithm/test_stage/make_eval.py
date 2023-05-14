from __future__ import annotations

import numpy as np
import os
import copy
import json
import collections

from algorithm.base import BaseAlgorithm

from algorithm.utils import (
    log, 
    parse_idx
)

from algorithm.metric.api import Metric

from typing import Any

from _typing import (
    Role,
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked


class MakeEval(BaseAlgorithm):
    '''
    Test model using the test dataset.
    Evaluate the predicted results 
    at each round. 

    Methods
    -------
    make_eval
    '''

    @classmethod
    def make_eval(
        cls, 
        user_id: str,
        test_id: str, 
        max_round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: Task_Mode, 
        metric_name: Metric_Name, 
        sponsor_test_cooperative_model_output_every_round: dict[str, Any],
        assistor_test_cooperative_model_output_every_round: dict[str, Any],
        trained_result_rounds_0: Any,
        trained_alpha_every_round: dict[str, Any],
        matched_identifier: dict[str, Any],
        role: Role
    ) -> tuple[dict, ]:

        result = trained_result_rounds_0
        if len(result.shape) == 0:
            result = result.reshape(-1)
        if len(result.shape) == 1:
            result = result.reshape(1, -1)

        if role == 'sponsor':
            dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
            target_idx = parse_idx(target_idx)
            target = dataset[:, target_idx]
            metric = Metric(task_mode, metric_name)
            result = result.repeat(target.shape[0], axis=0)
            eval = metric.eval(result, target)
            msg = 'Test Round: 0, {}'.format(eval)
        
        make_eval_res = collections.defaultdict(dict)
        for i in range(1, max_round + 1):
            rounds_key = f'rounds_{i}'
            output_i = sponsor_test_cooperative_model_output_every_round[rounds_key]
            output_i = output_i.reshape(output_i.shape[0], -1)
            count_i = np.ones((output_i.shape[0], 1))

            for assistor_random_id, tested_cooperative_model_output_every_round in assistor_test_cooperative_model_output_every_round.items():
                output_i_j = tested_cooperative_model_output_every_round[rounds_key]
                output_i_j = output_i_j.reshape(output_i_j.shape[0], -1)
                self_from_idx_j = matched_identifier[assistor_random_id]
                output_i[self_from_idx_j,] = output_i[self_from_idx_j,] + output_i_j
                count_i[self_from_idx_j,] = count_i[self_from_idx_j,] + 1

            output_i = output_i / count_i
            alpha = trained_alpha_every_round[rounds_key]
            result = result + alpha * output_i
            if role == 'sponsor':
                metric = Metric(task_mode, metric_name)
                eval, eval_dict = metric.eval(result, target)
                make_eval_res[rounds_key] = copy.deepcopy(eval_dict)
                msg = 'Test Round: {}, {}'.format(i, eval)

        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=make_eval_res,
            log_category='make_eval',
        )
        return (make_eval_res, )