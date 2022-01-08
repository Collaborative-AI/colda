import numpy as np
import os
import json
import collections
from utils import load, makedir_exist_ok, parse_idx


def make_test(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    round = args['round']
    from_id = args['from_id']
    dataset_path = args['dataset_path']
    data_idx = args['data_idx']
    skip_header = args['skip_header']
    dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
    data_idx = parse_idx(data_idx)
    data = dataset[:, data_idx]
    if from_id is not None:
        self_from_idx = np.genfromtxt(
            os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id)),
            delimiter=',').astype(np.int64)
        data = data[self_from_idx]
    output_path = []
    make_test_res = collections.defaultdict(list)
    for i in range(1, round + 1):
        model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(i), 'model.pkl'))
        output = model.predict(data)
        for j in range(4):
            make_test_res[i].append(output[j][0])
        # print('?make_test_resjian1',output)
        output_path_i = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'round', str(i), 'output')
        makedir_exist_ok(output_path_i)
        output_path_i = os.path.join(output_path_i, '{}.csv'.format(self_id))
        np.savetxt(output_path_i, output, delimiter=",")
        output_path.append(output_path_i)
    output_path = '?'.join(output_path)
    make_test_res = json.dumps(make_test_res)
    print('200?make_test?{make_test_res}?{output_path}'.format(make_test_res = make_test_res, output_path = output_path), end='')
    return
