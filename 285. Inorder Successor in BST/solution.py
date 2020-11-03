# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        Facebook
        DSF
        Interative
        T:O(V) S:O(1)
        Runtime: 68 ms, faster than 64.55% of Python online submissions for Inorder Successor in BST.
        Memory Usage: 21 MB, less than 34.02% of Python online submissions for Inorder Successor in BST.
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        pre = None
        while root.val != p.val:
            if root.val > p.val:
                pre = root
                root = root.left
            elif root.val < p.val:
                root = root.right
        if not root.right:
            return pre
        else:
            return self.dfs(root.right)

    def dfs(self, node):
        while node.left:
            return self.dfs(node.left)
        return node

