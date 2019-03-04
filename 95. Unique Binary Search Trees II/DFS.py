# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Perf: Runtime: 60 ms, faster than 28.42% / Memory Usage: 14.2 MB, less than 52.24%
        Inspired By: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31592/Recursive-python-solution
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n)

    def dfs(self, s, e):
        if s > e:
            return [None]
        res = []
        for i in range(s, e+1): # i is the current root node
            left_nodes = self.dfs(s, i-1)
            right_nodes = self.dfs(i+1, e)
            for l in left_nodes:
                for r in right_nodes:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                res.append(root)
        return res

