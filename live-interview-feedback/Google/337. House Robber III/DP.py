# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        Solution: DP
        Time: O(n)
        Space: O(1)
        Perf: Runtime: 36 ms, faster than 90.20% / Memory Usage: 15.9 MB, less than 79.13%
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self, root):
        if root is None:
            return 0, 0  # rob or no rob
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        rob = root.val + left[1] + right[1]
        no_rob = max(left) + max(right)

        return rob, no_rob