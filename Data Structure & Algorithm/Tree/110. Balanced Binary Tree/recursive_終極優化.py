# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        Solution: 終極優化(with early termination)
        Perf: Runtime: 36 ms, faster than 99.08% / Memory Usage: 16.4 MB, less than 79.03%
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if node is None:
            return 0
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(lh-rh) > 1:
            return -1
        return max(lh, rh)+1