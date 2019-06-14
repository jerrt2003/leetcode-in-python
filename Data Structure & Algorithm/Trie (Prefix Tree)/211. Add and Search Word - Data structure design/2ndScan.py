# -*- coding: utf-8 -*-
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for c in word:
            if root.val != c:
                newTrie = Trie(c)
                root.children[c] = newTrie
                root = root.children[c]
            root.isEnd = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.root)


    def _search(self, word, idx, root):
        if idx == len(word):
            return root.isEnd
        if word[idx] != '.':
            if word[idx] in root.children:
                return self._search(word, idx+1, root.children[word[idx]])
            else:
                for child in root.children.values():
                    if self._search(word, idx+1, child):
                        return True
        return False



class Trie(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.isEnd = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)