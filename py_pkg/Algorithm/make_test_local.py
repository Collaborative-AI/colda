import numpy as np
import os
from algo_utils import load, log, parse_idx


def make_test_local(root, self_id, task_id, test_id, dataset_path, data_idx, target_idx):
    # root = args['root']
    # self_id = args['self_id']
    # task_id = args['task_id']
    # test_id = args['test_id']
    # dataset_path = args['dataset_path']
    # data_idx = args['data_idx']
    # target_idx = args['target_idx']
    dataset = np.genfromtxt(dataset_path, delimiter=',')
    data_idx = parse_idx(data_idx)
    target_idx = parse_idx(target_idx)
    data = dataset[:, data_idx]
    target = dataset[:, target_idx]
    model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    loss = np.sqrt(((target - output) ** 2).mean())
    msg = 'Test Client: {}, RMSE: {}'.format(self_id, loss)
    log(msg, root, self_id, task_id, test_id)
    return '200?make_test_local?complete'

