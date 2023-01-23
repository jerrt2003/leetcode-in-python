from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.candidate = None
        self.diff = float('inf')
        self.dfs(root, target)
        return self.candidate.val

    def dfs(self, node: TreeNode, target: float) -> None:
        if not node:
            return None
        node_diff = abs(target - node.val)
        if node_diff == 0:
            return node
        if node_diff < self.diff:
            self.candidate = node
            self.diff = node_diff
        if target > node.val and node.right:
            self.dfs(node.right, target)
        elif node.left:
            self.dfs(node.left, target)
        
        