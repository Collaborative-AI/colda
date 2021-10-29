from Error import check_Algorithm_return_value
from Algorithm import log

def log_helper(msg, root, user_id, task_id):
    """
    Append the msg to log file

    Parameters:
     msg - List[String]. The name of current return_val

    Returns:
     None

    Raises:
     KeyError - raises an exception
    """
    for item in msg:
        log(item, root, user_id, task_id)




def handle_Algorithm_return_value(name, return_val, first_val, second_val):
    """
    Check the return value returned by the Algorithm

    Parameters:
     name - String. The name of current return_val
     return_val - String. Contains the status code, name, paths that are returned by Algorithm
     first_val - String. The first value needs to be checked
     second_val - String. The second value needs to be checked

    Returns:
     return_val that has been split

    Raises:
     KeyError - raises an exception
    """
    return_val = return_val.split("?")
    print(name, return_val)
    # check if return_val obeys the correct return value
    if not check_Algorithm_return_value(return_val, first_val, second_val):
        raise RuntimeError('testError')

    return return_val