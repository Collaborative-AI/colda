import numpy as np
import os
from sklearn.linear_model import LinearRegression
from utils import save, log, parse_idx


def make_train_local(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    dataset_path = args['dataset_path']
    data_idx = args['data_idx']
    target_idx = args['target_idx']
    dataset = np.genfromtxt(dataset_path, delimiter=',')
    data_idx = parse_idx(data_idx)
    target_idx = parse_idx(target_idx)
    data = dataset[:, data_idx]
    target = dataset[:, target_idx]
    model = LinearRegression().fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    loss = np.sqrt(((target - output) ** 2).mean())
    msg = 'Train Client: {}, RMSE: {}'.format(self_id, loss)
    log(msg, root, self_id, task_id)
    print('200?make_train_local?complete', end='')
    return
