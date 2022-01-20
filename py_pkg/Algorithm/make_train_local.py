import numpy as np
import os
from utils import save, log, parse_idx
from models import Model
from metrics import Metric

def make_train_local(root, self_id, task_id, dataset_path, data_idx, target_idx, skip_header, task_mode, model_name, metric_name):

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
    print('200?make_train_local?complete', end='')
    return
