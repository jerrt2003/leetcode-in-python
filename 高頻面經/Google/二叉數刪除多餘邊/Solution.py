# -*- coding: utf-8 -*-
class Solution(object):
    def deleteExtraEdgeInBS(self, node):
        self.visited = set()
        self.helper(node)

    def helper(self, node):
        if not node:
            return
        self.visited.add(node)
        if node.left in self.visited:
            node.left = None
            return
        if node.right in self.visited:
            node.right = None
            return
        self.helper(node.left)
        self.helper(node.right)