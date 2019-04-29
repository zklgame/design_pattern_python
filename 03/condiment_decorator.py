import abc
from beverage import Beverage


class CondimentDecorator(Beverage):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    @abc.abstractmethod
    def get_description(self):
        pass
