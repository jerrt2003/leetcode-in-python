# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        T:O(n) S:O(1)
        Runtime: 44 ms, faster than 58.44% of Python online submissions for Delete Leaves With a Given Value.
        Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Delete Leaves With a Given Value.
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        return self.dfs(root, target)

    def dfs(self, node, target):
        if not node:
            return None
        node.left = self.dfs(node.left, target)
        node.right = self.dfs(node.right, target)
        if not node.left and not node.right and node.val == target:
            return None
        return node