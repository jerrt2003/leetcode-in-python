# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/diameter-of-binary-tree/solution/
        Thinking Process:
        - Using DFS to count depth of both left and right
        - Update the final answer during the DFS
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.res = 0
        self.depth(root)
        return self.res - 1

    def depth(self, node):
        if not node:
            return 0
        L = self.depth(node.left)
        R = self.depth(node.right)
        self.res = max(self.res, L+R+1)
        return max(L,R)+1