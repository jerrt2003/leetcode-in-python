# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        Solution: BFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 140 ms, faster than 9.88% / Memory Usage: 27.6 MB, less than 5.41%
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = [root]
        count = 0
        while stack:
            r = stack.pop(0)
            count += 1
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        return count