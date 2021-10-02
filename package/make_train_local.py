import numpy as np
import os
from sklearn.linear_model import LinearRegression
from utils import save, log


def make_train_local(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    data_path = args['data_path']
    target_path = args['target_path']
    data = np.genfromtxt(data_path, delimiter=',')
    target = np.genfromtxt(target_path, delimiter=',')
    model = LinearRegression().fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'local', 'model.pkl'))
    output = model.predict(data)
    loss = np.sqrt(((target - output) ** 2).mean())
    msg = 'Train Client: {}, RMSE: {}'.format(self_id, loss)
    log(msg, root, self_id, task_id)
    print('200?make_train_local?complete', end='')
    return
