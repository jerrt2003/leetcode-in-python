# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        Perf: Runtime: 28 ms, faster than 62.82% / Memory Usage: 12.1 MB, less than 65.53%
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.node = None

        def reversePreorder(node):
            if not node:
                return
            reversePreorder(node.right)
            reversePreorder(node.left)
            node.left = None
            node.right = self.prev
            self.prev = node

        reversePreorder(root)