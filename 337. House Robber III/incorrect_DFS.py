# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        Solution: DFS (incorrect solution)
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF..
        TP:
        - didn't consider situation like: [4,1,null,2,null,3] (兩個點之間level超過2)
        :type root: TreeNode
        :rtype: int
        """
        self.odd = 0
        self.even = 0
        self.dfs(root, 1)
        return max(self.odd, self.even)

    def dfs(self, node, level):
        if node is None: return
        if level % 2 == 0:
            self.even += node.val
        else:
            self.odd += node.val
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)

