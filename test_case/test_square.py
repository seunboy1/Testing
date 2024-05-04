import math
import pytest
from src.my_class import Square, Shape

"""
Parametarize allows you to run the same tests with different values without the 
use of for loops
"""
@pytest.mark.parametrize("length, expected_area", [(5,25), (4,16), (6,36)])
def test_multiple_square_areas(length, expected_area):
    assert Square(length).area() == expected_area

@pytest.mark.parametrize("length, expected_perimeter", [(5,20), (4,16), (6,24)])
def test_multiple_square_perimeter(length, expected_perimeter):
    assert Square(length).perimeter() == expected_perimeter