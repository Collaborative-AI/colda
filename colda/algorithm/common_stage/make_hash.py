from __future__ import annotations

import os
import numpy as np
import hashlib

from algorithm.base import BaseAlgorithm

from algorithm.utils import parse_idx

from _typing import Identifier_Type

from typeguard import typechecked


#@typechecked
class MakeHash(BaseAlgorithm):
    '''
    Hash the identifier of dataset

    Methods
    -------
    make_hash
    '''

    @classmethod
    def make_hash(
        cls,
        dataset_path: str, 
        id_idx: str, 
        skip_header: int, 
    ) -> tuple[np.ndarray, ]:

        dataset = np.genfromtxt(dataset_path, delimiter=',', dtype=np.str_, skip_header=skip_header)
        id_idx = parse_idx(id_idx)
        id = dataset[:, id_idx]
        hash_id = np.array(list(map(cls.__hash, id)))
        
        return (hash_id, )


    @classmethod
    def __hash(
        cls, input: Identifier_Type
    ) -> str:
        output = hashlib.sha256(str(input).encode('utf-8'))
        output = output.hexdigest()
        return output
