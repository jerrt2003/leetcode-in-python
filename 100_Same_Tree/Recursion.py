# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        Solution: Recursion
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        elif (p is None and q is not None) or (p is not None and q is None): return False
        else:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left):
                    if self.isSameTree(p.right, q.right):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False