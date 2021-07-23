import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    data_name = args['data_name']
    client_id = '0'
    task_id = args['task_id']
    round = args['round']
    client_ids = os.listdir(os.path.join('.', '{}'.format(data_name)))
    for i in range(len(client_ids)):
        if client_ids[i] != client_id:
            if round == 0:
                shutil.copy(os.path.join(data_name, client_id, task_id, 'train', round, 'init.csv'),
                            os.path.join(data_name, client_ids[i], task_id, 'train', round, 'init.csv'))
            shutil.copy(os.path.join(data_name, client_id, task_id, 'train', round, 'res.csv'),
                        os.path.join(data_name, client_ids[i], task_id, 'train', round, 'res.csv'))
    return


if __name__ == "__main__":
    main()
