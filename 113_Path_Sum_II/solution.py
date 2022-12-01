# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        if not root:
            return self.ans
        self.helper(root, [], targetSum)
        return self.ans
    
    def helper(self, root: TreeNode, path: List[int], target_sum: int) -> None:
        if not root.left and not root.right:
            if sum(path+[root.val]) == target_sum:
                self.ans.append(path+[root.val])
                return
        if root.left:
            self.helper(root.left, path+[root.val], target_sum)
        if root.right:
            self.helper(root.right, path+[root.val], target_sum)
        