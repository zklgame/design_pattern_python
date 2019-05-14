import abc
from observer_pattern.observable import Observable
from observer_pattern.quack_observable import QuackObservable


class Quackable(Observable):

    def __init__(self):
        super().__init__()
        self.observable = QuackObservable(self)

    @abc.abstractmethod
    def quack(self):
        pass

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()
