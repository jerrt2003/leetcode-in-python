# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/symmetric-tree/solution/
        Thinking Process:
        - When will 2 trees satisfy "reflection"..?
            - 2 trees root value is same
            - t1.left is mirror of the t2.right
            - t1.right is mirror of the t2.left
        - Algorithm:
        if t1 is None and t2 is None: return True
        if t1 is None or t2 is None: return False
        return t1.val == t2.val && isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left)
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(t1, t2):
            if t1 is None and t2 is None: return True
            if t1 is None or t2 is None: return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)