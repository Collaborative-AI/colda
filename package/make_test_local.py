import numpy as np
import os
from utils import load, log


def make_test_local(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    data_path = args['data_path']
    target_path = args['target_path']
    data = np.genfromtxt(data_path, delimiter=',')
    target = np.genfromtxt(target_path, delimiter=',')
    model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    loss = np.sqrt(((target - output) ** 2).mean())
    msg = 'Test Client: {}, RMSE: {}'.format(self_id, loss)
    log(msg, root, self_id, task_id, test_id)
    print('200?make_test_local?complete', end='')
    return
