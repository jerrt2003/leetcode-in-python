from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ret: List[str] = []
        path: List[str] = []
        self.helper(root, path)
        return self.ret

    def helper(self, node: Optional[TreeNode], path: List[str]) -> None:
        val = str(node.val)
        if not node.left and not node.right:
            self.ret.append("->".join(path + [val]))
            return
        if node.left:
            self.helper(node.left, path + [val])
        if node.right:
            self.helper(node.right, path + [val])