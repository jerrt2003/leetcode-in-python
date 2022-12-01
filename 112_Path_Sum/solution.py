# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, 0, targetSum)
    
    def helper(self, root: Optional[TreeNode], prev_sum: int, target_sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return prev_sum + root.val == target_sum
        return self.helper(root.left, prev_sum + root.val, target_sum) or self.helper(root.right, prev_sum + root.val, target_sum)
        
        