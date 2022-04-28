import os
import numpy as np

from synspot.algorithm.base import BaseAlgorithm

from synspot.database import Database

from typing import (
    List,
    Any,
    Union
)

class MakeMatchIdx(BaseAlgorithm):
    '''
    Match the identifier from other participants with 
    '''

    def make_match_idx(
        self, 
        root: str, 
        self_id: str, 
        task_id: str, 
        mode: str, 
        test_id: str, 
        from_id: str,
        self_id_data: Union(List[str], Any),
        from_id_data: Union(List[str], Any),
    ) -> List[str]:
        pass
        # if mode == 'train':
        #     self_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id', '{}.csv'.format(self_id))
        #     from_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id', '{}.csv'.format(from_id))
        #     self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, mode, 'matched_idx')
        # elif mode == 'test' and test_id is not None:
        #     self_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id', '{}.csv'.format(self_id))
        #     from_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id', '{}.csv'.format(from_id))
        #     self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'matched_idx')
        # else:
        #     return '300?make_match_idx?not valid mode'
        # self_id_data = np.genfromtxt(self_id_path, delimiter=',', dtype=np.str_)
        # from_id_data = np.genfromtxt(from_id_path, delimiter=',', dtype=np.str_)

        # retrieve from DB
        # self_id_data = 5
        # from_id_data = 6

        _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
        # makedir_exist_ok(self_from_matched_idx_path)
        # np.savetxt(os.path.join(self_from_matched_idx_path, '{}.csv'.format(from_id)), self_from_matched_idx,
        #         delimiter=",")
        # print('66662')
        return self_from_matched_idx
