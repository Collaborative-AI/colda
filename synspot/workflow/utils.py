import json
import numpy as np

from synspot.algorithm import log

class check_sponsor_class:
    sponsor = 1
    assistor = 0

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


def log_helper(msg, root, user_id, task_id):
    """
    Append the msg to log file

    :param msg: List[String]. The name of current return_val

    :returns: None

    :exception OSError: Placeholder.
    """
    for item in msg:
        log(item, root, user_id, task_id)

def check_json_format(content):
    """
    start task with all assistors

    :param file_address: Integer. Maximum training round
    :param file_content: List. The List of assistors' usernames

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """
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
    except:
        return False
    return True

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

def load_json_data(json_data, json_data_name, testing_key_value_pair=None):
    """
    start task with all assistors

    :param file_address: Integer. Maximum training round
    :param file_content: List. The List of assistors' usernames

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """
    # assert json_data is not None
    print('load_json_data', json_data_name)

    if hasattr(json_data, 'text'):
        json_data = json_data.text

    if check_json_format(json_data):
        json_data = json.loads(json_data)
    if isinstance(json_data, dict):
        print('json_data', json_data.keys())
    # assert json_data is not None

    if testing_key_value_pair:
        for item in testing_key_value_pair:
            key, value = item[0], item[1]
            print('key_value', key, value)
            # assert key in json_data.keys()
            if value:
                # assert json_data[key] == value
                pass
    return json_data

def load_file(file_address):
    """
    start task with all assistors

    :param file_address: Integer. Maximum training round
    :param file_content: List. The List of assistors' usernames

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """
    file_data = np.genfromtxt(file_address, delimiter=',', dtype=np.str_)
    # assert file_data is not None

    if type(file_data) is np.ndarray:
        file_data = list(file_data)

    return file_data


def save_file(file_address, file_content):

    """
    start task with all assistors

    :param file_address: Integer. Maximum training round
    :param file_content: List. The List of assistors' usernames

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """

    try:
        if check_json_format(file_content):
            print('gggg')
            file_content = load_json_data(file_content, 'file_content')

        print('55555')
        # assert isinstance(file_content, list) == True
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

    :param name: String. The name of current return_val
    :param return_val: String. Contains the status code, name, paths that are returned by Algorithm
    :param first_val: String. The first value needs to be checked
    :param second_val: String. The second value needs to be checked

    :returns: return_val that has been split

    :exception OSError: Placeholder.
    """

    return_val = return_val.split("?")
    print(name, return_val)
    # check if return_val obeys the correct return value
    indicator = check_Algorithm_return_value(return_val, first_val, second_val)

    return indicator, return_val

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