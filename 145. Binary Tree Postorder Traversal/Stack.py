# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        Facebook
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - using stack
        - reverse the result to obtain the final result
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]

