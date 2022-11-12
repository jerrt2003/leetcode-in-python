# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        T:O(n) S:O(1)
        Runtime: 24 ms, faster than 78.95% of Python online submissions for Distribute Coins in Binary Tree.
        Memory Usage: 13 MB, less than 7.69% of Python online submissions for Distribute Coins in Binary Tree.
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.ans += abs(l)+abs(r)
            if node.val == 0:
                return l+r-1
            elif node.val == 1:
                return l+r
            else:
                return node.val+l+r-1

        dfs(root)
        return self.ans