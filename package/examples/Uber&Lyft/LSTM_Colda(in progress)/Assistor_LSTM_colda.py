# Install whl file first in your command:
# Ex: pip install /Users/qile/Documents/synspot_all/Package/dist/colda-0.0.0-py3-none-any.whl
import sys
sys.path.append('../../../')


from colda import Colda

colda_instance = Colda()
test_function_res = colda_instance.test_function()
print(test_function_res)
print(colda_instance.test_network())

username = "xie2"
password = "Xie2@123"

colda_instance.login(username, password)



default_file_path = 'lstm_dataset/1/small_all.csv'
colda_instance.set_default_info(
    default_mode='auto', 
    default_task_mode='regression', 
    default_model_name='lstm', 
    default_file_path=default_file_path,
    default_id_column='1', 
    default_data_column='2-58'
)
colda_instance.start_cooperation()

