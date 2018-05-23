class Node:
    def __init__(self, value=None):
        self.children = {}
        self.value = value

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert_words(self, word):
        cur_node = self.root
        
        for i, char in enumerate(word):
            if char in cur_node.children.keys():
                cur_node = cur_node.children[char]
            else:
                break

        for char in word[i:]:
            pass

    def count_chr_to_find_word(self, word):
        pass


if __name__ == "__main__":
    trie = Trie()
