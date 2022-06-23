from __future__ import annotations

import errno
import numpy as np
import os
import pickle


from typeguard import typechecked
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


def log(msg, root, self_id, task_id, test_id=None):
    if test_id is None:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'train'))
        log_path = os.path.join(root, self_id, 'task', task_id, 'train', 'log.txt')
    else:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'test', test_id))
        log_path = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'log.txt')
    with open(log_path, 'a') as f:
        f.write(msg + '\n')
    return


def parse_idx(idx):
    parsed_idx = []
    idx_list_comma = idx.split(',')
    for i in range(len(idx_list_comma)):
        idx_comma_i = idx_list_comma[i]
        idx_comma_list_i = idx_comma_i.split('-')
        if len(idx_comma_list_i) == 1:
            idx_i = [int(idx_comma_list_i[0]) - 1]
        elif len(idx_comma_list_i) == 2:
            start, end = idx_comma_list_i
            idx_i = list(range(int(start) - 1, int(end)))
        else:
            print('300?parse_idx?not valid idx')
        parsed_idx.extend(idx_i)
    return parsed_idx


def softmax(X, theta=1.0, axis=None):
    """
    Compute the softmax of each element along an axis of X.

    Parameters
    ----------
    X: ND-Array. Probably should be floats.
    theta (optional): float parameter, used as a multiplier
        prior to exponentiation. Default = 1.0
    axis (optional): axis to compute values along. Default is the
        first non-singleton axis.

    Returns an array the same size as X. The result will sum to 1
    along the specified axis.
    """
    # make X at least 2d
    y = np.atleast_2d(X)
    # find axis
    if axis is None:
        axis = next(j[0] for j in enumerate(y.shape) if j[1] > 1)
    # multiply y against the theta parameter,
    y = y * float(theta)
    # subtract the max for numerical stability
    y = y - np.expand_dims(np.max(y, axis=axis), axis)
    # exponentiate y
    y = np.exp(y)
    # take the sum along the specified axis
    ax_sum = np.expand_dims(np.sum(y, axis=axis), axis)
    # finally: divide elementwise
    p = y / ax_sum
    # flatten if X was 1D
    if len(X.shape) == 1: p = p.flatten()
    return p
