

# from traitlets import default
# from ceshi2 import _default

# print(id(_default))

import os
import errno
import torch
import pickle
import numpy as np

from typing import Any
# import colda
# from tests.tests.api import Colda
# from authentication.api import Authentication
# from colda.short_polling.api import ShortPolling

# def create_path(
#     path: str
# ) -> None:
#     try:
#         os.makedirs(path)
#     except OSError as e:
#         if e.errno == errno.EEXIST:
#             pass
#         else:
#             raise
#     return

# def process_path(
#     fileName: str,
#     path: str,
#     mode: str
# ) -> str:
#     '''
#     Process path according to the mode
#     '''
#     if path[-1] != '/':
#         path = f'{path}/'

#     if mode == 'torch':
#         path = f'{path}{fileName}.pt'
#     elif mode == 'np':
#         path = f'{path}{fileName}.np'
#     elif mode == 'pickle':
#         path = f'{path}{fileName}.pkl'
#     return path


# def save(
#     input: Any,
#     fileName: str='Colda',
#     path: str='./',
#     mode: str='pickle'
# ) -> None:
#     # delete filename, return folder path
#     dirname = os.path.dirname(path)
#     print(f'dirname: {dirname}')
#     # create folder path
#     create_path(dirname)

#     path = process_path(
#         fileName=fileName,
#         path=path,
#         mode=mode
#     )

#     if mode == 'torch':
#         torch.save(input, path)
#     elif mode == 'np':
#         np.save(path, input, allow_pickle=True)
#     elif mode == 'pickle':
#         pickle.dump(input, open(path, 'wb'))
#     else:
#         raise ValueError('Not valid save mode')
#     return

# def load(
#     fileName: str='Colda',
#     path: str='./',
#     mode: str='pickle'
# ) -> Any:

#     path = process_path(
#         fileName=fileName,
#         path=path,
#         mode=mode
#     )

#     if mode == 'torch':
#         return torch.load(path, map_location=lambda storage, loc: storage)
#     elif mode == 'np':
#         return np.load(path, allow_pickle=True)
#     elif mode == 'pickle':
#         return pickle.load(open(path, 'rb'))
#     else:
#         raise ValueError('Not valid save mode')

# from ceshi3 import SHISHI

# class ceshi:
#     def __init__(self):
#         self.test_var = 5
#         self.shishi = SHISHI()

#     def save_test(self):
#         self.test_var = 50000
#         print(self.test_var)
#         print(id(self.shishi))
#         save(
#             input=self,
#         )

#         # instance = load()
#         # print(instance.test_var)
#         # print(id(instance.shishi))

#         # self.test_var = 4000
#         # print(self.test_var)

#         # self = instance
#         # print(self.test_var)
#         # print(id(self.shishi))

# if __name__ == '__main__':
#     print('6656')
#     a = ceshi()
#     a.save_test()

#     instance = load()
#     print(instance.test_var)
#     print(id(instance.shishi), instance.shishi.value)