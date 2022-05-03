import errno
import os
import re
import uuid
import logging


from flask import current_app, g
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

from Items import mail, pyMongo
from Items.extensions import mail

def add_new_token_to_response(response):
    if g.current_user['new_token'] != None:
        response['new_token'] = g.current_user['new_token'].decode('utf-8')
    else:
        response['new_token'] = g.current_user['new_token']
    return response

def generate_password(password):
    password_hash = generate_password_hash(password)
    return password_hash

def check_password(user, password):
    return check_password_hash(user['password_hash'], password)

def obtain_user_id_from_token():
    user_id = g.current_user['user_id']
    return user_id

def obtain_unique_id():
    unique_id = str(uuid.uuid1())
    return unique_id

def verify_token_user_id_and_function_caller_id(token_user_id, function_caller_id):
    if token_user_id == function_caller_id:
        return True
    else:
        return False

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

# mail = Mail(app)
def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        # sender=app.config['MAIL_DEFAULT_SENDER']
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    # debug([
    # 	app.config['MAIL_DEFAULT_SENDER'],
    # 	app.config['MAIL_USERNAME'],
    # 	app.config['MAIL_PASSWORD']], 'email')
    
    a = mail.send(msg)
    return 

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

def get_log(self_id, task_id, test_id=None):

    """
    read log file and return content of log file.

    Parameters:
       self_id - id of current user
       task_id - task_id of task
       test_id - test_id of test

    Returns:
        data - List[String]. ['first log_interval\n', 'second\n', 'third']

    Raises:
        KeyError - raises an exception
    """
    
    root = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(root, 'log_file')

    self_id = str(self_id)
    task_id = str(task_id)
    if test_id:
        test_id = str(test_id)

    if test_id is None:
        log_path = os.path.join(root, self_id, 'task', task_id, 'train', 'current_task.log')
        f = open(log_path, "r")
        return f.readlines()
            
    else:
        log_path = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'current_test.log')
        f = open(log_path, "r")
        return f.readlines() 

def generate_logger(log_path):

    """
    generate an logger instance. If there is no handler in the logger instance, add handler.
    If ther is handler, skip

    Parameters:
       log_path - String. The file position of log file

    Returns:
        logger - Object

    Raises:
        KeyError - raises an exception
    """

    logger = logging.getLogger('Apollo_logger')

    if not logger.handlers:
        logger.setLevel(level=logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # output to file
        handler = logging.FileHandler(log_path)
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)

        # output to terminal
        # handler = logging.StreamHandler(sys.stdout)
        # handler.setFormatter(formatter)
        # logger.addHandler(handler)
    
    return logger


def log(msg, self_id, task_id, test_id=None):
    
    """
    Use python logging module to store the log information. The output level of the logging
    module is set to debug, which is the lowest level

    Parameters:
       self_id - id of current user
       task_id - task_id of task
       test_id - test_id of test

    Returns:
        None

    Raises:
        KeyError - raises an exception
    """
    
    root = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(root, 'log_file')
    
    self_id = str(self_id)
    task_id = str(task_id)
    if test_id:
        test_id = str(test_id)

    log_path = None
    if test_id is None:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'train'))
        log_path = os.path.join(root, self_id, 'task', task_id, 'train', 'current_task.log')
        
    else:
        makedir_exist_ok(os.path.join(root, self_id, 'task', task_id, 'test', test_id))
        log_path = os.path.join(root, self_id, 'task', task_id, 'test', test_id, 'current_test.log')

    file = open(log_path,'w')
    file.close()
    
    # print('log_path', msg, self_id, task_id)
    logger = generate_logger(log_path)
    logger.debug(msg)
    
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
    # symbol_regex = re.compile(r'[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""+]')
    

    if len(digit_regex.findall(password)) < 1: # 判断是否包含至少一位数字
        return False, 'Need at least 1 number'
    # print("1", len(digit_regex.findall(password)))

    if len(upper_regex.findall(password)) < 1: # 判断是否包含大写字母
        return False, 'Need at least 1 uppercase letter'
    # print("2", len(upper_regex.findall(password)))

    if len(lower_regex.findall(password)) < 1: # 判断是否包含小写字母
        return False, 'Need at least 1 lowercase letter'
    # print("3", len(lower_regex.findall(password)))

    # if len(symbol_regex.findall(password)) < 1: # 判断是否包含字符
    #     return False, 'Need at least 1 symbol'
    # print("4", len(symbol_regex.findall(password)))

    # if not re.fullmatch(r'[A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+]', password):
    #     return False, 'please fit in A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+ range'

    return True, ''

