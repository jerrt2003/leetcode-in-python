# -*- coding: utf-8 -*-
import collections


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = collections.Counter()
        self.words = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                self.pool[key] += 1
            self.words.add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if word in self.words:
            return False
        for i in range(len(word)):
            key = word[:i] + '*' + word[i + 1:]
            if key in self.pool:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

words = ["hello","hallo","leetcode"]
m = MagicDictionary()
m.buildDict(words)
print m.search('pello')