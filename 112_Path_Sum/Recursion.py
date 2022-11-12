# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        Thinking Process:
        - Same thinking prcess to Q.111
        - !!! path sum is root node to leaf !!!
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.target_sum = sum
        if root is None: return False
        return self.findSum(root, 0)


    def findSum(self, node, sum):
        new_sum = sum + node.val
        if node.left is None and node.right is None:
            if new_sum == self.target_sum:
                return True
            else:
                return False
        if node.left is not None and self.findSum(node.left, new_sum):
            return True
        if node.right is not None and self.findSum(node.right, new_sum):
            return True
        return False

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_1.left = node_2

sol = Solution()
print sol.hasPathSum(node_1, 0)