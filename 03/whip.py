from condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return 0.1 + self.beverage.cost()
