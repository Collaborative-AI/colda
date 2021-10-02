import argparse
import numpy as np
import os
from utils import load, parse_idx
from sklearn.linear_model import LinearRegression

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='BostonHousing', type=str)
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--num_users', default=None, type=int)
parser.add_argument('--task_id', default=None, type=int)
parser.add_argument('--match_rate', default=None, type=float)
args = vars(parser.parse_args())



def main():
    root = args['root']
    data_name = args['data_name']
    num_users = args['num_users']
    task_id = args['task_id']
    match_rate = args['match_rate']
    control = '_'.join([data_name, str(num_users), str(task_id), str(match_rate)])
    path = os.path.join(root, control)
    for i in range(num_users):
        _, data_i_idx, target_i_idx = load(os.path.join(path, str(i), 'idx.pkl'), mode='pickle')
        data_i_idx = parse_idx(data_i_idx)
        target_i_idx = parse_idx(target_i_idx)
        train_path = os.path.join(path, str(i), 'train')
        train_dataset = np.genfromtxt(os.path.join(train_path, 'dataset.csv'), delimiter=',')
        train_data = train_dataset[:, data_i_idx]
        train_target = train_dataset[:, target_i_idx]
        test_path = os.path.join(path, str(i), 'test')
        test_dataset = np.genfromtxt(os.path.join(test_path, 'dataset.csv'), delimiter=',')
        test_data = test_dataset[:, data_i_idx]
        test_target = test_dataset[:, target_i_idx]
        model = LinearRegression().fit(train_data, train_target)
        test_output = model.predict(test_data)
        loss = np.sqrt(((test_target - test_output) ** 2).mean())
        print('Test Client: {}, RMSE: {}'.format(i, loss))
    return


if __name__ == "__main__":
    main()
