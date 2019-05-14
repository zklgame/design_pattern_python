from observer_pattern.observable import Observable


class QuackObservable(Observable):

    def __init__(self, duck):
        super().__init__()
        self.observers = []
        self.duck = duck

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)
