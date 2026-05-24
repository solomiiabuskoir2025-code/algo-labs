class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end_of_word


def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

def find_criminal(trie, dna_list):

    for i, dna in enumerate(dna_list):
        if trie.search(dna):
            return i
    return -1

if __name__ == "__main__":

    criminal_dna_patterns = [
        "ACGT",
        "GCTA",
        "TTAG",
        "CGTA"
    ]

    people_dna = [
        "AAAAAA",
        "TTAG",
        "CCCCCC",
        "GGGGGG"
    ]


    trie = build_trie(criminal_dna_patterns)

    result = find_criminal(trie, people_dna)

    if result != -1:
        print(f"find criminal!!!! №{result} attention")
    else:
        print("all clean")