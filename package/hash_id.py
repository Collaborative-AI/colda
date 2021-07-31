import argparse
import os
import numpy as np
import hashlib
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--id_path', default=None, type=str)
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--run', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)

args = vars(parser.parse_args())


def main():
    id_path = args['id_path']
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    run = args['run']
    test_id = args['test_id']
    id = np.genfromtxt(id_path, delimiter=',', dtype=np.str_)
    hash_id = np.array(list(map(make_hash, id)))
    if run == 'default':
        hash_id_path = os.path.join(root, self_id, run, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
    elif run == 'train':
        hash_id_path = os.path.join(root, self_id, 'task', task_id, run, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
    elif run == 'test' and test_id is not None:
        hash_id_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
    else:
        raise ValueError('Not valid run')
    print(hash_id_path)
    return


def make_hash(input):
    output = hashlib.sha256(str(input).encode('utf-8'))
    output = output.hexdigest()
    return output


if __name__ == "__main__":
    main()
