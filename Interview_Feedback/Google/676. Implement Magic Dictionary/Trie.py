# -*- coding: utf-8 -*-
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in words:
            node = self.root
            for w in word:
                if w not in node.children:
                    trie = Trie(w)
                    node.children[w] = trie
                node = node.children[w]
            node.isEnd = True


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """


    def _search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isEnd


class Trie(object):

    def __init__(self, w=None):
        self.w = w
        self.children = dict()
        self.isEnd = False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

words = ["hello","hallo","leetcode"]
m = MagicDictionary()
m.buildDict(words)
print m.search('hello')