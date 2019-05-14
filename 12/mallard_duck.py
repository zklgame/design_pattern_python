from quackable import Quackable


class MallardDuck(Quackable):

    def quack(self):
        print('Quack')
        self.notify_observers()
