import abc


class Beverage(abc.ABC):

    def __init__(self, description='Unknown Beverage'):
        self.description = description

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass
