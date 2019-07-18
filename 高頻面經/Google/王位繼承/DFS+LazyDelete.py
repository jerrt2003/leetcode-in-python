# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def __init__(self, king):
        self.tree = collections.defaultdict(list)
        self.root = king
        self.dead = set()

    def birth(self, parent, kid):
        if parent not in self.tree:
            print('parent not exist')
            return
        self.tree[parent].append(kid)

    def dead(self, name):
        self.dead.add(name)

    def getOrder(self):
        res = []

        def dfs(root, res):
            if root not in self.dead:
                res.append(root)
            for node in self.tree[root]:
                dfs(node, res)

        dfs(self.root, res)
        return res