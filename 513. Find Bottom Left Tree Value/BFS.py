# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        Solution: BFS
        Time Complexity: O(n) <n: number of nodes>
        Space Complexity: O(n)
        Inspired By: MySELF!!
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return None
        q = [root]
        res = []
        while q:
            res = q[:]
            for i in range(len(q)):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res.pop(0).val