from __future__ import annotations

from typing import final

from typeguard import typechecked


class BaseMetric:
    '''
    Base class for Metric
    '''
    @final
    def placeholder(self):
        pass