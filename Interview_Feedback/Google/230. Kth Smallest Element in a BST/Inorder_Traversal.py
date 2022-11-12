# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        Solution: in-order traversal with early termination
        Time Complexity: O(n)
        Space Complexity: O(n)
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        self.count = k
        return self._kthSmallest(root)


    def _kthSmallest(self, root):
        if root is None:
            return
        if root.left:
            _res = self._kthSmallest(root.left)
            if _res is not None:
                return _res
        self.count -= 1
        if self.count == 0:
            return root.val
        if root.right:
            _res = self._kthSmallest(root.right)
            if _res is not None:
                return _res
        return None

