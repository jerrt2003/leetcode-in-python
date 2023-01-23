from common.tree_node import TreeNode

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans: int = -float('inf')
        self.dfs(root, 1)
        return self.ans

    def dfs(self, node: 'TreeNode', path: int) -> None:
        self.ans = max(self.ans, path)
        if node.left:
            if node.left.val == node.val + 1:
                self.dfs(node.left, path+1)
            else:
                self.dfs(node.left, 1)
        if node.right:
            if node.right.val == node.val + 1:
                self.dfs(node.right, path+1)
            else:
                self.dfs(node.right, 1)
        