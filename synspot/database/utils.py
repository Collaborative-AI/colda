from __future__ import annotations

from synspot.pi import PI

from typing import Tuple

def get_user_id() -> str:
    PI_instance = PI.get_instance()
    user_id = PI_instance.user_id
    # assert user_id is not None
    return user_id
