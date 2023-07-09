# T:O(n) S:O(n)
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        self.dfs(root, root.val, root.val)

        return self.ans

    def dfs(self, root, max_val, min_val) -> None:
        if not root:
            return

        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        self.ans = max(self.ans, abs(max_val - min_val))

        self.dfs(root.left, max_val, min_val)
        self.dfs(root.right, max_val, min_val)
