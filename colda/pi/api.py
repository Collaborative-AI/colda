from colda.pi.pi import PI


__all__ = [
    'PI'
]

def get_user_id() -> str:
    '''
    Get user id

    Parameters
    ----------
    None

    Returns
    -------
    str
    '''
    return PI.get_instance().user_id

def get_default_mode() -> str:
    '''
    Get default mode of assistor

    Parameters
    ----------
    None

    Returns
    -------
    str
    '''
    return PI.get_instance().default_mode

def get_data_storage_root() -> str:
    '''
    Data storage root path is used to store
    the seralization of some instance.

    Parameters
    ----------
    None

    Returns
    -------
    str
    '''
    return PI.get_instance().data_storage_root