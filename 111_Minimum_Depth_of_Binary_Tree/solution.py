import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_height = sys.maxsize
        curr_height = 1
        self.helper(root, curr_height)
        return self.min_height

    def helper(self, root: Optional[TreeNode], curr_height: int) -> None:
        if not root.left and not root.right:
            self.min_height = min(curr_height, self.min_height)
            return
        if root.left:
            self.helper(root.left, curr_height+1)
        if root.right:
            self.helper(root.right, curr_height+1)