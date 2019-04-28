import unittest
from weather_data import WeatherData
from current_conditions_display import CurrentConditionsDisplay
from forecast_display import ForecastDisplay
from statistics_display import StatisticsDisplay
from third_party_display import ThirdPartyDisplay
from heat_index_display import HeatIndexDisplay


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('##################################')


class TestDisplayElement(TestCase):

    def setUp(self):
        self.weather_data = WeatherData()

    def test_CurrentConditionsDisplay(self):
        display = CurrentConditionsDisplay(self.weather_data)
        self.weather_data.set_measurements(1, 2, 3)

    def test_ForecastDisplay(self):
        display = ForecastDisplay(self.weather_data)
        self.weather_data.set_measurements(1, 2, 3)
        self.weather_data.set_measurements(1, 2, 4)
        self.weather_data.set_measurements(1, 2, 4)

    def test_StatisticsDisplay(self):
        display = StatisticsDisplay(self.weather_data)
        self.weather_data.set_measurements(2, 2, 3)
        self.weather_data.set_measurements(4, 2, 3)
        self.weather_data.set_measurements(1, 2, 3)

    def test_ThirdPartyDisplay(self):
        display = ThirdPartyDisplay(self.weather_data)
        self.weather_data.set_measurements(1, 2, 3)

    def test_weather_station(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)
        heat_index_display = HeatIndexDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)

    def test_remove_observer(self):
        display = StatisticsDisplay(self.weather_data)
        self.weather_data.set_measurements(1, 2, 3)
        self.weather_data.remove_observer(display)
        self.weather_data.set_measurements(3, 2, 1)


if __name__ == '__main__':
    unittest.main()
