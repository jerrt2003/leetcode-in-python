# -*- coding: utf-8 -*-
class Solution(object):
    def deleteExtraEdge(self, root):

        def dfs(node, left, right):
            if node is None:
                return None
            if node.val <= left or node.right >= right:
                return None
            node.left = dfs(node, left, node.val)
            node.right = dfs(node, node.val, right)
            return node

        dfs(root, -float('inf'), float('inf'))

