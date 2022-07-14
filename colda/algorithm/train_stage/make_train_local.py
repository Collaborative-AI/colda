from __future__ import annotations

import os
import colda
import numpy as np

from colda.algorithm.base import BaseAlgorithm

from colda.algorithm.utils import (
    save, 
    log, 
    parse_idx
)

from colda.algorithm.model.api import Model

from colda.algorithm.metric.metrics import Metric

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from typeguard import typechecked


class MakeTrainLocal(BaseAlgorithm):
    '''
    Sponsor train model locally(only use its dataset) 
    and get its performance

    Methods
    -------
    make_train_local
    '''

    @classmethod
    def make_train_local(
        cls,
        root: str, 
        self_id: str, 
        task_id: str, 
        dataset_path: str, 
        data_idx: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        metric_name: Metric_Name
    ) -> None:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        data_idx = parse_idx(data_idx)
        target_idx = parse_idx(target_idx)
        data = dataset[:, data_idx]
        target = dataset[:, target_idx]
        model = Model(task_mode, model_name)
        model.fit(data, target.reshape(-1))
        save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
        output = model.predict(data)
        metric = Metric(task_mode, metric_name)
        eval = metric.eval(output, target)
        msg = 'Train Local Client: {}, {}'.format(self_id, eval)
        log(msg, root, self_id, task_id)

        return (eval, )
