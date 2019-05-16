# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        Solution: Iterative + Stack
        Time Complexity:O(n)
        Space Complexity:O(n)
        Inspired By: https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
        Thinking Process:
        Algorithm:
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.stack = []
        self.traversal(root)
        return self.res

    def traversal(self, curr):
        while curr is not None or len(self.stack) != 0:
            while curr is not None:
                self.stack.append(curr)
                curr = curr.left
            curr = self.stack.pop()
            self.res.append(curr.val)
            curr = curr.right