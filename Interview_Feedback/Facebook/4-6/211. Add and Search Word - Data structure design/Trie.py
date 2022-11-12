# -*- coding: utf-8 -*-
class WordDictionary(object):
    """
    Solution: Trie
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    Perf: Runtime: 460 ms, faster than 22.54% / Memory Usage: 36 MB, less than 5.51%
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word, 0)


    def _search(self, root, word, pos):
        if pos == len(word):
            if root.isEnd:
                return True
            else:
                return False
        if word[pos] != '.':
            if word[pos] in root.children:
                return self._search(root.children[word[pos]], word, pos+1)
        else:
            for node in root.children.values():
                if self._search(node, word, pos+1):
                    return True
        return False


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = dict()
        self.isEnd = False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
#obj.addWord('bad')
#obj.addWord('dad')
#obj.addWord('mad')
#obj.search('pad')
#print obj.search('bad')
#print obj.search('.ad')
#obj.search('c..')
