# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        Solution:
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
        TP:
        - inorder traversal: left -> root -> right
        - postorder traversal: left -> right -> root
        - as you can see, with any given tree, the last element of postorder traversal must be the root node
        - also based on the question, there won't be any duplicate nodes
        - thus we can use postorder info to find tree's "root" node in inorder traversal, then divide the tree into half
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: # means no more nodes available for recursion
            return None
        root = TreeNode(postorder.pop())
        inorder_idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorder_idx+1:], postorder) # need to start with right node since postorder's order is left -> right -> root
        root.left = self.buildTree(inorder[:inorder_idx], postorder)
        return root


