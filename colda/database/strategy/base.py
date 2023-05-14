from __future__ import annotations

from typing import final

class BaseDatabaseStrategy:
    '''
    Base class for database strategy pattern
    '''

    @final
    def placeholder(self, **kwargs):
        pass