# This is a use case for BostonHousing dataset

# 1. Install whl file first in your command:
#   Example: pip install /local_path/colda-0.0.0-py3-none-any.whl

# 2. Please follow the instructions in Assistor_User_Guide_bos.py first

# 3. Replace the 'local_path' in train_file_path and test_file_path with your own path
# local_path = '/colda/package'
local_path = 'Users/kewang/colda/package'
# 4. Open a new terminal and run the following command:
#   python Sponsor_User_Guide_bos.py
import colda
from colda import Colda, load

colda_instance = Colda()
test_function_res = colda_instance.test_function()
print(test_function_res)
print(colda_instance.test_network())
print("boston")

username = "xie1"
password = "Xie1@123"

colda_instance.login(username, password)
colda_instance.clean_db()

train_file_path = f"/{local_path}/examples/BostonHousing/data/BostonHousing_2_123_1.0/0/train/dataset.csv"
colda_instance.fit(
    max_round=2, 
    assistors=['xie2'], 
    train_file_path=train_file_path,
    train_id_column='1', 
    train_data_column='2-8', 
    train_target_column='9', 
    task_mode='regression', 
    model_name='linear', 
    metric_name='MAD_RMSE_R2', 
    task_name='demo_training', 
    task_description='colda Demo Training'
)

colda_instance.save()
colda_instance = load()

test_file_path = f"/{local_path}/examples/BostonHousing/data/BostonHousing_2_123_1.0/0/test/dataset.csv"
colda_instance.predict(
    test_file_path=test_file_path, 
    test_id_column='1', 
    test_data_column='2-8', 
    test_target_column='9',  
    test_name='demo_testing', 
    test_description='colda Demo Testing'
)
