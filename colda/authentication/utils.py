from __future__ import annotations
# from typeguard import typechecked


def handle_base64_padding(
    base64_string: str
) -> str:
    '''
    If the length of the base64 string is not multiple of 3, 
    add '=' or '==' behind to let the base64_string can be
    parsed

    Parameters
    ----------
    base64_string : str
        part of token

    Returns
    -------
    str
        Processed base64_string
    '''
    num = len(base64_string)%4
    if num != 0:
        base64_string = base64_string + '=' * (4-num)

    return base64_string


def del_instance(
    objectInstance: object
) -> None:
    '''
    Delete instance

    Parameters
    ----------
    objectInstance : object

    Returns
    -------
    None
    '''
    try:
        del objectInstance
    except Exception as e:
        print('Logout procedure wrong')
        raise e
    return