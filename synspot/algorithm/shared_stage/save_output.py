from __future__ import annotations

import os

from synspot.algorithm.base import BaseAlgorithm


# from synspot.algorithm.utils import makedir_exist_ok


class SaveOutput(BaseAlgorithm):

    def save_output(
        self, 
        root: str, 
        self_id: str, 
        task_id: str, 
        mode: str, 
        round: str,
        from_id: str,
        test_id: str = None
    ) -> bool:

        if mode == 'train':
            # Database stores
            pass
            # output_path = os.path.join(root, self_id, 'task', task_id, mode, 'round', str(round), 'output')
            # makedir_exist_ok(output_path)
            # open(os.path.join(output_path, '{}.csv'.format(from_id)), "a")
        elif mode == 'test' and test_id is not None:
            # Database stores
            pass
            # output_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'round', str(round), 'output')
            # makedir_exist_ok(output_path)
            # open(os.path.join(output_path, '{}.csv'.format(from_id)), "a")
        else:
            # raise error
            pass
        
            # print('300?save_output?not valid mode', end='')
            # return
        # output_path = os.path.join(output_path, '{}.csv'.format(from_id))
        # return '200?save_output?{}'.format(output_path)
        return True
