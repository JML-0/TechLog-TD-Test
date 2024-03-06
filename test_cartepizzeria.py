import unittest
from unittest.mock import Mock
from cartepizzeria import CartePizzeria

class TestCartePizzeria(unittest.TestCase):

    def test_is_not_empty(self):
        pizza = Mock()
        cp = CartePizzeria()
        cp.pizzas = [pizza]
        assert not cp.is_empty()

    def test_nb_pizzas(self):
        pizza = Mock()
        cp = CartePizzeria()
        cp.pizzas = [pizza]
        assert cp.nb_pizzas() == 1

    def test_add_pizza(self):
        pizza = Mock()
        cp = CartePizzeria()
        self.assertTrue(len(cp.pizzas) == 0)
        cp.add_pizza(pizza)
        self.assertTrue(len(cp.pizzas) == 1)

    def test_remove_pizza(self):
        pizza = Mock()
        pizza.name = "calzone"
        pizza2 = Mock()
        pizza2.name = "canibale"
        cp = CartePizzeria()
        cp.pizzas = [pizza]
        cp.add_pizza(pizza2)
        self.assertTrue(len(cp.pizzas) == 2)
        cp.remove_pizza("canibale")
        self.assertTrue(len(cp.pizzas) == 1)
    
if __name__ == "__main__":
    unittest.main()