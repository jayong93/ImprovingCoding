class Node:
    def __init__(self, value=None):
        self.children = {}
        self.value = value

class Trie:
    def __init__(self):
        self.root = Node()

    def insert_words(self, word):
        cur_node = self.root
        
        for i, char in enumerate(word):
            if char in cur_node.children.keys():
                cur_node = cur_node.children[char]
            else:
                break

        for j, char in enumerate(word[i:]):
            cur_node.children[char] = Node()
            cur_node = cur_node.children[char]
        cur_node.value = word

    def count_chr_to_find_word(self, word):
        cur_node = self.root
        count = 0

        for char in word:
            cur_node = cur_node.children[char]
            count += 1
            if self._is_unique(cur_node, word):
                break

        return count

    def _is_unique(self, cur_node, word):
        while len(cur_node.children) > 0:
            if len(cur_node.children) > 1:
                return False
            if cur_node.value is not None:
                return False
            cur_node = list(cur_node.children.values())[0]

        return True

if __name__ == "__main__":
    inputs = [["go", "gone", "guild"], ["abc", "def", "ghi", "jklm"], ["word", "war", "warrior", "world"]]

    for inp in inputs:
        count = 0
        trie = Trie()
        for word in inp:
            trie.insert_words(word)
        for word in inp:
            count += trie.count_chr_to_find_word(word)

        print(count)
