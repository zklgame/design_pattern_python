import unittest
from tea import Tea
from coffee import Coffee


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('###################')


class TestCaffeineBeverages(TestCase):

    def test_Tea(self):
        tea = Tea()
        tea.prepare_recipe()

    def test_Coffee(self):
        coffee = Coffee()
        coffee.prepare_recipe()


if __name__ == '__main__':
    unittest.main()
