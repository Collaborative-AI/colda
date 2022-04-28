from typing import final

from synspot.algorithm.shared_stage import (
    MakeDataset,
    MakeHash,
    MakeMatchIdx,
    SaveMatchId,
    SaveOutput,
)

class BaseAlgorithm:

    @final
    def make_hash(self, *args):
        return MakeHash.make_hash(*args)

    @final
    def make_match_idx(self, *args):
        return MakeMatchIdx.make_match_idx(*args)

    @final
    def save_match_id(self, *args):
        return SaveMatchId.save_match_id(*args)

    @final
    def save_output(self, *args):
        return SaveOutput.save_output(*args)