import abc


class Icon(abc.ABC):

    @abc.abstractmethod
    def get_icon_width(self):
        pass

    @abc.abstractmethod
    def get_icon_height(self):
        pass

    @abc.abstractmethod
    def paint_icon(self, x, y):
        pass
