import errno
import numpy as np
import os
import pickle


def makedir_exist_ok(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    return


def save(input, path, mode='pickle'):
    dirname = os.path.dirname(path)
    makedir_exist_ok(dirname)
    if mode == 'torch':
        torch.save(input, path)
    elif mode == 'np':
        np.save(path, input, allow_pickle=True)
    elif mode == 'pickle':
        pickle.dump(input, open(path, 'wb'))
    else:
        raise ValueError('Not valid save mode')
    return


def load(path, mode='pickle'):
    if mode == 'torch':
        return torch.load(path, map_location=lambda storage, loc: storage)
    elif mode == 'np':
        return np.load(path, allow_pickle=True)
    elif mode == 'pickle':
        return pickle.load(open(path, 'rb'))
    else:
        raise ValueError('Not valid save mode')
    return


def log(msg, self_id, task_id, test_id=None):
    if test_id is None:
        log_path = os.path.join('Local_Data', self_id, task_id, 'train', 'Log.txt')
    else:
        log_path = os.path.join('Local_Data', self_id, task_id, 'test', test_id, 'Log.txt')
    with open(log_path, 'a''') as f:
        f.write(msg + '\n')
    return
