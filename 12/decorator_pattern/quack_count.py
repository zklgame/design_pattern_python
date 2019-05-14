from quackable import Quackable


class QuackCount(Quackable):

    number_of_quacks = 0

    def __init__(self, duck):
        super().__init__()
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCount.number_of_quacks += 1

    @classmethod
    def get_quacks(cls):
        return cls.number_of_quacks

    def register_observer(self, observer):
        self.duck.register_observer(observer)

    def notify_observers(self):
        self.duck.notify_observers()
