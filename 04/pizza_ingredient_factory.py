import abc


# abstract factory pattern
class PizzaIngredientFactory(abc.ABC):

    @abc.abstractmethod
    def create_dough(self):
        pass

    @abc.abstractmethod
    def create_sauce(self):
        pass

    @abc.abstractmethod
    def create_cheese(self):
        pass

    @abc.abstractmethod
    def create_veggies(self):
        pass

    @abc.abstractmethod
    def create_pepperoni(self):
        pass

    @abc.abstractmethod
    def create_clam(self):
        pass
