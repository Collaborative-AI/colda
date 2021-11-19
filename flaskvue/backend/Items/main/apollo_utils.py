import errno
import os
import re

# make directory exist
def makedir_exist_ok(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    return    

def generate_msg(*args):
    res = []
    for item in args:
        if isinstance(item, list):
            for sub_item in item:
                sub_item = str(sub_item)
            res.append(" ".join(item))
        else:
            item = str(item)
            res.append(item)
    
    return " ".join(res)


def log(msg, self_id, task_id, test_id=None):
    
    root = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(root, 'log_file')

    self_id = str(self_id)
    task_id = str(task_id)
    test_id = str(test_id)

    if test_id is None:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'train'))
        log_path = os.path.join(root, self_id, 'task', task_id, 'train', 'log.txt')
    else:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'test', test_id))
        log_path = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'log.txt')
    with open(log_path, 'a') as f:
        f.write(msg + '\n')
    return

def validate_password(password):
    
    """
    Validate the password. Must meet all conditions:
        1. At least 8 characters
        2. At most 40 characters
        3. Must be restricted to:
            3.1 uppercase letters: A-Z
            3.2 lowercase letters: a-z
            3.3 numbers: 0-9
            3.4 any of the special characters: @#$%^&+=

    Parameters:
        password - String. 

    Returns:
        Bolean

    Raises:
        KeyError - raises an exception
    """
    if len(password) < 8 or len(password) > 40:
        return False, 'please create password between 8 chars and 40 chars'

    # 匹配数字的正则
    digit_regex = re.compile(r'\d')
    # 匹配大写字母的正则
    upper_regex = re.compile(r'[A-Z]')
    # 匹配小写字母的正则
    lower_regex = re.compile(r'[a-z]')
    # 匹配字符
    symbol_regex = re.compile(r'[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""+]')
    

    if len(digit_regex.findall(password)) < 1: # 判断是否包含至少一位数字
        return False, 'Need at least 1 number'
    # print("1", len(digit_regex.findall(password)))

    if len(upper_regex.findall(password)) < 1: # 判断是否包含大写字母
        return False, 'Need at least 1 uppercase letter'
    # print("2", len(upper_regex.findall(password)))

    if len(lower_regex.findall(password)) < 1: # 判断是否包含小写字母
        return False, 'Need at least 1 lowercase letter'
    # print("3", len(lower_regex.findall(password)))

    if len(symbol_regex.findall(password)) < 1: # 判断是否包含字符
        return False, 'Need at least 1 symbol'
    print("4", len(symbol_regex.findall(password)))

    # if not re.fullmatch(r'[A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+]', password):
    #     return False, 'please fit in A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+ range'

    return True, ''