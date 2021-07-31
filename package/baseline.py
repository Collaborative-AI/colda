import argparse
import numpy as np
import os
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
    path = os.path.join(root, data_name, str(num_users), str(task_id), str(match_rate))
    for i in range(num_users):
        train_path = os.path.join(path, str(i), 'train')
        train_data = np.genfromtxt(os.path.join(train_path, 'data.csv'), delimiter=',')
        train_target = np.genfromtxt(os.path.join(train_path, 'target.csv'), delimiter=',')
        test_path = os.path.join(path, str(i), 'test')
        test_data = np.genfromtxt(os.path.join(test_path, 'data.csv'), delimiter=',')
        test_target = np.genfromtxt(os.path.join(test_path, 'target.csv'), delimiter=',')
        model = LinearRegression().fit(train_data, train_target)
        test_output = model.predict(test_data)
        loss = np.sqrt(((test_target - test_output) ** 2).mean())
        print('Test Client: {}, RMSE: {}'.format(i, loss))
    return


if __name__ == "__main__":
    main()
