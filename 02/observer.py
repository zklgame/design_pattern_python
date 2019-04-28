import abc


class Observer(abc.ABC):

    @abc.abstractmethod
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

