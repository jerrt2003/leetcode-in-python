# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        Solution: BFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        q = [root]
        res = []
        while q:
            max_val = -float('inf')
            for _ in range(len(q)):
                curr = q.pop(0)
                max_val = max(max_val, curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            res.append(max_val)
        return res