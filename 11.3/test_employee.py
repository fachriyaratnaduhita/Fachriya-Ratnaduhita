
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create an employee instance for use in all test methods."""
        self.my_employee = Employee('john', 'doe', 50000)

    def test_give_default_raise(self):
        """Test that a default raise of $5000 works correctly."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test that a custom raise amount works correctly."""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()