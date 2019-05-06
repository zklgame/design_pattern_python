import abc


class Duck(abc.ABC):

    @abc.abstractmethod
    def quack(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass
