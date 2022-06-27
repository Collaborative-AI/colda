from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, final, overload

# class A(ABC):
#     @abstractmethod
#     def ceshi(self):
#         pass

# class B(A):
#     def __ceshi(self):
#         print('gan')

# b = B()
# b.__ceshi()

# class PizzaStore(object):  # 客户端程序抽象出父类
#     def order_pizza(self, pizza_type):
#         # ------------------------------------
#         print('pizza_type', pizza_type)
#         self.pizza = self.create_pizza(pizza_type)
#         # -------------------------------------

#         # self.pizza.prepare()
#         # self.pizza.bake()
#         # self.pizza.cut()
#         # self.pizza.box()
#         return self.pizza

#     def create_pizza(self, pizza_type):  #抽象的工厂方法
#         return pizza_type.create_pizza()
#         # pass


# class BeijingPizzaStore(PizzaStore):  # 客户端程序的子类
#     def create_pizza(self, pizza_type):  # 具体的工厂方法
#         pizzas = dict(cheese=5, vegetable=6, seafood=7)  # 不同的子类可能使用不同的产品
#         return pizzas[pizza_type]()

# class ShanghaiPizzaStore(PizzaStore):
#     def create_pizza(self, pizza_type):
#         pizzas = dict(cheese=1, vegetable=2, seafood=3)
#         return pizzas[pizza_type]()

# a = PizzaStore()
# res = a.order_pizza(BeijingPizzaStore)
# print(res)

# def some_function(number:int,name:str) -> None:
#     print("%s entered %s"%(name,number))

# some_function('1', 1)



# import string
# from functools import singledispatch

# @singledispatch
# def add(a,b):
#     raise NotImplementedError("Unsupport type")

# @add.register(int)
# def _(a:int,b:int) -> int:
#     print("Fist argument is of type ",type(a))
#     print (a+b)
#     return a+b

# @add.register(str)
# def _(a:string,b:string) -> string:
#     print("Fist argument is of type ",type(a))
#     print (a+b)
#     return a+b

# @add.register(list)
# def _(a:list,b:list) -> list:
#     print("Fist argument is of type ",type(a))
#     print (a+b)
#     return a+b

# res = add(5,6)
# print(f'res: {res}')

# from typing import cast

# a = 5
# b = cast(str, a)
# c = cast(float, a)

# print(f'b: {b}, {type(b)}')
# print(f'c: {c}, {type(c)}')


# class DuplicateLabelError(ValueError):
#     """
#     Error raised when an operation would introduce duplicate labels.

#     .. versionadded:: 1.2.0

#     Examples
#     --------
#     >>> s = pd.Series([0, 1, 2], index=['a', 'b', 'c']).set_flags(
#     ...     allows_duplicate_labels=False
#     ... )
#     >>> s.reindex(['a', 'a', 'b'])
#     Traceback (most recent call last):
#        ...
#     DuplicateLabelError: Index has duplicates.
#           positions
#     label
#     a        [0, 1]
#     """

# raise DuplicateLabelError('woshishabi')


# @overload
# def area(a: str):
#     print(f'wowowo')

# # @overload
# # def area(a: int):
# #     print(f'nonono')

# @final
# def area(a):
#     print('final')
#     pass


# area(5)
# area('6')


# @overload
# def area(a: str):
#     print(f'wowowo')

# @area.add
# def area(a: int, b: int):
#     print(f'nonono')

# # @final
# # def area(a):
# #     print('final')
# #     pass


# area(5,6)


# class A:
#     a = 5

#     @classmethod
#     def modify(cls):
#         a = 6

# class B(A):

#     @classmethod
#     def ceshi(cls):
#         print(f'a: {B.a}')

# B.ceshi()
# A.modify()
# B.ceshi()


# def ceshi(a: int | None = None):
#     print('gggg')

# class Base:
#     def fuji(self):
#         print('fuji')

# class AbstractDatabase(ABC):

#     @abstractmethod
#     def ceshi(self, a: int):
#         pass

# class concrete(AbstractDatabase):

