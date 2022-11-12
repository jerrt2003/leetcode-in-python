# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        T:O(n) S:O(1)
        Runtime: 12 ms, faster than 97.97% of Python online submissions for Univalued Binary Tree.
        Memory Usage: 12.7 MB, less than 8.33% of Python online submissions for Univalued Binary Tree.
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root.val, root.left) and self.dfs(root.val, root.right)


    def dfs(self, v, node):
        if not node:
            return True
        if v != node.val:
            return False
        return self.dfs(v, node.left) and self.dfs(v, node.right)