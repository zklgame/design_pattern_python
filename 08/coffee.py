from caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):

    def brew(self):
        print('Dripping Coffee through filter')

    def add_condiments(self):
        print('Adding Sugar and Milk')

    def customer_wants_condiments(self):
        return False
