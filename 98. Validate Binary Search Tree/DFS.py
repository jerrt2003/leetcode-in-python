# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        Solution: DFS + In Order Traversal
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - In order traversal: left -> root -> right
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.inorder = list()
        self.get_inorder(root)
        for i in range(len(self.inorder)-1):
            if self.inorder[i] >= self.inorder[i+1]:
                return False
        return True

    def get_inorder(self, node):
        if node.left is not None:
            self.get_inorder(node.left)
        self.inorder.append(node.val)
        if node.right is not None:
            self.get_inorder(node.right)


Node_1 = TreeNode(1)
Node_2 = TreeNode(1)
Node_1.left = Node_2

sol = Solution()
print sol.isValidBST(Node_1)