# Install whl file first in your command:
# Ex: pip install /Users/qile/Documents/synspot_all/Package/dist/colda-0.0.0-py3-none-any.whl
# pip install ../../dist/colda-0.0.0-py3-none-any.whl

# import os
# cwd = os.getcwd()
# print("Current working directory: {0}".format(cwd))
# os.chdir('../../../')
# cwd = os.getcwd()


import sys
sys.path.append('../../../')

from colda import Colda, load

colda_instance = Colda()
test_function_res = colda_instance.test_function()


print(test_function_res)
print(colda_instance.test_network())

username = "xie1"
password = "Xie1@123"

colda_instance.login(username, password)

# exit()

# get train id all

print(colda_instance.get_all_train_id())

colda_instance.clean_db()


train_file_path = "lstm_dataset/0/small_train.csv"


import pandas as pd
test= pd.read_csv(train_file_path)


print(test.shape)
colda_instance.fit(
    max_round=2, 
    assistors=['xie2'], 
    train_file_path=train_file_path,
    train_id_column='1', 
    train_data_column='2-58', 
    train_target_column='59', 
    task_mode='regression', 
    model_name='lstm', 
    metric_name='MAD_RMSE_R2', 
    task_name='Uber_lyft_linear_train', 
    task_description='Uber_lyft_train'
)
print(colda_instance.get_all_train_id())

colda_instance.save()
colda_instance = load()

test_file_path = 'lstm_dataset/0/small_test.csv'
colda_instance.predict(
    test_file_path=test_file_path, 
    test_id_column='1', 
    test_data_column='2-58', 
    test_target_column='59',  
    test_name='lstm_test', 
    test_description='lstm_test'
)