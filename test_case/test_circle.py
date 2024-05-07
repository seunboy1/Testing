import math
from src.my_class import Circle


class TestCircle:

    """
        A simple Test case for the my_class scripts.
        Note: Class based test comes with 2 default functions 
        1. Set up method 
        2. Tear down method

        Alternatively you can use @pytest.fixture

        Note: To get pytest to print things to the commandline use -s flag. pytest test_case/test_circle.py -s
    """

    def setup_method(self, method):
        #pylint: disable=attribute-defined-outside-init

        """
            This is defined to run tear down code after each test method
        """

        print(f"Setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):

        """
            This is defined to run set up code before each test method
        """

        print(f"Tearing down {method}")
        del self.circle

    
    def test_area(self):
        circle = self.circle
        assert circle.area() ==  math.pi * circle.radius ** 2

    def test_perimeter(self):
        circle = self.circle
        assert circle.perimeter() ==  2 * math.pi * circle.radius

    def test_conftest_instance(self, conftest_circle):
        assert conftest_circle.perimeter() ==  2 * math.pi * conftest_circle.radius

