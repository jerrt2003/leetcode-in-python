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
        Solution: In order traversal
        Time Complexity: O(n)
        Space Complexity: O(n)
        :type root: TreeNode
        :rtype: bool
        """

        # in-order traversal
        def helper(node, path):
            if node is None:
                return
            if node.left:
                helper(node.left, path)
            path.append(node.val)
            if node.right:
                helper(node.right, path)

        path = []
        helper(root, path)
        prev = path[0]
        for i in range(1, len(path)):
            if prev >= path[i]:
                return False
            prev = path[i]
        return True
