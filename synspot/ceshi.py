from abc import ABC, abstractmethod
from typing import final, overload

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
class lihai:
    lihai1 = 7

class Database:
    __Database_instance = None

    # def __init__(self):
    #     self.__temp_database = collections.defaultdict(dict)
    #     self.ceshi_num = 0

    @classmethod
    def get_Database_instance(cls):
        if cls.__Database_instance == None:
            cls.__Database_instance = Database()

            # cls.__Database_instance.__temp_database['5'] = random.random()
        return cls.__Database_instance

    @classmethod
    def get_data(cls):
        return cls.__Database_instance
    
    # def change_ceshi_num(self):
    #     self.ceshi_num = 5

instance_1 = Database.get_Database_instance()
print(hex(id(instance_1)))
res = hex(id(Database.get_Database_instance()))
print(f'res, {res}')

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