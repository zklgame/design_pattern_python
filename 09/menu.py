import abc


class Menu(abc.ABC):

    @abc.abstractmethod
    def create_iterator(self):
        pass
