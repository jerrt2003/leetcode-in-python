# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        Sol: BS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 72 ms, faster than 67.36% / Memory Usage: 15.8 MB, less than 50.51%
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(node, val):
            if node.val == val:
                return node
            if node.left:
                res = search(node.left, val)
                if res:
                    return res
            if node.right:
                res = search(node.right, val)
                if res:
                    return res
            return None

        return search(root, val)
