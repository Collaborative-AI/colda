import os
import errno
import torch
import pickle
import numpy as np

from typing import Any

def create_path(
    path: str
) -> None:
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    return

def process_path(
    fileName: str,
    path: str,
    mode: str
) -> str:
    '''
    Process path according to the mode
    '''
    if path[-1] != '/':
        path = f'{path}/'

    if mode == 'torch':
        path = f'{path}{fileName}.pt'
    elif mode == 'np':
        path = f'{path}{fileName}.np'
    elif mode == 'pickle':
        path = f'{path}{fileName}.pkl'
    return path


def save_file(
    input: Any,
    fileName: str='Colda',
    path: str=os.path.dirname(os.path.abspath(__file__)),
    mode: str='pickle'
) -> None:
    # delete filename, return folder path
    dirname = os.path.dirname(path)
    # print(f'dirname: {dirname}')
    # create folder path
    create_path(dirname)

    path = process_path(
        fileName=fileName,
        path=path,
        mode=mode
    )
    print(f'Saving path is: {path}')

    if mode == 'torch':
        torch.save(input, path)
    elif mode == 'np':
        np.save(path, input, allow_pickle=True)
    elif mode == 'pickle':
        pickle.dump(input, open(path, 'wb'))
    else:
        raise ValueError('Not valid save mode')
    return

def load_file(
    fileName: str='Colda',
    path: str=os.path.dirname(os.path.abspath(__file__)),
    mode: str='pickle'
) -> Any:

    path = process_path(
        fileName=fileName,
        path=path,
        mode=mode
    )

    if mode == 'torch':
        return torch.load(path, map_location=lambda storage, loc: storage)
    elif mode == 'np':
        return np.load(path, allow_pickle=True)
    elif mode == 'pickle':
        return pickle.load(open(path, 'rb'))
    else:
        raise ValueError('Not valid save mode')