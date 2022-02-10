
def check_Algorithm_return_value(check_list, first_val, second_val):
    """
    Parameters:
     first_val - String. The first val needs to check.
     second_val - String. The second val needs to check.

    Returns:
     Boolean

    Raises:
     KeyError - raises an exception
    """
    if first_val:
        if check_list[0] != first_val:
            return False

    if second_val:
        if check_list[1] != second_val:
            return False

    return True
