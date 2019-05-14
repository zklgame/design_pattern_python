from quackable import Quackable


class DuckCall(Quackable):

    def quack(self):
        print('Kwak')
        self.notify_observers()
