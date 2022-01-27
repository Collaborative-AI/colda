from .Error import check_Algorithm_return_value
from py_pkg.Algorithm import log

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
    Check if the return value returned by the Algorithm equals to the correct value, e.x. 
    return_val[0] == first_val ('200'), return_val[1] == second_val ('make_train')

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
        raise RuntimeError('pythonError')

    return return_val

def handle_base64_padding(base64_string):
    """
    If the length of the base64 string is not multiple of 3, add '=' or '==' behind

    Parameters:
        base64_string - String. part of token

    Returns:
        base64_string - String. Processed String

    Raises:
        KeyError - raises an exception
    """
    print('length', len(base64_string))
    num = len(base64_string)%4
    if num != 0:
        base64_string = base64_string + '=' * (4-num)
    print('length_after', len(base64_string))
    return base64_string