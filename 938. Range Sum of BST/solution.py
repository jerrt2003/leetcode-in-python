# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        DFS: T:O(n) S:O(1)
        Runtime: 268 ms, faster than 62.38% of Python online submissions for Range Sum of BST.
        Memory Usage: 29.1 MB, less than 6.45% of Python online submissions for Range Sum of BST.
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0
        self.dfs(root, L, R)
        return self.ans

    def dfs(self, root, L, R):
        if root:
            if L <= root.val <= R:
                self.ans += root.val
            if L < root.val:
                self.dfs(root.left, L, R)
            if R > root.val:
                self.dfs(root.right, L, R)