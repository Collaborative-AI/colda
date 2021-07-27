import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--run', default='train', type=str)
args = vars(parser.parse_args())

root = 'exp'


def main():
    data_name = args['data_name']
    client_id = '0'
    task_id = args['task_id']
    round = args['round']
    run = args['run']
    client_ids = os.listdir(os.path.join(root, '{}'.format(data_name)))
    for i in range(len(client_ids)):
        if client_ids[i] != client_id and client_ids[i] != 'oracle':
            shutil.copy(os.path.join(root, data_name, client_ids[i], task_id, run, str(round), 'output',
                                     '{}.csv'.format(client_ids[i])),
                        os.path.join(root, data_name, client_id, task_id, run, str(round), 'output',
                                     '{}.csv'.format(client_ids[i])))
    return


if __name__ == "__main__":
    main()
