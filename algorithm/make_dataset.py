import argparse
import numpy as np
import os
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--num_users', default=2, type=int)
args = vars(parser.parse_args())


def main():
    data_name = args['data_name']
    num_users = args['num_users']
    path = os.path.join('.', '{}_{}'.format(data_name, num_users))
    if os.path.exists(path):
        os.remove(path)
    feature_split = split_dataset(data_name, num_users)
    train_set, test_set = make_data(data_name)
    for i in range(num_users):
        train_id_i, train_data_i, train_target_i = train_set
        train_data_i = train_data_i[:, feature_split[i]]
        test_id_i, test_data_i, test_target_i = test_set
        test_data_i = test_data_i[:, feature_split[i]]
        makedir_exist_ok(os.path.join(path, str(i), 'train'))
        makedir_exist_ok(os.path.join(path, str(i), 'test'))
        np.savetxt(os.path.join(path, str(i), 'train', 'id.csv'), train_id_i, delimiter=",")
        np.savetxt(os.path.join(path, str(i), 'train', 'data.csv'), train_data_i, delimiter=",")
        np.savetxt(os.path.join(path, str(i), 'test', 'id.csv'), test_data_i, delimiter=",")
        np.savetxt(os.path.join(path, str(i), 'test', 'data.csv'), train_data_i, delimiter=",")
        if i == 0:
            np.savetxt(os.path.join(path, str(i), 'train', 'target.csv'), train_target_i, delimiter=",")
            np.savetxt(os.path.join(path, str(i), 'test', 'target.csv'), test_target_i, delimiter=",")
    return


def split_dataset(data_name, num_users):
    data_shape = {'Blob': [10], 'Iris': [4], 'Diabetes': [10], 'BostonHousing': [13], 'Wine': [13],
                  'BreastCancer': [30], 'QSAR': [41]}
    num_features = data_shape[data_name][-1]
    feature_split = list(np.array_split(np.random.permutation(num_features), num_users))
    return feature_split


def make_data(data_name):
    from sklearn.datasets import load_boston
    X, y = load_boston(return_X_y=True)
    perm = np.random.permutation(len(X))
    X, y = X[perm], y[perm].reshape(-1, 1)
    split_idx = int(X.shape[0] * 0.8)
    train_data, test_data = X[:split_idx].astype(np.float32), X[split_idx:].astype(np.float32)
    train_target, test_target = y[:split_idx].astype(np.float32), y[split_idx:].astype(np.float32)
    train_id, test_id = np.arange(len(train_data)).astype(np.int64), np.arange(len(test_data)).astype(np.int64)
    return (train_id, train_data, train_target), (test_id, test_data, test_target)


if __name__ == "__main__":
    main()
