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
        # 遞歸時紀錄含root+左子樹+右子樹的最大和(這是當下全局最大和)
        self.ans = max(self.ans, root.val + left_node_max + right_node_max)
        # 返回含root+(左子樹或是右子樹的最大和)=>當下最大的path和
        return root.val + max(left_node_max, right_node_max)
        