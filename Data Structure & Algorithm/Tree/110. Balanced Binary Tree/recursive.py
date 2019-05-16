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
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh = self.maxHeight(root.left)
        rh = self.maxHeight(root.right)
        if abs(lh-rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def maxHeight(self, node):
        if node is None:
            return 0
        return 1 + max(self.maxHeight(node.left), self.maxHeight(node.right))