import unittest

class MathsTest(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(1+2,3)

    def test_subtraction(self):
        self.assertEqual(1-2,-1)

    def test_divbyzero(self):
        with self.assertRaises(ZeroDivisionError):
            1/0

if __name__ == '__main__':
    unittest.main(verbosity=3)
