import json
import numpy as np

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

def check_json_format(content):
    if isinstance(content, list):
        return False
    elif isinstance(content, int):
        return False
    elif isinstance(content, tuple):
        return False    
    elif isinstance(content, dict):
        return False

    try:
        print('sss')
        json.loads(content)
        print('sss1')
    except ValueError:
        return False
    return True

def load_json_data(json_data, json_data_name, testing_key_value_pair=None):
    assert json_data is not None
    print('load_json_data', json_data_name)

    if hasattr(json_data, 'text'):
        json_data = json_data.text

    if check_json_format(json_data):
        json_data = json.loads(json_data)
    if isinstance(json_data, dict):
        print('json_data', json_data.keys())
    assert json_data is not None

    if testing_key_value_pair:
        for item in testing_key_value_pair:
            key, value = item[0], item[1]
            print('key_value', key, value)
            assert key in json_data.keys()
            if value:
                assert json_data[key] == value

    return json_data

def load_file(file_address):
    file_data = np.genfromtxt(file_address, delimiter=',', dtype=np.str_)
    assert file_data is not None

    if type(file_data) is np.ndarray:
        file_data = list(file_data)

    return file_data


def save_file(file_address, file_content):
    try:
        if check_json_format(file_content):
            print('gggg')
            file_content = load_json_data(file_content, 'file_content')

        print('55555')
        assert isinstance(file_content, list) == True
        np.savetxt(file_address, file_content, delimiter=",", fmt="%s")
    except:
        print('file_address', file_address, type(file_address))
        print('file_content', file_content, type(file_content))
        raise RuntimeError('Python save file wrong')
    return


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