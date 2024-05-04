import math
import pytest
from src.my_class import Rectangle, Shape

"""
    Fixtures are functions, which will run before each test function to which it is applied. 
    Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. 
    Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run 
    and return the data to the test before executing each test.

"""

rect = Rectangle(50,20)

@pytest.fixture
def my_rectangle():
    return Rectangle(10,20)

@pytest.fixture
def weird_rectangle():
    return Rectangle(5,6)

def test_area(my_rectangle):
    assert my_rectangle.area() ==  10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() ==  (2 * 10) + (2 * 20)

def test_instance_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

def test_conftest_instance(conftest_rectangle):
    assert conftest_rectangle.area() ==  50 * 20

