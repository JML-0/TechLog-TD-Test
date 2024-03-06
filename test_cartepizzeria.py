import unittest
from unittest.mock import Mock
from cartepizzeria import CartePizzeria

def test_is_not_empty():
    pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]
    assert not cp.is_empty()

def test_nb_pizzas():
    pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]
    assert cp.nb_pizzas() == 1

def test_add_pizza():
    pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]
    cp.add_pizza(pizza)
    assert cp.nb_pizzas() == 2

def test_remove_pizza():
    pizza = Mock()
    pizza2 = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]
    cp.add_pizza(pizza2)
    cp.remove_pizza("pizza2")
    assert cp.nb_pizzas() == 1