# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By:
        Thinking Process:
        - Use recursion
        - If node's left & right is None, then we hit left node, so we can compare the min_path with current accumulated path
        :type root: TreeNode
        :rtype: int
        """
        self.min_path = float('inf')
        if root is None: return 0
        self.findMinDepth(root, 0)
        return self.min_path

    def findMinDepth(self, node, path):
        path += 1
        if node.left is None and node.right is None:
            self.min_path = min(self.min_path, path)
            return
        if node.left is not None:
            self.findMinDepth(node.left, path)
        if node.right is not None:
            self.findMinDepth(node.right, path)
