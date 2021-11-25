import numpy as np
import os
from utils import load, log, parse_idx


def make_test_local(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    dataset_path = args['dataset_path']
    data_idx = args['data_idx']
    target_idx = args['target_idx']
    skip_header = args['skip_header']
    dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
    data_idx = parse_idx(data_idx)
    target_idx = parse_idx(target_idx)
    data = dataset[:, data_idx]
    target = dataset[:, target_idx]
    model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    loss = np.sqrt(((target - output) ** 2).mean())
    msg = 'Test Local Client: {}, RMSE: {}'.format(self_id, loss)
    log(msg, root, self_id, task_id, test_id)
    print('200?make_test_local?complete', end='')
    return
