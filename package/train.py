import argparse
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from utils import save, makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--data_path', default=None, type=str)
args = vars(parser.parse_args())


def main():
    self_id = args['self_id']
    task_id = args['task_id']
    from_id = args['from_id']
    round = args['round']
    data_path = args['round']
    data = np.genfromtxt(data_path, delimiter=',')
    target = np.genfromtxt(self_id, task_id, 'train', str(round), 'residual', '{}.csv.'.format(self_id),
                           delimiter=',')
    if from_id is not None:
        self_from_idx = np.genfromtxt(os.path.join(self_id, task_id, 'train', 'matched_idx', '{}.csv'.format(from_id)),
                                      delimiter=',').astype(np.int64)
        data = data[self_from_idx]
    model = LinearRegression().fit(data, target)
    save(model, os.path.join(self_id, task_id, 'train', str(round), 'model.pkl'))
    output = model.predict(data)
    makedir_exist_ok(os.path.join(self_id, task_id, 'train', str(round), 'output'))
    output_path = os.path.join(self_id, task_id, 'train', str(round), 'output', '{}.csv'.format(self_id))
    np.savetxt(output_path, output, delimiter=",")
    print(output_path)
    return


if __name__ == "__main__":
    main()
