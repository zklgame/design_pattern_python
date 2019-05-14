from quackable import Quackable


class RedheadDuck(Quackable):

    def quack(self):
        print('Quack')
        self.notify_observers()
