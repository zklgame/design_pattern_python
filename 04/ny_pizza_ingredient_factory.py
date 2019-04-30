from pizza_ingredient_factory import PizzaIngredientFactory


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return 'Thin Crust Dough'

    def create_sauce(self):
        return 'Marinara Sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'

    def create_veggies(self):
        return ['Garlic', 'Onion', 'Mushroom', 'RedPepper']

    def create_pepperoni(self):
        return 'Sliced Pepperoni'

    def create_clam(self):
        return 'Fresh Clams'
