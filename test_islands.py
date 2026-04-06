import unittest
from lab5 import count_islands_bfs   # імпорт з твого файлу

class TestCountIslandsBFS(unittest.TestCase):
    def test_example_matrix(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(count_islands_bfs(matrix), 6)

    def test_empty_matrix(self):
        self.assertEqual(count_islands_bfs([]), 0)

    def test_single_island(self):
        matrix = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(count_islands_bfs(matrix), 1)

    def test_no_islands(self):
        matrix = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(count_islands_bfs(matrix), 0)

if __name__ == "__main__":
    unittest.main()