#     @overload
#     def ceshi(self, a: float):
#         print('sssss')

#     def ceshi(self, a: int):
#         print(f'lihaine: {a}')

# a = concrete()
# a.ceshi(0.5)
# a = concrete()
# a.ceshi()
# a.fuji()
import collections
import random
# class lihai:
#     lihai1 = 7

# class Database:
#     __Database_instance = None

#     # def __init__(self):
#     #     self.__temp_database = collections.defaultdict(dict)
#     #     self.ceshi_num = 0

#     @classmethod
#     def get_Database_instance(cls):
#         if cls.__Database_instance == None:
#             cls.__Database_instance = Database()

#             # cls.__Database_instance.__temp_database['5'] = random.random()
#         return cls.__Database_instance

#     @classmethod
#     def get_data(cls):
#         return cls.__Database_instance
    
#     # def change_ceshi_num(self):
#     #     self.ceshi_num = 5

# instance_1 = Database.get_Database_instance()
# print(hex(id(instance_1)))
# res = hex(id(Database.get_Database_instance()))
# print(f'res, {res}')

# instance_2 = Database.get_Database_instance()
# instance_2.change_ceshi_num()

# res = instance_1.get_data()
# print(f'res, {res}')
# a = Database()
# res = a.get_data()
# res2 = a.__Database_instance
# print(f'res, {res}, {res2}')

# instance = Database.get_Database_instance()
# res = instance.get_data()
# print(f'res, {res}')

# class CECSCESCEE:
#     def ceshi(self):
#         print(self.__class__.__name__, type(self.__class__.__name__))

# a = CECSCESCEE()
# a.ceshi()

# a = 5

# print(f'sss: {a}')
# print(f"sss: {a}")

# from typing import (
#     Union,
#     Any,
# )

# JSONType = Union(
#     dict[str, str],
#     list[dict],
#     list[Any]
# )
  

# def a(cc: list[str]):
#     print(cc)

# a(['1', 2])


# a = {'a':{'aa':5}, 'b':{'bb':6}}

# for key,val in a.items():
#     print(key, val)
#     print(type(key), type(val))


# import numpy as np

# a = np.array(1)
# print(a, type(a))

# def ceshi(a: np.ndarray[int]):
#     print('fsdfsd', a)

# ceshi(a)

import collections

from typing import (
    Any,
    Hashable,
    TypeVar,
    Literal,
    Union
)

# DictKey = TypeVar('DictKey', bound=Hashable)
# DictValue = TypeVar("DictValue", bound=Any)
# Store_Type = Literal['append', 'one_access']


# class DictHelper:

#     @classmethod
#     def is_key_in_dict(
#         cls,
#         key: DictKey, 
#         container: dict
#     ) -> bool:

#         if key in container:
#             return True
#         return False

#     @classmethod
#     def generate_unique_dict_key(
#         cls, user_id: str, task_id: str
#     ) -> tuple[str, str]:

#         return (user_id, task_id)

#     @classmethod
#     def append_type(
#         cls,
#         key: DictKey, 
#         value: Union(dict[DictKey, DictValue], list[DictValue]),
#         container: dict[DictKey, DictValue],
#     ) -> None:

#         if key not in container:
#             container[key] = value
#         else:
#             if isinstance(container[key], dict) and isinstance(value, dict):
#                 for sub_key, sub_value in value.items():
#                     container[key][sub_key] = sub_value
#             elif isinstance(container[key], list) and isinstance(value, list):
#                 container[key].append(value)
#         return

#     @classmethod
#     def one_access_type(
#         cls,
#         key: DictKey, 
#         value: DictValue,
#         container: dict[DictKey, DictValue]
#     ) -> None:
#         if key not in container:
#             container[key] = value
#         else:
#             print('error')
#         return None

#     @classmethod
#     def store_value(
#         cls,
#         key: DictKey, 
#         value: DictValue,
#         container: dict[DictKey, DictValue],
#         store_type: Store_Type = 'one_access'
#     ) -> None:

