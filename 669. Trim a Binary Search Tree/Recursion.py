# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        Solution: Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/trim-a-binary-search-tree/solution/
        Thinking process:
        Algorithm:
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node):
            if node is None: return None
            if node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root,L,R)


