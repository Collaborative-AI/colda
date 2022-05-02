from __future__ import annotations

from typing import final

from synspot.algorithm.shared_stage import (
    MakeDataset,
    MakeHash,
    MakeMatchIdx,
    SaveMatchId,
    SaveOutput,
)

class BaseAlgorithmStrategy:

    @final
    def make_hash(self, **kwargs):
        return MakeHash.make_hash(**kwargs)

    @final
    def make_match_idx(self, **kwargs):
        return MakeMatchIdx.make_match_idx(**kwargs)

    @final
    def save_match_id(self, **kwargs):
        return SaveMatchId.save_match_id(**kwargs)

    @final
    def save_output(self, **kwargs):
        return SaveOutput.save_output(**kwargs)