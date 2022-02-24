import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# print('zzz', basedir)
import sys
# sys.path.append(basedir)

# from make_dataset import make_data
from synspot.algorithm.make_train_local import make_train_local
from synspot.algorithm.make_test_local import make_test_local
from synspot.algorithm.make_hash import make_hash
from synspot.algorithm.save_match_id import save_match_id
from synspot.algorithm.make_match_idx import make_match_idx
from synspot.algorithm.make_residual import make_residual
from synspot.algorithm.save_residual import save_residual
from synspot.algorithm.make_train import make_train
from synspot.algorithm.save_output import save_output
from synspot.algorithm.make_result import make_result
from synspot.algorithm.make_test import make_test
from synspot.algorithm.make_eval import make_eval
from synspot.algorithm.utils import makedir_exist_ok, save, load, log, parse_idx
