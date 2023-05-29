import colda


usernameass = "testKaiwangkeass"
emailass = "wan00802@umn.edu"
passwordass = "1testWangkeass!"


colda.login(usernameass, passwordass)
# colda.start_cooperation()


default_file_path = "/home/ke/Package-main/package_Introduction/synspot_data/data/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv"

colda.set_default_info(
    default_mode='auto', 
    default_task_mode='regression', 
    default_model_name='linear', 
    default_file_path=default_file_path,
    default_id_column='1', 
    default_data_column='2-14'
)

colda.start_cooperation()

print(colda.get_all_algo_logs())


# colda.end_cooperation()

# colda.end_cooperation()



