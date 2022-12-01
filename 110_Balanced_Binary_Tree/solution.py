from typing import Optional, List, Any

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_left_balanced, left_h = self.helper(root.left, 0)
        is_right_balanced, right_h = self.helper(root.right, 0)
        return is_left_balanced and is_right_balanced and abs(left_h-right_h) <= 1

    def helper(self, root: Optional[TreeNode], ht: int) -> List[Any]:
        if not root:
            return True, ht
        is_left_balanced, left_h = self.helper(root.left, ht+1)
        is_right_balanced, right_h = self.helper(root.right, ht+1)
        return [is_left_balanced and is_right_balanced and abs(left_h - right_h) <= 1, ht+1]