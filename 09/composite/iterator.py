import abc


class Iterator(abc.ABC):

    @abc.abstractmethod
    def has_next(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass
