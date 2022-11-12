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
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
        Thinking Process:
        - Continue to check every node, if not balanced, then return -1 otherwise return current depth
        - At the end if the return == -1 which mean tree is not balanced
        Algorithm:
        def check(root):
            if root is None: return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1+max(left, right)
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            if left == -1:
                return -1
            right = check(root.right)
            if right == -1 or abs(left - right) > 1: # need to use abs because right side might be bigger
                return -1
            return 1 + max(left, right) # calculate the depth and return

        return check(root) != -1


