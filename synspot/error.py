
def check_Algorithm_return_value(check_list, first_val, second_val):
    """
    :param first_val: String. The first val needs to check.
    :param second_val: String. The second val needs to check.

    :returns: Boolean

    :exception OSError: Placeholder.
    """
    if first_val:
        if check_list[0] != first_val:
            return False

    if second_val:
        if check_list[1] != second_val:
            return False

    return True
