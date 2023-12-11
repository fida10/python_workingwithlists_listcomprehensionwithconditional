import unittest
from src.ans import negative_to_zero

class TestNegativeToZero(unittest.TestCase):
    def test_negative_to_zero(self):
        self.assertEqual(negative_to_zero(
            [1, -2, 3, -4, 5, -6]), [1, 0, 3, 0, 5, 0])

    def test_no_negatives(self):
        self.assertEqual(negative_to_zero([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_negatives(self):
        self.assertEqual(negative_to_zero([-1, -2, -3]), [0, 0, 0])


if __name__ == '__main__':
    unittest.main()
