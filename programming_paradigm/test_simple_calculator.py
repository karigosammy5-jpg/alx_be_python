import unittest
# Import the class you intend to test
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, covering all arithmetic methods.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        # Create a new instance of the calculator for every test
        self.calc = SimpleCalculator()

    # --- Test Methods for Addition ---

    def test_addition_positive_numbers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_addition_negative_numbers(self):
        """Test addition with two negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_addition_mixed_numbers(self):
        """Test addition with positive and negative numbers."""
        self.assertEqual(self.calc.add(10, -3), 7)

    def test_addition_with_zero(self):
        """Test addition involving zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Test Methods for Subtraction ---

    def test_subtraction_positive_numbers(self):
        """Test subtraction with two positive integers (positive result)."""
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtraction_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    # --- Test Methods for Multiplication ---

    def test_multiplication_positive(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_by_zero(self):
        """Test multiplication where one factor is zero."""
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_multiplication_negative_mixed(self):
        """Test multiplication with one negative factor."""
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    # --- Test Methods for Division ---

    def test_division_normal(self):
        """Test a standard division scenario."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_division_float_result(self):
        """Test division resulting in a floating-point number."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_by_zero_edge_case(self):
        """Test the crucial edge case: division by zero."""
        # The SimpleCalculator returns None for division by zero
        self.assertIsNone(self.calc.divide(10, 0))

# Standard way to run tests from the script itself
if __name__ == '__main__':
    unittest.main()