# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        Sol: DFS
        Perf: Runtime: 68 ms, faster than 98.80% / Memory Usage: 24.2 MB, less than 72.50%
        T: O(V+E)
        S: O(V+E)
        :type root: TreeNode
        :rtype: int
        """
        self.res = -float('inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        l = max(0, self.dfs(node.left))
        r = max(0, self.dfs(node.right))
        self.res = max(self.res, l + r + node.val)
        return max(l, r) + node.val