#         if store_type == 'one_access':
#             cls.one_access_type(key, value, container)
#         elif store_type == 'append':
#             cls.append_type(key, value, container)
#         else:
#             print('store type wrong')
#         return

#     @classmethod
#     def get_value(
#         cls,
#         key: DictKey, 
#         container: dict[DictKey, DictValue]
#     ) -> DictValue:
        
#         if key not in container:
#             '''
#             warning
#             '''
#             pass
#         return container[key]
# # a = ['5', '6']

# # print('\n'.join(a))

# # from colda.utils.dict_helper import DictHelper

# # a = collections.defaultdict(dict)

# # value = {
# #     6:8
# # }

# # DictHelper.store_value(
# #     key=5,
# #     value=value,
# #     container=a
# # )

# # print(f'sss: {a}')

# # value = {
# #     9:10
# # }

# # # DictHelper.store_value(
# # #     key=5,
# # #     value=value,
# # #     container=a,
# # #     store_type='append'
# # # )

# # # print(f'sss: {a}')


# # b = {}
# # b[5] = 6

# # def ceshi(a):
# #     print(a)

# # class A:
# #     def wudi(self, a):
# #         print(f'aaaa: {a}')

# # class B(A):
# #     def __init__(self):
# #         self.__a = 666
    
# #     def diaoyong(self):
# #         ceshi(self.__a)

# # b = B()
# # b.diaoyong()

# # def a(a,b,c):
# #     print(a,b,c)

# # a(5, None, 6)


# # from __future__ import annotations

# import json
# import requests

# # from .utils import ParseJson

# from typing import (
#     Union,
#     Any,
# )

# # JSONType = Union(
# #     dict[str, Any],
# #     list[dict],
# #     list[Any]
# # )
    


# # a = {}
# # print(a['5'])

# def ceshi(**kwargs):
#     ceshi2(
#         helper=helper,
#         user
#     )


# def ceshi2(
#     helper: str,
#     user: str,
# ):
#     print(f'fasdf:{user, helper}')

# ceshi(
#     user='shima',
#     helper='wudi',
# )

# def a(
#     a,
#     b = None,
#     c = 200,
# ):
#     print(a,b,c)

# a(5, 10)

# class ceshi:
#     def __init__(self):
#         self.__database_operator = None

#     @property
#     def database(self):
#         """
#         The Context maintains a reference to one of the Strategy objects. The
#         Context does not know the concrete class of a strategy. It should work
#         with all strategies via the Strategy interface.
#         """

#         return self.__database_operator

#     @database.setter
#     def database(self, database) -> None:
#         """
#         Usually, the Context allows replacing a Strategy object at runtime.
#         """

#         self.__database_operator = database
#         print(self.__database_operator)
    
#     def fuyu(self, x):
#         self.database

# a = ceshi()
# a.database = 'wudi'
# a.fuyu('shima')


# def ceshi(**kwargs):
#     ceshi2(
#         **kwargs
#     )


# def ceshi2(
#     helper: str,
#     user: str,
#     wudi: str,
# ):
#     print(f'fasdf:{user, helper}')

# ceshi(
#     user='shima',
# )


# class parent:
#     __ceshi = 5

#     @classmethod
#     def fulei(cls):
#         print('yyy')

# class child(parent):

#     @classmethod
#     def dayin(cls):
#         # super().__init__()
#         # print(parent.__ceshi)
#         cls.fulei()
import json
import copy
import numpy as np
def check(data):
    try:
        json.dumps(data)
    except:
        return False
    else:
        return True

# child.dayin()

