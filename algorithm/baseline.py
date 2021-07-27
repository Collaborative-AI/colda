import argparse
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from utils import save, makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--client_id', default=None, type=str)
args = vars(parser.parse_args())

root = 'exp'


def main():
    data_name = args['data_name']
    client_id = args['client_id']
    if client_id == 'oracle':
        train_data = np.genfromtxt(os.path.join(root, data_name, 'oracle', 'train', 'data.csv'), delimiter=',')
        test_data = np.genfromtxt(os.path.join(root, data_name, 'oracle', 'test', 'data.csv'), delimiter=',')
        train_target = np.genfromtxt(os.path.join(root, data_name, 'oracle', 'train', 'target.csv'), delimiter=',')
        test_target = np.genfromtxt(os.path.join(root, data_name, 'oracle', 'test', 'target.csv'), delimiter=',')
    else:
        train_data = np.genfromtxt(os.path.join(root, data_name, client_id, 'train', 'data.csv'), delimiter=',')
        test_data = np.genfromtxt(os.path.join(root, data_name, client_id, 'test', 'data.csv'), delimiter=',')
        train_target = np.genfromtxt(os.path.join(root, data_name, '0', 'train', 'target.csv'),
                                     delimiter=',')
        test_target = np.genfromtxt(os.path.join(root, data_name, '0', 'test', 'target.csv'),
                                    delimiter=',')
    model = LinearRegression().fit(train_data, train_target)
    test_output = model.predict(test_data)
    loss = np.sqrt(((test_target - test_output) ** 2).mean())
    print('Client: {}, RMSE: {}'.format(client_id, loss))
    return


if __name__ == "__main__":
    main()
