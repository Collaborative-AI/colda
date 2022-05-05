from __future__ import annotations

import os

from synspot.algorithm.base import BaseAlgorithm


class SaveMatchId(BaseAlgorithm):
    '''
    Delete in Package
    Return the path to store Match Id
    '''

    def save_match_id(
        self, 
        root: str, 
        self_id: str, 
        task_id: str, 
        mode: str, 
        from_id: str,
        test_id: str = None, 
    ) -> bool:

        if mode == 'train':
            # Database stores
            pass
            # match_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id')
            # makedir_exist_ok(match_id_path)
            # open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")
        elif mode == 'test' and test_id is not None:
            # Database stores
            pass
            # match_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id')
            # makedir_exist_ok(match_id_path)
            # open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")
        else:
            # print('300?save_match_id?not valid mode', end='')
            # raise error
            pass 
        # match_id_path = os.path.join(match_id_path, '{}.csv'.format(from_id))
        # return '200?save_match_id?{}'.format(match_id_path)

        return True
