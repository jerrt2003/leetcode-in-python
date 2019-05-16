# -*- coding: utf-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        return trie.search(s)

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.isEnd = True

    def cache(f):
        def method(obj, s):
            if s not in obj.cache:
                obj.cache[s] = f(obj, s)
            return obj.cache
        return method

    def search(self, word):
        root = self.root
        for i, char in enumerate(word):
            if char not in root.children:
                return False
            if root.children[char].isEnd:
                if self.search(word[i+1:]):
                    return True
            root = root.children[char]
        return root.isEnd



class TrieNode(object):
    def __init__(self):
        self.children = dict() # {char: node}
        self.isEnd = False

s = "leetcode"
wordDict = ["leet", "code"]

print Solution().wordBreak(s, wordDict)