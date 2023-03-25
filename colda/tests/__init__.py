import os
import sys

CUR_FILE_PATH = os.path.abspath(__file__)
UPPER_LEVEL_PATH = os.path.dirname(CUR_FILE_PATH)
UPPER_UPPER_LEVEL_PATH = os.path.dirname(UPPER_LEVEL_PATH)
# TOP_LEVEL_PATH = os.path.dirname(UPPER_UPPER_LEVEL_PATH)
print(f'Colda Test Upper Level Path Init: {UPPER_LEVEL_PATH}')
print(f'Colda Test Upper Upper Level Path Init: {UPPER_UPPER_LEVEL_PATH}')
# sys.path.append(UPPER_LEVEL_PATH)
sys.path.append(UPPER_UPPER_LEVEL_PATH)

# if '/Users/qile/Documents/synspot_all' in sys.path:
#     print('###########')
#     sys.path.remove('/Users/qile/Documents/synspot_all')


# if '/Users/qile/Documents/synspot_all/colda/colda/tests' in sys.path:
#     print('22###########')
#     sys.path.remove('/Users/qile/Documents/synspot_all/colda/colda/tests')

print(f'------Colda Test Total Path Init: {sys.path}')
# sys.path.pop(0)
# print(f'222222-Colda Test Total Path: {sys.path}')

# import colda
from __init__ import Colda

colda_instance = Colda()
print(colda_instance.test_function())


    