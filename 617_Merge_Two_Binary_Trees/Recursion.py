# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None: return None
        if t1 is None and t2 is not None: return t2
        if t2 is None and t1 is not None: return t1
        def merge(t1, t2):
            t1.val += t2.val
            if t1.left is not None and t2.left is not None:
                merge(t1.left, t2.left)
            if t1.left is None and t2.left is not None:
                t1.left = t2.left
            if t1.right is not None and t2.right is not None:
                merge(t1.right, t2.right)
            if t1.right is None and t2.right is not None:
                t1.right = t2.right
            return

        merge(t1, t2)
        return t1

T_A4 = TreeNode(5)
T_A5 = TreeNode(4)
T_A6 = TreeNode(7)
T_A2 = TreeNode(3)
T_A2.left = T_A4
T_A2.right = T_A5
T_A3 = TreeNode(2)
T_A3.right = T_A6
T_A1 = TreeNode(1)
T_A1.left = T_A2
T_A1.right = T_A3


T_B4 = TreeNode(4)
T_B5 = TreeNode(7)
T_B2 = TreeNode(1)
T_B2.right = T_B4
T_B3 = TreeNode(3)
T_B3.right = T_B5
T_B1 = TreeNode(1)
T_B1.left = T_B2
T_B1.right = T_B3

sol = Solution()
sol.mergeTrees(T_A1, T_B1)