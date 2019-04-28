from observer import Observer
from display_element import DisplayElement


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather):
        super().__init__(weather)

        self.max_temp = 0.
        self.min_temp = 200.
        self.temp_sum = 0.
        self.num_readings = 0

    def update(self, temperature, humidity, pressure):
        self.temp_sum += temperature
        self.num_readings += 1

        self.max_temp = max(self.max_temp, temperature)
        self.min_temp = min(self.min_temp, temperature)

        self.display()

    def display(self):
        print('Avg/Max/Min temperature = %.2f/%.2f/%.2f'
              % (self.temp_sum / self.num_readings,
                 self.max_temp,
                 self.min_temp))
