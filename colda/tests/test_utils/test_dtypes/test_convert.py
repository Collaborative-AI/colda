import copy
import pytest
import numpy as np
import pandas as pd

from colda.utils.dtypes.api import to_serializable

from colda.error import DataNotSerializable

class TestConvert:

    @pytest.mark.parametrize("data, expected", [
        (np.array(5), 5),
        (np.array([5]), [5]),
        ({6}, [6])
    ])
    def test_to_serializable(self, data, expected):
        assert expected == to_serializable(
            data=data
        )
    
    @pytest.mark.parametrize("data", [
        pd.array(['a', 'b'], dtype=str),
        pd.Period('2000', freq="D")
    ])
    def test_to_serializable_exception(self, data):
        msg = 'Can only convert numpy and set type data'
        with pytest.raises(DataNotSerializable, match=msg):
            to_serializable(
                data=data
            )
        return 
