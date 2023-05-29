# This is a use case for BostonHousing dataset

# 1. Install whl file first in your command:
#   Example: pip install /local_path/colda-0.0.0-py3-none-any.whl

# 2. Replace the 'local_path' in default_file_path with your own path
local_path = 'Users/qile/Documents/colda/package'

# 3. Open a new terminal and run the following command:
#   python Assistor_User_Guide_bos.py

from colda import Colda

colda_instance = Colda()
test_function_res = colda_instance.test_function()
print(test_function_res)
print(colda_instance.test_network())
username = "xie2"
password = "Xie2@123"

colda_instance.login(username, password)

default_file_path = f"/{local_path}/use_case_data/BostonHousing/BostonHousing_2_123_1.0/1/all/dataset.csv"
colda_instance.set_default_info(
    default_mode='auto', 
    default_task_mode='regression', 
    default_model_name='linear', 
    default_file_path=default_file_path,
    default_id_column='1', 
    default_data_column='2-7'
)
colda_instance.start_cooperation()

