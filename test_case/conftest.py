"""
Conftest.py

Description:
    This demonstrates how to use conftest in pytest.



Author:
    Oluwwaseun Adeyo

Date:
    2nd May, 2024

Notes:
    Conftest allows you to declare values which can be used in other test files.
"""

import pytest

from src.my_class import Circle, Rectangle


# This instance of Rectangle is used in test_conftest_instance() in the test_rectangle file
@pytest.fixture
def conftest_rectangle():
    return Rectangle(50, 20)


# This instance of Circle is used in test_conftest_instance() in the test_circle file
@pytest.fixture
def conftest_circle():
    return Circle(5)
