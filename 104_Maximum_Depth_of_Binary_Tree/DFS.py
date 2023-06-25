# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = -float('inf')
        self.dfs(root, 0)
        
        return self.ans
        
        
    def dfs(self, node: Optional[TreeNode], depth: int) -> None:
        if not node:
            self.ans = max(self.ans, depth)
            return
        self.dfs(node.left, depth+1)    
        self.dfs(node.right, depth+1)
            
        