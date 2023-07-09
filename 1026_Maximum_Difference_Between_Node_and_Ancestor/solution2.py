# T:O(n^2) S:O(n)
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        path = []
        self.dfs(root, path)

        return self.ans

    def dfs(self, node, path) -> None:
        if not node:
            return
        for ancestor in path:
            self.ans = max(self.ans, abs(node.val - ancestor.val))
        if node.left:
            self.dfs(node.left, path + [node])
        if node.right:
            self.dfs(node.right, path + [node])
