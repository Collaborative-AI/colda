import argparse
import numpy as np
import os
from utils import load, makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--client_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    data_name = args['data_name']
    client_id = args['client_id']
    task_id = args['task_id']
    round = args['round']
    assert round > 0
    data = np.genfromtxt(os.path.join(data_name, client_id, 'test', 'data.csv'), delimiter=',')
    model = load(os.path.join(data_name, client_id, task_id, 'test', round, 'model.pkl'))
    output = model.predict(data)
    makedir_exist_ok(os.path.join(data_name, client_id, task_id, 'test', round, 'output'))
    np.savetxt(os.path.join(data_name, client_id, task_id, 'test', round, 'output', '{}.csv'.format(client_id)),
               output, delimiter=",")
    return


def make_init(target):
    init = np.mean(target)
    return init


def make_res(output, target):
    return 2 * (target - output)


if __name__ == "__main__":
    main()
