# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 52 ms, faster than 69.52% / Memory Usage: 16.1 MB, less than 24.34%
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def traverse(node, path):
            if node is None:
                return
            if node.left:
                traverse(node.left, path)
            path.append(node.val)
            if node.right:
                traverse(node.right, path)
        path = []
        traverse(root, path)
        res = float('inf')
        for i in range(1, len(path)):
            res = min(res, path[i] - path[i-1])
        return res