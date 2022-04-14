import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# print('zzz', basedir)
import sys
# sys.path.append(basedir)

# from make_dataset import make_data
from synspot.algorithm.algoAPI.make_train_local import make_train_local
from synspot.algorithm.algoAPI.make_test_local import make_test_local
from synspot.algorithm.algoAPI.make_hash import make_hash
from synspot.algorithm.algoAPI.save_match_id import save_match_id
from synspot.algorithm.algoAPI.make_match_idx import make_match_idx
from synspot.algorithm.algoAPI.make_residual import make_residual
from synspot.algorithm.algoAPI.save_residual import save_residual
from synspot.algorithm.algoAPI.make_train import make_train
from synspot.algorithm.algoAPI.save_output import save_output
from synspot.algorithm.algoAPI.make_result import make_result
from synspot.algorithm.algoAPI.make_test import make_test
from synspot.algorithm.algoAPI.make_eval import make_eval
from synspot.algorithm.algoAPI.utils import makedir_exist_ok, save, load, log, parse_idx



