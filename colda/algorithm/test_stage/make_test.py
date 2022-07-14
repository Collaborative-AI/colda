from __future__ import annotations

import os
import copy
import json
import collections
import numpy as np

from colda.algorithm.base import BaseAlgorithm

from colda.algorithm.utils import parse_idx

from colda._typing import Role

from typing import Any

from typeguard import typechecked


class MakeTest(BaseAlgorithm):
    '''
    Sponsor side:
        Utilize sponsor_trained_model at each round 
        to produce n(round number) predictions
    Assistor side:
        Utilize assistor_trained_model at each round 
        to produce n(round number) predictions

    Methods
    -------
    make_test
    '''

    @classmethod
    def make_test(
        cls, 
        user_id: str,
        test_id: str,
        max_round: int, 
        matched_identifier: dict[str],
        trained_models_of_each_round: dict[str, Any], 
        dataset_path: str, 
        data_idx: str, 
        skip_header: int,
        role: Role,
    ) -> dict[str, Any]:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        data_idx = parse_idx(data_idx)
        data = dataset[:, data_idx]

        if role == 'assistor':
            self_from_idx = matched_identifier
            data = data[self_from_idx]
  
        make_test_log = collections.defaultdict(list)
        outputs = {}
        for i in range(1, max_round + 1):
            rounds_key = f'rounds_{i}'
            model = trained_models_of_each_round[rounds_key]
            outputs[rounds_key] = model.predict(data)
            for j in range(4):
                make_test_log[rounds_key].append(copy.deepcopy(outputs[f'rounds_{i}'][j][0]))
                
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=make_test_log,
            log_category='make_test',
        )
        return (outputs, )
    
