import errno
import os

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
