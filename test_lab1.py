import unittest
from lab1 import find_k_largest


class FindKLargest(unittest.TestCase):

    def test_example(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        value, index = find_k_largest(arr, k)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

    def test_first_largest(self):
        arr = [1, 5, 3]
        value, index = find_k_largest(arr, 1)
        self.assertEqual(value, 5)
        self.assertEqual(index, 1)

    def test_second_largest(self):
        arr = [10, 20, 30]
        value, index = find_k_largest(arr, 2)
        self.assertEqual(value, 20)
        self.assertEqual(index, 1)

    def test_invalid_k(self):
        arr = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_k_largest(arr, 0)
        with self.assertRaises(ValueError):
            find_k_largest(arr, 5)


if __name__ == '__main__':
    unittest.main()