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
        Solution: use global variable to log tree is balanced or not.
        !!! however it looks like we can't do "early termination" (which means if there is a sub-tree is unbalanced, then don't compare any further)
        Time Complexity: O(nlog(n))
        Space Complexity: O(log(n))
        Perf: Runtime: 44 ms, faster than 79.85% / Memory Usage: 16.3 MB, less than 95.71%
        :type root: TreeNode
        :rtype: bool
        """
        self.balance = True
        self.getHeight(root)
        return self.balance

    def getHeight(self, node):
        if not node:
            return 0
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)
        if abs(lh-rh) > 1:
            self.balance = False
        return 1+max(lh, rh)