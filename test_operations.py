import calculator
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)

    def test_minus(self):
        self.assertEqual(calculator.minus(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
