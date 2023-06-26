# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans: List[List[int]] = []
        if not root:
            return self.ans
        self.target_sum = targetSum
        path: List[int] = []
        total = 0
        self.find_path(root, path, total)

        return self.ans

    def find_path(self, node: Optional[TreeNode], path: List[int], total) -> None:
        if not node.left and not node.right:
            if total + node.val == self.target_sum:
                self.ans.append(path + [node.val])
                return

        if node.left:
            self.find_path(node.left, path + [node.val], total + node.val)

        if node.right:
            self.find_path(node.right, path + [node.val], total + node.val)
