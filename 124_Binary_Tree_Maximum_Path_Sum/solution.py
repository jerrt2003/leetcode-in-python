# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')
        self.helper(root)
        return self.ans
    
    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_node_max = max(0, self.helper(root.left))
        right_node_max = max(0, self.helper(root.right))
        # 递归时记录好全局最大和
        self.ans = max(self.ans, root.val + left_node_max + right_node_max)
        # 返回联络最大和
        return root.val + max(left_node_max, right_node_max)
        