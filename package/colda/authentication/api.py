import sys, os

# print('-----authentication+_api', sys.path)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #__file__的是打印当前被执行的模块.py文件相对路径，注意是相对路径print(BASE_DIR)
# print(f'Base_Dir: {BASE_DIR}')

from authentication.authentication import Authentication

__all__ = [
    'Authentication'
]

def ceshi():
    return 5