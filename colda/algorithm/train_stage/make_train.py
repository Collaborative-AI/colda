from __future__ import annotations
import time
import os
import numpy as np

from algorithm.base import BaseAlgorithm

from algorithm.utils import parse_idx

from algorithm.model.api import Model

from typing import Any

from _typing import (
    Role,
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked
# make the type same I/O



class MakeTrain(BaseAlgorithm):
    '''
    Train the model

    Methods
    -------
    make_train
    '''

    @classmethod
    def make_train(
        cls,
        dataset_path: str, 
        data_idx: str, 
        skip_header: int, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        cur_round_residual: Any,
        role: Role,
        matched_identifier: Any = None,
    ) -> tuple[Any, np.ndarray]:
        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        data_idx = parse_idx(data_idx)
        data = dataset[:, data_idx]
        data = data.reshape(data.shape[0], -1)
        cur_round_residual = cur_round_residual.reshape(cur_round_residual.shape[0], -1)

        # assostor
        if role == 'assistor':
            print("current role is assistor")
            print(data.shape)
            data = data[matched_identifier]
        model = Model(task_mode, model_name)
        
        model.fit(data, cur_round_residual)
        
        trained_output = model.predict(data)
        
        return model, trained_output
