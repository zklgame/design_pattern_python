import abc


class State(abc.ABC):

    def __init__(self, machine):
        super().__init__()
        self.machine = machine

    @abc.abstractmethod
    def insert_quarter(self):
        pass

    @abc.abstractmethod
    def eject_quarter(self):
        pass

    @abc.abstractmethod
    def turn_crank(self):
        pass

    @abc.abstractmethod
    def dispense(self):
        pass
