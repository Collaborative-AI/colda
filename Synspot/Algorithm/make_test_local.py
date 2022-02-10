import numpy as np
import os
from utils import load, log, parse_idx
from metrics import Metric

def make_test_local(root,self_id, task_id, test_id, dataset_path, data_idx, target_idx, skip_header, task_mode, metric_name):

    dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
    data_idx = parse_idx(data_idx)
    target_idx = parse_idx(target_idx)
    data = dataset[:, data_idx]
    target = dataset[:, target_idx]
    model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    metric = Metric(task_mode, metric_name)
    eval = metric.eval(output, target)
    msg = 'Test Local Client: {}, {}'.format(self_id, eval)
    log(msg, root, self_id, task_id, test_id)
    return '200?make_test_local?complete'
