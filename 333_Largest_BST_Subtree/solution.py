# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.is_valid_BST(root, -float("inf"), float("inf")):
            return self.count_node(root)
        else:
            return max(
                self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right)
            )

    def is_valid_BST(self, node, l, r) -> bool:
        if not node:
            return True
        if node.val >= r or node.val <= l:
            return False
        return self.is_valid_BST(node.left, l, node.val) and self.is_valid_BST(
            node.right, node.val, r
        )

    def count_node(self, node) -> int:
        if not node:
            return 0
        return 1 + self.count_node(node.left) + self.count_node(node.right)
