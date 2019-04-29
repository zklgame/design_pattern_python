import unittest
from espresso import Espresso
from house_blend import HouseBlend
from decaf import Decaf
from dark_roast import DarkRoast
from milk import Milk
from mocha import Mocha
from soy import Soy
from whip import Whip


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('##################################')


class TestBeverage(TestCase):

    def test_DarkRoast(self):
        dark_roast = DarkRoast()
        self.simulate(dark_roast)

    def test_Decaf(self):
        decaf = Decaf()
        self.simulate(decaf)

    def test_Espresso(self):
        espresso = Espresso()
        self.simulate(espresso)

    def test_HouseBlend(self):
        house_blend = HouseBlend()
        self.simulate(house_blend)

    def test_starbuzz_coffee(self):
        beverage_1 = Espresso()
        self.simulate(beverage_1)

        beverage_2 = DarkRoast()
        beverage_2 = Mocha(beverage_2)
        beverage_2 = Mocha(beverage_2)
        beverage_2 = Whip(beverage_2)
        self.simulate(beverage_2)

        beverage_3 = HouseBlend()
        beverage_3 = Soy(beverage_3)
        beverage_3 = Mocha(beverage_3)
        beverage_3 = Whip(beverage_3)
        self.simulate(beverage_3)

    def simulate(self, beverage):
        print(beverage.get_description(), beverage.cost())


if __name__ == '__main__':
    unittest.main()
