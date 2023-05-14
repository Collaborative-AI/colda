import copy
import pytest
import numpy as np
import pandas as pd

from utils.api import Serialization

from error import DataNotSerializable

class TestSerialization:

    @pytest.mark.parametrize("data, expected", [
        (np.array(5), 5),
        (np.array([5]), [5]),
        ({6}, [6]),
        (None, None),
        ({'5': np.array([[1, 2, 3], [4, 5, 6]])}, {'5': [[1, 2, 3], [4, 5, 6]]}),
        ([{'5': np.array([[1, 2, 3], [4, 5, 6]])}, '6'], [{'5': [[1, 2, 3], [4, 5, 6]]}, '6'])
    ])
    def test_make_data_serializable(self, data, expected):
        assert expected == Serialization.make_data_serializable(
            data=data
        )