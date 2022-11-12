# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        Thinking Process:
        - create a list to store all finding path
        - if node.left is not None or node.right is not None, then add node(current) into path and pass this "path" along
        - if node.left is None and node.right is None, then add this path into list then return
        - return final path list
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path = []
        if root is not None:
            path = str(root.val)
            self.findPath(root, path)
        return self.path


    def findPath(self, node, path):
        if node.left is None and node.right is None:
            self.path.append(path)
            return
        if node.left is not None:
            new_path = path + '->' + str(node.left.val)
            self.findPath(node.left, new_path)
        if node.right is not None:
            new_path = path + '->' + str(node.right.val)
            self.findPath(node.right, new_path)