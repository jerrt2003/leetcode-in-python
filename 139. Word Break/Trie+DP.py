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
            trie.add(word)

        m = len(s)
        dp = [False] * (m+1)
        dp[0] = True

        for i in range(m):
            for j in range(i, m):
                if dp[i] and trie.search(s[i:j+1]):
                    dp[j+1] = True
        return dp[-1]



class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                node = TrieNode(w)
                root.children[w] = node
            root = root.children[w]
        root.isEnd = True

    def search(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.isEnd

class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = dict()
        self.isEnd = False

s = "leetcode"
wordDict = ["leet", "code"]
assert Solution().wordBreak(s, wordDict) == True