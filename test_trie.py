import unittest

from trie import Trie, build_trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.trie.insert("cat")
        self.trie.insert("car")
        self.trie.insert("dog")

    def test_insert_and_search_existing_word(self):
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("car"))
        self.assertTrue(self.trie.search("dog"))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("cow"))

    def test_search_prefix_not_word(self):
        self.assertFalse(self.trie.search("ca"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertTrue(self.trie.starts_with("do"))

    def test_starts_with_non_existing_prefix(self):
        self.assertFalse(self.trie.starts_with("xy"))

    def test_build_trie(self):
        patterns = ["apple", "app", "banana"]

        trie = build_trie(patterns)

        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("banana"))
        self.assertFalse(trie.search("ban"))


if __name__ == "__main__":
    unittest.main()
