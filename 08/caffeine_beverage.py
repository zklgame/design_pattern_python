import abc


class CaffeineBeverage(abc.ABC):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print('Boiling water')

    @abc.abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print('Pouring into cup')

    @abc.abstractmethod
    def add_condiments(self):
        pass

    # hook, can be changed in the sub-class
    def customer_wants_condiments(self):
        return True
