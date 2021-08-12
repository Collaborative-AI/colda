import numpy as np
import os
from sklearn.linear_model import LinearRegression
from utils import save, makedir_exist_ok


def make_train(args):
    data_path = args['data_path']
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    from_id = args['from_id']
    round = args['round']
    data = np.genfromtxt(data_path, delimiter=',')
    target = np.genfromtxt(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual',
                                        '{}.csv'.format(self_id)), delimiter=',')
    if from_id is not None:
        self_from_idx = np.genfromtxt(
            os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx', '{}.csv'.format(from_id)),
            delimiter=',').astype(np.int64)
        data = data[self_from_idx]
    model = LinearRegression().fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))
    output = model.predict(data)
    output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
    makedir_exist_ok(output_path)
    output_path = os.path.join(output_path, '{}.csv'.format(self_id))
    np.savetxt(output_path, output, delimiter=",")
    print(output_path)
    return
