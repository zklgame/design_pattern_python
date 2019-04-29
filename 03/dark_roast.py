from beverage import Beverage


class DarkRoast(Beverage):

    def __init__(self):
        super().__init__('Dark Roast Coffee')

    def cost(self):
        return 0.99
