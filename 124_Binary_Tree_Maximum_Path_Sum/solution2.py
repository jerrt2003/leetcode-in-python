# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        self.helper(root)

        return self.ans

    def helper(self, node) -> int:
        if not node:
            return 0

        left_tree_sum = max(0, self.helper(node.left))
        right_tree_sum = max(0, self.helper(node.right))

        self.ans = max(self.ans, node.val + left_tree_sum + right_tree_sum)

        return node.val + max(left_tree_sum, right_tree_sum)
