import argparse
import numpy as np
import os
from utils import load, makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--from_id', default=None, type=str)

parser.add_argument('--data_path', default=None, type=str)
args = vars(parser.parse_args())


def main():
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    round = args['round']
    from_id = args['from_id']
    data_path = args['data_path']
    data = np.genfromtxt(data_path, delimiter=',')
    if from_id is not None:
        self_from_idx = np.genfromtxt(
            os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id)),
            delimiter=',').astype(np.int64)
        data = data[self_from_idx]
    output_path = []
    for i in range(round + 1):
        model = load(os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(i), 'model.pkl'))
        output = model.predict(data)
        output_path_i = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'round', str(i), 'output')
        makedir_exist_ok(output_path_i)
        output_path_i = os.path.join(output_path_i, '{}.csv'.format(self_id))
        np.savetxt(output_path_i, output, delimiter=",")
        output_path.append(output_path_i)
    print('?'.join(output_path))
    return


if __name__ == "__main__":
    main()
