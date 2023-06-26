# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = float("inf")
        self.helper(root, 0)

        return self.ans

    def helper(self, node: Optional[TreeNode], depth: int) -> None:
        if not node.left and not node.right:
            self.ans = min(self.ans, depth + 1)
            return
        if node.left:
            self.helper(node.left, depth + 1)
        if node.right:
            self.helper(node.right, depth + 1)
