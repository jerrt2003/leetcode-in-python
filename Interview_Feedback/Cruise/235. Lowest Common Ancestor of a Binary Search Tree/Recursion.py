# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Thinking process:
        - if root.val == p or root.val == q -> return root directly (since it will be the direct ancestor)
        - if root.val > p and root.val > q -> continue to find in the left side of tree
        - if root.val < p and root.val < q -> continue to find in the right side of tree
        - if (root.val < p and root.val > q) or (root.val > p and root.val < q): return root (lowest ancestor)
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        if root.val == p.val or root.val == q.val: return root
        if root.val > p.val and root.val > q.val: return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val: return self.lowestCommonAncestor(root.right, p, q)
        if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val): return root


