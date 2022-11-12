# -*- coding: utf-8 -*-
class Trie(object):
    """
    Time Complexity:
    - insert: O(mn)
    - search: O(mn)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            if w not in root.children:
                newNode = TrieNode(w)
                root.children[w] = newNode
            root = root.children[w]
        root.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for p in prefix:
            if p not in root.children:
                return False
            root = root.children[p]
        return True

class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.isEnd = False


obj = Trie()
obj.insert('apple')
print obj.search('apple')

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)