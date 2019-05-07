import abc


class MenuComponent(abc.ABC):

    def get_name(self):
        raise NotImplementedError()

    def get_description(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def is_vegetarian(self):
        raise NotImplementedError()

    def print(self):
        raise NotImplementedError()

    def add(self, component):
        raise NotImplementedError()

    def remove(self, component):
        raise NotImplementedError()

    def get_child(self, i):
        raise NotImplementedError()

    @abc.abstractmethod
    def create_iterator(self):
        pass
