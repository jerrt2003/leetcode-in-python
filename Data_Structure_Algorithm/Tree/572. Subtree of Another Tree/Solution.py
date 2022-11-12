# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        Solution:
        Time Complexity: O(m+n)
        Space Complexity: O(m*n) ??
        Perf: Runtime: 244 ms, faster than 70.80% / Memory Usage: 13.2 MB, less than 20.77%
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def isSubtree(s, t):
            if not s and not t:
                return True
            if (not s and t) or (s and not t):
                return False
            if s.val != t.val:
                return False
            return isSubtree(s.left, t.left) and isSubtree(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False
            if s.val == t.val and isSubtree(s, t):
                return True
            else:
                return dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)