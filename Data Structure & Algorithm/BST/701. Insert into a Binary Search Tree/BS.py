# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        Sol: BS
        Time: O(log(n))
        Space: O(log(n))
        Perf: Runtime: 120 ms, faster than 17.08% / Memory Usage: 15.9 MB, less than 49.48%
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            node = TreeNode(val)
            return node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

