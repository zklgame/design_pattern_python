from quackable import Quackable


class RubberDuck(Quackable):

    def quack(self):
        print('Squeak')
        self.notify_observers()
