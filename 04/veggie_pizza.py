from pizza import Pizza


class VeggiePizza(Pizza):

    def __init__(self, factory):
        super().__init__(factory)

    def prepare(self):
        print('Preparing ' + self.name)
        self.dough = self.factory.create_dough()
        self.sauce = self.factory.create_sauce()
        self.cheese = self.factory.create_cheese()
        self.veggies = self.factory.create_veggies()
