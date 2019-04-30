import abc


class PizzaStore(abc.ABC):

    def __init__(self, factory):
        self.factory = factory

    # this function acts like a factory method
    @abc.abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
