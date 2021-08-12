import argparse
import numpy as np
import os
import shutil
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--data_name', default=None, type=str)
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
    np.random.seed(task_id)
    path = os.path.join(root, data_name, str(num_users), str(task_id), str(match_rate))
    if os.path.exists(path):
        shutil.rmtree(path)
    feature_split = split_dataset(data_name, num_users)
    train_set, test_set = make_data(data_name)
    train_id, train_data, train_target = train_set
    test_id, test_data, test_target = test_set
    for i in range(num_users):
        if i == 0:
            match_rate_i = 1.
        else:
            match_rate_i = match_rate
        train_match_size = int(len(train_id) * match_rate_i)
        test_match_size = int(len(test_id) * match_rate_i)
        train_random_i = np.random.choice(np.arange(len(train_id)), train_match_size, replace=False)
        test_random_i = np.random.choice(np.arange(len(test_id)), test_match_size, replace=False)
        train_id_i = train_id[train_random_i]
        test_id_i = test_id[test_random_i]
        all_id_i = np.concatenate([train_id_i, test_id_i], axis=0)
        train_data_i = train_data[train_random_i.reshape(-1, 1), feature_split[i].reshape(1, -1)]
        test_data_i = test_data[test_random_i.reshape(-1, 1), feature_split[i].reshape(1, -1)]
        all_data_i = np.concatenate([train_data_i, test_data_i], axis=0)
        train_target_i = train_target[train_random_i]
        test_target_i = test_target[test_random_i]
        all_target_i = np.concatenate([train_target_i, test_target_i], axis=0)
        print('Client: {}, Train: ({}, {}), Test: ({}, {}), All: ({}, {})'.format(i,
                                                                                  train_data_i.shape,
                                                                                  train_target_i.shape,
                                                                                  test_data_i.shape,
                                                                                  test_target_i.shape, all_data_i.shape,
                                                                                  all_target_i.shape))
        train_path = os.path.join(path, str(i), 'train')
        makedir_exist_ok(train_path)
        np.savetxt(os.path.join(train_path, 'id.csv'), train_id_i, delimiter=",")
        np.savetxt(os.path.join(train_path, 'data.csv'), train_data_i, delimiter=",")
        np.savetxt(os.path.join(train_path, 'target.csv'), train_target_i, delimiter=",")
        test_path = os.path.join(path, str(i), 'test')
        makedir_exist_ok(test_path)
        np.savetxt(os.path.join(test_path, 'id.csv'), test_id_i, delimiter=",")
        np.savetxt(os.path.join(test_path, 'data.csv'), test_data_i, delimiter=",")
        np.savetxt(os.path.join(test_path, 'target.csv'), test_target_i, delimiter=",")
        all_path = os.path.join(path, str(i), 'all')
        makedir_exist_ok(all_path)
        np.savetxt(os.path.join(all_path, 'id.csv'), all_id_i, delimiter=",")
        np.savetxt(os.path.join(all_path, 'data.csv'), all_data_i, delimiter=",")
        np.savetxt(os.path.join(all_path, 'target.csv'), all_target_i, delimiter=",")
    return


def split_dataset(data_name, num_users):
    data_shape = {'Blob': [10], 'Iris': [4], 'Diabetes': [10], 'BostonHousing': [13], 'Wine': [13],
                  'BreastCancer': [30], 'QSAR': [41]}
    num_features = data_shape[data_name][-1]
    feature_split = list(np.array_split(np.random.permutation(num_features), num_users))
    return feature_split


def make_data(data_name):
    if data_name == 'BostonHousing':
        from sklearn.datasets import load_boston
        data, target = load_boston(return_X_y=True)
        perm = np.random.permutation(len(data))
        data, target = data[perm], target[perm].reshape(-1, 1)
        split_idx = int(data.shape[0] * 0.8)
        train_data, test_data = data[:split_idx].astype(np.float32), data[split_idx:].astype(np.float32)
        train_target, test_target = target[:split_idx].astype(np.float32), target[split_idx:].astype(np.float32)
        id = np.arange(len(data)).astype(np.int64)
        train_id, test_id = id[:split_idx], id[split_idx:]
    else:
        raise ValueError('Not valid data name')
    return (train_id, train_data, train_target), (test_id, test_data, test_target)


if __name__ == "__main__":
    main()
