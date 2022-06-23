from __future__ import annotations

from typing import final

from colda.algorithm.shared_stage.api import (
    MakeDataset,
    MakeHash,
    MakeMatchIdx,
)

from typing import Callable

from colda.algorithm.dp import DP

from typeguard import typechecked

from colda._typing import Serializable_Datatype


#@typechecked
class BaseAlgorithmStrategy:
    '''
    Base class for algorithm
    1. Contains data processing for input and 
    output
    2. Contains shared stage:
            make_hash
            make_match_idx

    Attributes
    ----------
    None

    Methods
    -------
    algorithm_process
    make_hash
    make_match_idx
    '''

    @final
    def algorithm_process(
        self, 
        func: Callable, 
        **kwargs
    ) -> Serializable_Datatype:
        '''
        1. Process the input that pass into
        all the algorithm methods. Mainly change
        list to np.array
        2. Process the output that generated from
        all the algorithm methods. Mainly change
        np.array to list

        Parameters
        ----------
        func : Callable
        **kwargs : Any

        Returns
        -------
        JSONType
        '''
        kwargs = DP.process_input(**kwargs)
        res = func(**kwargs)  
        res = DP.process_output(res)
        return res

    @final
    def make_hash(self, **kwargs) -> list:
        '''
        Call MakeHash.make_hash to hash
        identifiers

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.algorithm_process(MakeHash.make_hash, **kwargs)

    @final
    def make_match_idx(self, **kwargs) -> list:
        '''
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
        return self.algorithm_process(MakeMatchIdx.make_match_idx, **kwargs)