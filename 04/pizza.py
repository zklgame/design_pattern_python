import abc


class Pizza(abc.ABC):

    def __init__(self, factory):
        super().__init__()
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.cheese = ''
        self.pepperoni = ''
        self.clam = ''
        self.veggies = []
        self.factory = factory

    @abc.abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
