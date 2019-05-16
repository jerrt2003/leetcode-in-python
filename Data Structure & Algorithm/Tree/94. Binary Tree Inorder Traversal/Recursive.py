# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        Solution: recursive
        Time complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 16 ms, faster than 98.33% / Memory Usage: 11.6 MB, less than 97.68%
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node is None:
            return
        if node.left:
            self.helper(node.left)
        self.res.append(node.val)
        if node.right:
            self.helper(node.right)