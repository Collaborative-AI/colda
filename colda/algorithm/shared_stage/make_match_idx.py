from __future__ import annotations
import os

import numpy as np

from colda.algorithm.base import BaseAlgorithm

from typing import (
    Any,
    Union
)
from typeguard import typechecked


#@typechecked
class MakeMatchIdx(BaseAlgorithm):
    '''
    Match the identifiers from other participants and
    current user's identifiers

    Attributes
    ----------
    None

    Methods
    -------
    make_match_idx
    '''

    @classmethod
    def make_match_idx(
        cls, 
        self_id_data: list[str],
        from_id_data: list[str],
    ) -> tuple[np.ndarray, ]:
        
        _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
        return (self_from_matched_idx, )
