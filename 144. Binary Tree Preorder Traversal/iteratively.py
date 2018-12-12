# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        Solution: Iterative(迭代)
        Time Complexity:
        Space Complexity:
        Thinking Process:
        - Using Stack and LIFO(last in first out)
        - Store from right node first
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        self.res = []
        self.traversal([root])
        return self.res


    def traversal(self, stack):
        while stack:
            node = stack.pop()
            self.res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
