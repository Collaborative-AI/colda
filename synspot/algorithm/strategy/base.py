from __future__ import annotations

from typing import final

from synspot.algorithm.shared_stage import (
    MakeDataset,
    MakeHash,
    MakeMatchIdx,
    SaveMatchId,
    SaveOutput,
)

from synspot.algorithm.dp import DP



class BaseAlgorithmStrategy:

    @final
    def algorithm_process(self, func, **kwargs):
        kwargs = DP.process_input(**kwargs)
        # print('))))', kwargs)
        res = func(**kwargs)
        # print(')))res', len(res), res)
        res2 = DP.process_output(res)
        # print(')))res2', len(res2), res2)
        return res2

    @final
    def make_hash(self, **kwargs):
        return self.algorithm_process(MakeHash.make_hash, **kwargs)

    @final
    def make_match_idx(self, **kwargs):
        return self.algorithm_process(MakeMatchIdx.make_match_idx, **kwargs)

    @final
    def save_match_id(self, **kwargs):
        return self.algorithm_process(SaveMatchId.save_match_id, **kwargs)

    @final
    def save_output(self, **kwargs):
        return self.algorithm_process(SaveOutput.save_output, **kwargs)