# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 28 ms, faster than 97.24% / Memory Usage: 16.4 MB, less than 57.44%
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, lower, upper):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return self.helper(node.left, lower, node.val) and self.helper(node.right, node.val, upper)