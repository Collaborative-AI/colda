# class a:
#     z = "a"
#
#     @classmethod
#     def set(cls, value):
#         cls.z = value
#
#     @classmethod
#     def get(cls):
#         return cls.z
#
#
# a.set(5)
# print(a.get())

print(bin(5))
import numpy as np
file_address = '/Users/qile/Documents/Apollo_Package/Package/py_pkg/ceshi.csv'
file_content = ['zzzz', "ed3f1d00884bcc9d8545d3ef0d4549cc84c2efe0cd7fe06949247ba14c21d7c4"]
np.savetxt(file_address, file_content, delimiter=",", fmt="%s")
# 3个class  (单例)
# 每个class用task_id或者test_id当key， dictofdict
