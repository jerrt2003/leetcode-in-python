# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        Facebook
        T:O(V) S:O(1)
        DFS
        Runtime: 28 ms, faster than 79.08% of Python online submissions for Maximum Difference Between Node and Ancestor.
        Memory Usage: 19.7 MB, less than 29.03% of Python online submissions for Maximum Difference Between Node and Ancestor.
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node.left and not node.right:
                return node.val, node.val
            sub_min, sub_max = float('inf'), -float('inf')
            if node.left:
                min_l, max_l = dfs(node.left)
                sub_min, sub_max = min(min_l, sub_min), max(max_l, sub_max)
            if node.right:
                min_r, max_r = dfs(node.right)
                sub_min, sub_max = min(min_r, sub_min), max(max_r, sub_max)
            self.ans = max(self.ans, abs(node.val - sub_max), abs(node.val - sub_min))
            return min(node.val, sub_min), max(node.val, sub_max)

        self.ans = -float('inf')
        dfs(root)
        return self.ans