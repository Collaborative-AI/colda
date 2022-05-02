from __future__ import annotations

from typing import final

class BaseDatabaseStrategy:

    @final
    def placeholder(self, **kwargs):
        pass