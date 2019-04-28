from observer import Observer
from display_element import DisplayElement


class ThirdPartyDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        pass

    def update(self, temperature, humidity, pressure):
        self.display()

    def display(self):
        print('ThirdPartyDisplay')
