from __future__ import annotations

from synspot.personalinformation import PersonalInformation

from typing import Tuple

def get_user_id() -> str:
    PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
    user_id = PersonalInformation_instance.user_id
    # assert user_id is not None
    return user_id
