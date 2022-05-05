import json

from typing import Any


def check_status_code(response, status_code):
    """
    start task with all assistors

    :param file_address: Integer. Maximum training round
    :param file_content: List. The List of assistors' usernames

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """
    if response.status_code == status_code:
        return True

    return False