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
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 36 ms, faster than 97.15% / Memory Usage: 19.7 MB, less than 26.87%
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inOrderTraversal(node):
            if node.left:
                ret = inOrderTraversal(node.left)
                if ret is not None:
                    return ret
            self.count -= 1
            if self.count == 0:
                return node.val
            if node.right:
                ret = inOrderTraversal(node.right)
                if ret is not None:
                    return ret
            return None

        if not root:
            return None
        self.count = k
        return inOrderTraversal(root)

