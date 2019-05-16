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
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res1 = self.helper(p, [])
        print res1
        res2 = self.helper(q, [])
        print res2
        return str(res1) == str(res2)

    def helper(self, node, res):
        if node is None:
            return None
        res.append(node.val)
        res.append(self.helper(node.left, res))
        res.append(self.helper(node.right, res))
        return res