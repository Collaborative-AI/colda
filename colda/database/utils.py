from __future__ import annotations

from colda.pi.api import PI

from typing import Tuple
from typeguard import typechecked


def get_user_id() -> str:
    '''
    Get current user_id

    Returns
    -------
    str
    '''
    PI_instance = PI.get_instance()
    user_id = PI_instance.user_id
    return user_id
