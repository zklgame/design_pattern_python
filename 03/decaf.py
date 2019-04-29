from beverage import Beverage


class Decaf(Beverage):

    def __init__(self):
        super().__init__('Decaf Coffee')

    def cost(self):
        return 1.05
