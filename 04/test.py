import unittest
from ny_pizza_store import NYPizzaStore
from ny_pizza_ingredient_factory import NYPizzaIngredientFactory


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('##################################')


class TestPizzaStore(TestCase):

    def test_NYPizzaStore(self):
        factory = NYPizzaIngredientFactory()
        store = NYPizzaStore(factory)
        store.order_pizza('cheese')


if __name__ == '__main__':
    unittest.main()
