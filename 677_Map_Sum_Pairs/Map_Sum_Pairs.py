# -*- coding: utf-8 -*-
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        root = self.root
        for w in key:
            if w not in root.children:
                newNode = TrieNode(w)
                root.children[w] = newNode
            root = root.children[w]
        root.isWord = True
        root.value = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        root = self.root
        self.res = 0
        for p in prefix:
            if p not in root.children:
                return 0
            root = root.children[p]
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root.isWord:
            self.res += root.value
        if len(root.children) != 0:
            for kid in root.children.values():
                self.dfs(kid)




class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.isWord = False
        self.value = 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

obj = MapSum()
obj.insert("apple", 3)
obj.sum("ap")
obj.insert("app", 2)
obj.sum("ap")