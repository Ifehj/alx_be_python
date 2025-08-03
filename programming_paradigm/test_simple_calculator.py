import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -6), 3)

    def test_subtraction_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_multiplication_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 999), 0)

    # --- Division Tests ---
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_with_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
