import unittest
from lab2 import aggressive_cows

class TestAggressiveCows(unittest.TestCase):
    def test_example_case(self):
        stalls = [1, 2, 8, 4, 9]
        cows = 3
        self.assertEqual(aggressive_cows(stalls, cows), 3)

    def test_small_case(self):
        stalls = [1, 2]
        cows = 2
        self.assertEqual(aggressive_cows(stalls, cows), 1)

    def test_large_gap(self):
        stalls = [1, 10, 20, 30]
        cows = 2
        self.assertEqual(aggressive_cows(stalls, cows), 29)

    def test_three_cows_far_apart(self):
        stalls = [1, 5, 9, 15]
        cows = 3
        self.assertEqual(aggressive_cows(stalls, cows), 6)

if __name__ == "__main__":
    unittest.main()
