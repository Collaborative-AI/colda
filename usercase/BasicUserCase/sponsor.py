import colda




username = "testKaiwangke"
email = "wangkedaily@gmail.com"
password = "1testWangke!"
print(colda.test_network())


test_function_res = colda.test_function()
print(test_function_res)



print("ABOVE TESTS=========================================")
colda.login(username, password)


train_file_path = "/home/ke/Package-main/package_Introduction/synspot_data/data/BostonHousing/BostonHousing_2_123_1.0/0/train/dataset.csv"


# colda.end_cooperation()

colda.start_cooperation()
colda.call_for_train(
    max_round=2, 
    assistors=['testKaiwangkeass'], 
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


# print(colda.get_all_algo_logs())
# train_id = input("paste the training ID into: ")
# test_file_path = "/home/ke/Package-main/package_Introduction/synspot_data/data/BostonHousing/BostonHousing_2_123_1.0/0/test/dataset.csv"
# colda.call_for_test(
#     train_id=train_id, 
#     test_file_path=test_file_path, 
#     test_id_column='1', 
#     test_data_column='2-8', 
#     test_target_column='9',  
#     test_name='demo_testing', 
#     test_description='colda Demo Testing'
# )
# print(colda.get_all_algo_logs())

# colda.end_cooperation()
    # colda.end_cooperation()