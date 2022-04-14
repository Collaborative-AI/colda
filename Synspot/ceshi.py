from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def ceshi(self):
#         pass

# class B(A):
#     def __ceshi(self):
#         print('gan')

# b = B()
# b.__ceshi()

class PizzaStore(object):  # 客户端程序抽象出父类
    def order_pizza(self, pizza_type):
        # ------------------------------------
        print('pizza_type', pizza_type)
        self.pizza = self.create_pizza(pizza_type)
        # -------------------------------------

        # self.pizza.prepare()
        # self.pizza.bake()
        # self.pizza.cut()
        # self.pizza.box()
        return self.pizza

    def create_pizza(self, pizza_type):  #抽象的工厂方法
        return pizza_type.create_pizza()
        # pass


class BeijingPizzaStore(PizzaStore):  # 客户端程序的子类
    def create_pizza(self, pizza_type):  # 具体的工厂方法
        pizzas = dict(cheese=5, vegetable=6, seafood=7)  # 不同的子类可能使用不同的产品
        return pizzas[pizza_type]()

class ShanghaiPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizzas = dict(cheese=1, vegetable=2, seafood=3)
        return pizzas[pizza_type]()

a = PizzaStore()
res = a.order_pizza(BeijingPizzaStore)
print(res)
