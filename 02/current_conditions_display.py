from observer import Observer
from display_element import DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        super().__init__(weather_data)

        self.temperature = 0.
        self.humidity = 0.

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity

        self.display()

    def display(self):
        print('Current conditions: %.2fF degrees and %.2f%% humidity.'
              % (self.temperature, self.humidity))
