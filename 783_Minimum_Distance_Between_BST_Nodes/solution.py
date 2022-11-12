# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        T:O(n) S:O(1)
        Runtime: 20 ms, faster than 66.00% of Python online submissions for Minimum Distance Between BST Nodes.
        Memory Usage: 12.8 MB, less than 14.29% of Python online submissions for Minimum Distance Between BST Nodes.
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.ans = float('inf')
        self.prev = -float('inf')

        dfs(root)

        return self.ans