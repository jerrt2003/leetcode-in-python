# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, curr_sum):
        if node.left is None and node.right is None:
            self.res += curr_sum*10 + node.val
            return
        if node.left:
            self.dfs(node.left, curr_sum*10 + node.val)
        if node.right:
            self.dfs(node.right, curr_sum*10 + node.val)

