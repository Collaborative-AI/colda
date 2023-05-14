import colda


username = "testKaiwangke"
email = "wangkedaily@gmail.com"
password = "1testWangke!"
print(colda.test_network())

colda.login(username, password)

print("Login=========================================")


test_function_res = colda.test_function()
print(test_function_res)



print("ABOVE TESTS=========================================")

print(colda.get_all_algo_logs())