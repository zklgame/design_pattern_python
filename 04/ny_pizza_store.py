from pizza_store import PizzaStore
from cheese_pizza import CheesePizza
from clam_pizza import ClamPizza
from pepperoni_pizza import PepperoniPizza
from veggie_pizza import VeggiePizza


class NYPizzaStore(PizzaStore):

    def __init__(self, factory):
        super().__init__(factory)

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza(self.factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif pizza_type == 'clam':
            pizza = ClamPizza(self.factory)
            pizza.set_name('New York Style Clam Pizza')
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.factory)
            pizza.set_name('New York Style Pepperoni Pizza')
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(self.factory)
            pizza.set_name('New York Style Veggie Pizza')

        return pizza
