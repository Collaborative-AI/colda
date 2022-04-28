from synspot.personalinformation import PersonalInformation

from typing import Tuple

def get_user_id() -> str:
    PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
    user_id = PersonalInformation_instance.user_id
    # assert user_id is not None
    return user_id

def generate_database_key(user_id: str, task_id: str) -> Tuple[str, str]:
    return (user_id, task_id)