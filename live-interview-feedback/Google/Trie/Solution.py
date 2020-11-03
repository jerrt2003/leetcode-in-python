# -*- coding: utf-8 -*-
class Solution(object):
    def findAllPossible(self, words, target):
        trie = Trie()
        for word in words:
            trie.build(word)
        node, path, i = trie.find(target)
        self.res = []

        def dfs(node, path, i):
            if i == len(target):
                if node.isEnd:
                    self.res.append(path)
                    return
            for n in node.children.values():
                dfs(n, path+n.c, i+1)

        dfs(node, path, i)
        return self.res

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def build(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                trie = TrieNode(w)
                node.children[w] = trie
            node = node.children[w]
        node.isEnd = True

    def find(self, word):
        node = self.root
        path = ''
        i = 0
        for w in word:
            if w in node.children:
                path += w
                i += 1
                node = node.children[w]
            else:
                break
        return node, path, i

class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = dict()
        self.isEnd = False


words = ['DAVID','DAD','BAD','DAVIS']
#target = 'DAVIK'
target = 'CAD'

print Solution().findAllPossible(words, target)