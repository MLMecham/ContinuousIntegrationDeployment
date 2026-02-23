from continuousintegrationdeployment.add_numbers import add
from continuousintegrationdeployment.template_package import multiply


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(-1.5, 0.5) == -1.0


def test_add_zero():
    assert add(0, 0) == 0


def test_multiply_default_factor():
    assert multiply(5) == 10.0


def test_multiply_custom_factor():
    assert multiply(3, 4) == 12


def test_multiply_zero():
    assert multiply(0, 100) == 0
