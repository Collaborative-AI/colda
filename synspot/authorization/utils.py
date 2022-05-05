




def handle_base64_padding(base64_string):
    """
    If the length of the base64 string is not multiple of 3, add '=' or '==' behind

    :param base64_string: String. part of token

    :returns: base64_string - String. Processed String

    :exception OSError: Placeholder.
    """
    print('length', len(base64_string))
    num = len(base64_string)%4
    if num != 0:
        base64_string = base64_string + '=' * (4-num)
    print('length_after', len(base64_string))
    return base64_string