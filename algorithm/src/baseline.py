import argparse
import numpy as np
import os
from utils import load, parse_idx
from models import Model
from metrics import Metric

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='BostonHousing', type=str)
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--num_users', default=None, type=int)
parser.add_argument('--task_id', default=None, type=int)
parser.add_argument('--match_rate', default=None, type=float)
parser.add_argument('--skip_header', default=1, type=int)
parser.add_argument('--task_mode', default=None, type=str)
parser.add_argument('--model_name', default=None, type=str)
parser.add_argument('--metric_name', default=None, type=str)
args = vars(parser.parse_args())



def main():
    root = args['root']
    data_name = args['data_name']
    num_users = args['num_users']
    task_id = args['task_id']
    match_rate = args['match_rate']
    skip_header = args['skip_header']
    task_mode = args['task_mode']
    model_name = args['model_name']
    metric_name = args['metric_name']
    control = '_'.join([data_name, str(num_users), str(task_id), str(match_rate)])
    path = os.path.join(root, control)
    for i in range(num_users):
        _, data_i_idx, target_i_idx = load(os.path.join(path, str(i), 'idx.pkl'), mode='pickle')
        data_i_idx = parse_idx(data_i_idx)
        target_i_idx = parse_idx(target_i_idx)
        train_path = os.path.join(path, str(i), 'train')
        train_dataset = np.genfromtxt(os.path.join(train_path, 'dataset.csv'), delimiter=',', skip_header=skip_header)
        train_data = train_dataset[:, data_i_idx]
        train_target = train_dataset[:, target_i_idx]
        test_path = os.path.join(path, str(i), 'test')
        test_dataset = np.genfromtxt(os.path.join(test_path, 'dataset.csv'), delimiter=',', skip_header=skip_header)
        test_data = test_dataset[:, data_i_idx]
        test_target = test_dataset[:, target_i_idx]
        model = Model(task_mode, model_name)
        model.fit(train_data, train_target.reshape(-1))
        train_output = model.predict(train_data)
        test_output = model.predict(test_data)
        metric = Metric(task_mode, metric_name)
        train_eval = metric.eval(train_output, train_target)
        test_eval = metric.eval(test_output, test_target)
        print('Train Baseline Client: {}, {}'.format(i, train_eval))
        print('Test Baseline Client: {}, {}'.format(i, test_eval))
    return


if __name__ == "__main__":
    main()
