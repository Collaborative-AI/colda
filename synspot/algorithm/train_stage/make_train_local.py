import numpy as np
import os
import synspot
from synspot.algorithm.base import BaseAlgorithm
from synspot.algorithm.utils import save, log, parse_idx
from synspot.algorithm.model.models import Model
from synspot.algorithm.metric.metrics import Metric

class MakeTrainLocal(BaseAlgorithm):
    '''
    暂时没动
    '''
    def make_train_local(
        self,
        root: str, 
        self_id: str, 
        task_id: str, 
        dataset_path: str, 
        data_idx: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: str, 
        model_name: str, 
        metric_name: str
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

        return '200?make_train_local?complete'
