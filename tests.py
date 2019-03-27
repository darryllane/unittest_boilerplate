import unittest
from calculator import add, divide, multiply, subtract


class CalculatorTestCase(unittest.TestCase):
    """Tests for `calculator.py`."""

    def test_add(self):
        """Is add function working correctly"""
        self.assertEquals(add(2,2), 4)
    
    def test_subtract(self):
        """Is subtract function working correctly"""
        self.assertEquals(subtract(2,2), 0)
    
    def test_divide(self):
        """Is divide function working correctly"""
        self.assertEquals(divide(2,2), 1)
        
    def test_multiply(self):
        """Is multiply function working correctly"""
        self.assertEquals(multiply(2,2), 4)      

if __name__ == '__main__':
    unittest.main()
