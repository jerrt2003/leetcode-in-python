# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import hash2
class Solution(object):
    def maxDepth(self, root):
        """
        Solution: BFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 24 ms, faster than 99.56% / Memory Usage: 14.5 MB, less than 82.76%
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        res = 0
        stack = hash2.deque([root])
        while stack:
            res += 1
            for i in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res