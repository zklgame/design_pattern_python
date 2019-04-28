from observer import Observer
from display_element import DisplayElement


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        super().__init__(weather_data)

        self.current_pressure = 29.92
        self.last_pressure = 0.

    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure

        self.display()

    def display(self):
        print('Forecast: ', end='')
        if self.current_pressure > self.last_pressure:
            print('Improving weather on the day!')
        elif self.current_pressure == self.last_pressure:
            print('More of the same.')
        else:
            print('Watch out for cooler, rainy weather!')
