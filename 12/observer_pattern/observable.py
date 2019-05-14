import abc


class Observable(abc.ABC):

    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass
