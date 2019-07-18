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
        Solution: Recursion + InOrderTraversal
        Time Complexity:
        Space Complexity:
        Inspired By: MYSLEF!!
        Thinking Process:
        - In BST, in order traversal (left->root->right) is very useful since it guaranteed left < root < right
        - Thus we can first do in order traversal to build up a completed ordered list
        - Then we return (k-1)th element of that list
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if k == 0 or root is None:
            return 0
        self.orderedNodes = []
        self.inOrderTraversal(root)
        if k-1 > len(self.orderedNodes):
            return 0
        return self.orderedNodes[k-1]

    def inOrderTraversal(self, node):
        if node.left is None and node.right is None:
            self.orderedNodes.append(node.val)
            return
        if node.left is not None:
            self.inOrderTraversal(node.left)
        self.orderedNodes.append(node.val)
        if node.right is not None:
            self.inOrderTraversal(node.right)