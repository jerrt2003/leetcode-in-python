# -*- coding: utf-8 -*-
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        Solution: Trie
        Time Complexity: O(mn)
        Space Complexity: O(mn)
        Perf: Runtime: 144 ms, faster than 74.53% / Memory Usage: 51.8 MB, less than 6.67%
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)

        res = []
        for cand in sentence.split(' '):
            search_result = trie.search(cand, '')
            if search_result is not None:
                cand = search_result
            res.append(cand)

        return ' '.join(res)

class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                newNode = TrieNode(w)
                root.children[w] = newNode
            root = root.children[w]
        root.isEnd = True

    def search(self, word, path):
        root = self.root
        for s in word:
            if root.isEnd:
                return path
            else:
                if s not in root.children:
                    return None
                else:
                    root = root.children[s]
                    path += root.char

class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.isEnd = False


dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print Solution().replaceWords(dict, sentence)