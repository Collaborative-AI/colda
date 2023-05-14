from __future__ import annotations

from typing import final

from algorithm.common_stage.api import (
    MakeDataset,
    MakeHash,
    MakeMatchIdx,
)

from typing import Callable

from algorithm.strategy.utils import algorithm_process

from typeguard import typechecked

from _typing import Serializable_Datatype


#@typechecked
class BaseAlgorithmStrategy:
    '''
    Base class for algorithm
    1. Contains data processing for input and 
    output
    2. Contains shared stage:
            make_hash
            make_match_idx

    Methods
    -------
    algorithm_process
    make_hash
    make_match_idx
    '''

    @final
    @algorithm_process
    def make_hash(self, **kwargs) -> list:
        '''
        Common stage algo
        Call MakeHash.make_hash to hash
        identifiers

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return MakeHash.make_hash(**kwargs)

    @final
    @algorithm_process
    def make_match_idx(self, **kwargs) -> list:
        '''
        Common stage algo
        Call MakeMatchIdx.make_match_idx to
        match the identifiers between sponsor
        and assistor

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return MakeMatchIdx.make_match_idx(**kwargs)