# Definition for a binary tree node.
from typing import Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balance = self.helper(root)
        return is_balance

    def helper(self, node: Optional[TreeNode]) -> Tuple[int, bool]:
        if not node:
            return 0, True

        left_tree, is_left_balance = self.helper(node.left)
        right_tree, is_right_balance = self.helper(node.right)

        return (
            1 + max(left_tree, right_tree),
            abs(left_tree - right_tree) <= 1 and is_left_balance and is_right_balance,
        )
