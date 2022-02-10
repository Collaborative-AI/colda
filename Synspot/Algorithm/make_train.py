import numpy as np
import os
from utils import save, makedir_exist_ok, parse_idx
from models import Model

def make_train(root, self_id, task_id, round, dataset_path, data_idx, skip_header, task_mode, model_name, from_id=None):
    # return "300?make_train assistor cannot find match idx file"
    dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
    data_idx = parse_idx(data_idx)
    data = dataset[:, data_idx]
    data = data.reshape(data.shape[0], -1)
    target = np.genfromtxt(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual',
                                        '{}.csv'.format(self_id)), delimiter=',')
    target = target.reshape(target.shape[0], -1)
    if from_id is not None:
        match_idx_file_location = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx',
                                               '{}.csv'.format(from_id))
        if not os.path.exists(match_idx_file_location):
            return "300?make_train assistor cannot find match idx file"
        self_from_idx = np.genfromtxt(
            os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx', '{}.csv'.format(from_id)),
            delimiter=',').astype(np.int64)
        data = data[self_from_idx]
    model = Model(task_mode, model_name)
    model.fit(data, target)
    save(model, os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'model.pkl'))
    output = model.predict(data)
    output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
    makedir_exist_ok(output_path)
    output_path = os.path.join(output_path, '{}.csv'.format(self_id))
    np.savetxt(output_path, output, delimiter=",")
    return '200?make_train?{}'.format(output_path)
