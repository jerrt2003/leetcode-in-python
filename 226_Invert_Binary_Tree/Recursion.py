# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        def invert(node=None):
            if node.left is None and node.right is None:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left is not None:
                invert(node.left)
            if node.right is not None:
                invert(node.right)

        invert(root)
        return root
