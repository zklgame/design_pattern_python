import abc


class Subject(abc.ABC):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def set_name(self, name):
        pass

    @abc.abstractmethod
    def get_gender(self):
        pass

    @abc.abstractmethod
    def set_gender(self, gender):
        pass

    @abc.abstractmethod
    def get_interests(self):
        pass

    @abc.abstractmethod
    def set_interests(self, interests):
        pass

    @abc.abstractmethod
    def get_hot_or_not_rating(self):
        pass

    @abc.abstractmethod
    def set_hot_or_not_rating(self, rating):
        pass
