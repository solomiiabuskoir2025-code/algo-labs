import unittest
from avl_priority_queue import PriorityQueueAVL


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = PriorityQueueAVL()

    def test_push_peek(self):
        self.q.push("A", 1)
        self.q.push("B", 5)
        self.q.push("C", 3)
        self.assertEqual(self.q.peek(), "B")

    def test_pop(self):
        self.q.push("A", 1)
        self.q.push("B", 5)
        self.q.push("C", 3)

        self.assertEqual(self.q.pop(), "B")
        self.assertEqual(self.q.pop(), "C")
        self.assertEqual(self.q.pop(), "A")

    def test_empty(self):
        self.assertIsNone(self.q.pop())
        self.assertIsNone(self.q.peek())

    def test_show(self):
        self.q.push("A", 2)
        self.q.push("B", 1)
        self.q.push("C", 3)

        result = self.q.show()
        self.assertEqual(result, [("B", 1), ("A", 2), ("C", 3)])


if __name__ == "__main__":
    unittest.main()