# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            self.max_height = 1

        def find_depth(node=None, height=None):
            height += 1
            self.max_height = max(self.max_height, height)
            if node.left is not None:
                find_depth(node.left, height)
            if node.right is not None:
                find_depth(node.right, height)
            return

        find_depth(node=root, height=0)
        return self.max_height

node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20)
node_20.left = node_15
node_20.right = node_7
node_9 = TreeNode(9)
root = TreeNode(3)
root.left = node_9
root.right = node_20

sol = Solution()
print sol.maxDepth(root)