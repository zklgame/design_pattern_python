import abc


class Turkey(abc.ABC):

    @abc.abstractmethod
    def gobble(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass
