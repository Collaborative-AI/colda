import os
import numpy as np
import hashlib
from utils import makedir_exist_ok, parse_idx


def make_hash(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    mode = args['mode']
    test_id = args['test_id']
    dataset_path = args['dataset_path']
    id_idx = args['id_idx']
    skip_header = args['skip_header']
    dataset = np.genfromtxt(dataset_path, delimiter=',', dtype=np.str_, skip_header=skip_header)
    id_idx = parse_idx(id_idx)
    id = dataset[:, id_idx]
    hash_id = np.array(list(map(hash, id)))
    if mode == 'default':
        hash_id_path = os.path.join(root, self_id, mode, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
        hash_id_path = os.path.join(hash_id_path, '{}.csv'.format(self_id))
    elif mode == 'train':
        hash_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
        hash_id_path = os.path.join(hash_id_path, '{}.csv'.format(self_id))

        log_path = os.path.join(root, self_id, 'task', task_id, 'train')
        makedir_exist_ok(log_path)
        open(os.path.join(log_path, "log.txt"), "a")
    elif mode == 'test' and test_id is not None:
        hash_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id')
        makedir_exist_ok(hash_id_path)
        np.savetxt(os.path.join(hash_id_path, '{}.csv'.format(self_id)), hash_id, delimiter=",", fmt='%s')
        hash_id_path = os.path.join(hash_id_path, '{}.csv'.format(self_id))

        log_path = os.path.join(root, self_id, 'task', task_id, 'test', test_id)
        makedir_exist_ok(log_path)
        open(os.path.join(log_path, "log.txt"), "a")
    else:
        print('300?make_hash?not valid mode', end='')
        return
    print('200?make_hash?{}'.format(hash_id_path), end='')
    return


def hash(input):
    output = hashlib.sha256(str(input).encode('utf-8'))
    output = output.hexdigest()
    return output