class ParseJson:

    @classmethod
    def is_json(
        cls,
        data: Any
    ) -> bool:

        """
        start task with all assistors

        :param file_address: Integer. Maximum training round
        :param file_content: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        if isinstance(data, list):
            return False
        elif isinstance(data, int):
            return False
        elif isinstance(data, tuple):
            return False    
        elif isinstance(data, dict):
            return False

        try:
            json.loads(data)
        except:
            return False

        return True

    @classmethod
    def load_json_recursion(
        cls,
        data: Any,
    ) -> dict[Any]:

        if data is None:
            return None

        if cls.is_json(data):
            data = json.loads(data)
        
        if not isinstance(data, dict):
            return data

        processed_data = {}
        for key, value in data.items():
            processed_data[key] = cls.load_json_recursion(value)    

        return processed_data
    
    @classmethod
    def is_serializable(
        cls,
        data: Any
    ) -> bool:

        # if isinstance(data, (np.ndarray, np.generic)):
        #     return False
        # return True

        try:
            json.dumps(data)
        except:
            return False
        else:
            return True

    @classmethod
    def make_data_serializable(
        cls,
        data: Any
    ) -> Any:

        if data is None:
            return None

        if cls.is_serializable(data):
            return copy.deepcopy(data)
        
        if isinstance(data, (np.ndarray, np.generic)):
            return copy.deepcopy(data.tolist())

        # processed_data = None
        if isinstance(data, dict):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = cls.make_data_serializable(value)    
        elif isinstance(data, list):
            processed_data = []
            for i in range(len(data)):
                processed_data.append(cls.make_data_serializable(data[i])) 

        return processed_data

# from colda.utils import ParseJson

# a = np.array(5)
# b = np.array(6)
# c = [a,b]
# res = check(c)
# print(res)
# c = ParseJson.make_data_serializable(c)
# print('ccc', c)
# res = check(c)
# print(res)
# def is_json(myjson):
#   try:
#     json.loads(myjson)
#   except ValueError as e:
#     return False
#   return True

# aa = json.dumps(
#     {
#         '8': {
#             5: 7
#         }
#     },
# )
# a = {
#     '5': aa,
#     'wudi': [
#         1,2,3
#     ]
# }

# b = json.dumps(a)
# print(b, type(b), is_json(b))
# # c = b.json()
# c = json.loads(b)
# print(c, type(c))
# d = c['5']
# print(d, type(d), is_json(d))


# print(a,type(a))
# b = json.dumps(a)
# c = json.dumps(b)
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))

# def a(*args):
#     # print(args, type(args))
#     # print(5 in args)
#     return 5,6,7,8
# b = a()

# print(b)

class DictValueNotFound(ValueError):
    """
    Error raised when the value cannot found in corresponding dict key
    """
    pass

# print(DictValueNotFound == a.all())
# a = np.array([1,2,3])
# print('aaaa', a)
# print(len(a), len(DictValueNotFound))
# print( (DictValueNotFound == a).all() )
# print(type(DictValueNotFound))
# print(type(a))
# print(type([1,2,3]))
# print(type(5))
# print(DictValueNotFound == a.tolist())
# print(type(a) == DictValueNotFound)
# print(DictValueNotFound == [1,2,3])
# def is_numpy(obj) -> bool:
#     if isinstance(obj, (np.ndarray, np.generic)):
#         return True
#     return False

# def if_response_valid(
#     *args
# ) -> bool:
#     print('if_response_valid1', args)

#     args = [val.tolist() if is_numpy(val) else val for val in args]
#     print('if_response_valid2', args)
#     if DictValueNotFound in args:
#         return False
#     return True

# res = if_response_valid(a)

# print(res)


# a = [[5,6,7,8]]

# b = [a, [5,6]]

# print(DictValueNotFound == b)

# def ceshi(**kwargs):
    # for key, val in kwargs.items():
    #     print(key, val)
    #     if val == 'lihai':
    #         kwargs[key] = 'lihaima'

    # for key, val in kwargs.items():
    #     print(key, val)
        # if val == 'lihai':
        #     val = 'lihaima'
#     return (
#         wudi='wudi',
#         lihai='lihai',
#     )

# ceshi(
#     wudi='wudi',
#     lihai='lihai'
# )

# def ceshi1(**kwargs):
#     print(kwargs)
#     return kwargs

# def ceshi2(**kwargs):
#     print(kwargs)

# res = ceshi1(
#     wudi='wudi',
#     lihai='lihai'
# )
# print('res', res)
# ceshi2(**res)

# def ceshi():
#     return (5, 6, 7)

# res = ceshi()
# print(res, type(res))
# for val in res:
#     print(val)

# def ceshi2(*args):
#     print(args)

# ceshi2(*res)

# a = [1,2,3]

# def ceshi(c, *args):
#     print(c)
#     print(args, args==())

# ceshi(a)


def is_serializable(
    data: Any
) -> bool:

    # if isinstance(data, (np.ndarray, np.generic)):
    #     return False
    # return True

    try:
        json.dumps(data)
    except:
        return False
    else:
        return True

# a = [4,5,[6,6,[7,8,9]]]
# import numpy as np

# b = np.array(a, dtype="object")
# print(b, type(b), is_serializable(b))
# for item in b:
#     print(item, type(item), is_serializable(item))

# b1 = b.tolist()
# print('b1', b1, type(b1), is_serializable(b1))

# c = np.array([np.array(_) for _ in a])
# print(c, type(c), is_serializable(c))
# for item in c:
#     print(item, type(item), is_serializable(item))
# b = np.array()
# a = []
# print(a == None, not a, not b)
# a = np.array(5.6, dtype='float')
# b = np.array(5.6, dtype=float)
# c = 5
# print(a,b)
# print(type(c))
# d = np.array(5, dtype=type(c))

# a = np.ones([2,2,3], dtype = int)
# print(a)
# res1 = is_serializable(a)

# a = a.tolist()

# res2 = is_serializable(a)

# print(res1, res2)
# from pandas.api.types import is_dict_like as pandas_is_dict_like
# from pandas.api.types import is_integer as pandas_is_integer
# from pandas.api.types import is_list_like as pandas_is_list_like
# from pandas.api.types import is_float as pandas_is_float
# def is_numpy(obj) -> bool:
#     return isinstance(obj, (np.ndarray, np.generic))

# def is_dict_like(obj) -> bool:
#     return pandas_is_dict_like(obj)

# def is_list_like(obj) -> bool:
#     return pandas_is_list_like(obj)

# def is_tuple(obj) -> bool:
#     return isinstance(obj, tuple)

# def is_list(obj) -> bool:
#     return isinstance(obj, list)

# def is_integer(obj) -> bool:
#     return pandas_is_integer(obj)

# def is_float(obj) -> bool:
#     return pandas_is_float(obj)



# def process_input_recursion(
#     data: Any,
# ):

    '''
    Change list to np.array
    '''
    
    # if data is None or not data:
    #     return None
    
    # # processed_data = None
    # if is_dict_like(data):
    #     processed_data = {}
    #     for key, value in data.items():
    #         processed_data[key] = process_input_recursion(value)    
    # elif is_list(data):
    #     processed_data = []
    #     for i in range(len(data)):
    #         processed_data.append(process_input_recursion(data[i]))
    #     print('processed_data', processed_data) 
    #     if not is_array()
    #     processed_data = np.array(processed_data, dtype=type(processed_data[0]))
    #     print(f'new_type: {type(processed_data[0])}')
    # else:
    #     return data

    # return processed_data


# a = [[-4.44], [-5.66]]
# b = process_input_recursion(a)

# print(b, type(b))


# a = [6, 5]
# a = np.array(a)
# # a = np.array(a, type(a[0]))
# b = {5: a}
# print(is_serializable(b))

# b[5] = b[5].tolist()
# print(is_serializable(b))
# d = 5

# print(type(d) == int)

# class wudi:
#     stop = False

#     @classmethod
#     def ceshi(cls):
#         if cls.stop == False:
#             print('wudi')
#             cls.stop = True

# wudi.ceshi()
# wudi.ceshi()



# # Code to execute in an independent thread
# def countdown(n, started_evt):
#     print('countdown starting')
#     started_evt.set()
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(5)

# # # Create the event object that will be used to signal startup
# # started_evt = Event()

# # # Launch the thread and pass the startup event
# # print('Launching countdown')
# # t = Thread(target=countdown, args=(10,started_evt))
# # t.start()

# # # Wait for the thread to start
# # started_evt.wait()
# # print('countdown is running')

# import threading
# from threading import Thread, Event
# import time

# class Ceshi:
#     __temp_instance = None

#     def __init__(self):
#         self.stop_indicator = False
#         # self.timer = None
#         self.shortpolling = {'running': False}

#     @classmethod
#     def get_instance(cls):
#         if cls.__temp_instance == None:
#             cls.__temp_instance = Ceshi()

#         return cls.__temp_instance

#     def start_helper(self, x):
#         if self.shortpolling['running'] == False:
#             self.shortpolling['running'] = True
#             self.__start(x)

#         return 

#     def __start(self, x):
#         # if self.stop_indicator == False and self.timer == None:
#         # if self.shortpolling['running'] == None:
#         print('zzzz', x)
#         if self.shortpolling['running'] == True:
#             self.timer = threading.Timer(5, self.__start, args=([x+1]))
#             # self.shortpolling['running'] = True
#             self.timer.start()

#         return
    
#     def end(self):
#         self.shortpolling['running'] = False
#         # self.timer = None
#         return


# _a = Ceshi()

# def kaishi():
#     # a = Ceshi()
#     print('wudi', id(_a))
#     _a.start_helper(0)
#     _a.start_helper(-10000)

# def jieshu():
#     # a = Ceshi()
#     print('wudi', id(_a))
#     _a.end()

# import sys
# if __name__ == '__main__':
#     globals()[sys.argv[1]]()
#     time.sleep(20)
#     globals()[sys.argv[2]]()
# python -c 'import foo; print foo.hello()'

# import numpy as np

# a = [[2,3],[1,2]]

# # dict[str, Any]

# b = np.array(a)

# c = {5: 6, 7: 8}
# d = np.array(c)


# # print(b, type(b))
# # for item in b:
# #     print(item, type(item))

# print(d, type(d), d[5])
# Role = Literal[
#     'sponsor',
#     'assistor',
# ]

# def a(role: Role):
#     print(f'role: {role}')

# a(5)
# from typeguard import typechecked

# #@typechecked
# def a() -> tuple[int]:
#     return (5, )

# print(type(a()))

# class ceshi:
#     __shuxing = 5

#     # def __init__(cls, shuxing):
#     #     cls.__shuxing = shuxing
#     #     cls.get()

#     @property
#     def shuxing(cls):
#         print(cls.__shuxing)

#     @shuxing.setter
#     def shuxing(cls, shuxing):
#         cls.__shuxing = shuxing
#         return cls.__shuxing

# ceshi.shuxing = 7
# print(ceshi.shuxing)

# print(ceshi.shuxing)

# a = list(5)
# print(a)


# key = [(5, 4)]
# key.append(6)
# print(key)

# a = {}
# a[key] = 6
# print(a)

def is_json_object(
    data: Any
) -> bool:
    '''
    Check if data is json object.

    Parameters
    ----------
    data : Any

    Returns
    -------
    bool
    '''
    try:
        json.loads(data)
    except ValueError as err:
        return False
    else:
        return True

# print(is_json('5'))

# a = json.dumps('5')
# print(a)
# print(type(a) == str)
# a = json.loads('5')
# b = json.loads('"5"')
# print(type(a))
# print(type(b))
# a = '{"5": "6"}'

# b = json.loads(a)
# print(b, type(b))
# c = json.loads(b['5'])
# print(c, type(c))

# def is_serializable(
#     data: Any
# ) -> bool:
#     '''
#     Check if data is serializable.

#     Parameters
#     ----------
#     data : Any

#     Returns
#     -------
#     bool
#     '''
#     try:
#         json.dumps(data)
#     except:
#         return False
#     else:
#         return True


# a = {'5': [4, 5, np.array(5)]}
# print(is_serializable(a))


import hashlib
input = 5
output = hashlib.sha256(str(input).encode('utf-8'))
output = output.hexdigest()
print(type(output))
