from beverage import Beverage


class Espresso(Beverage):

    def __init__(self):
        super().__init__('Espresso')

    def cost(self):
        return 1.99
