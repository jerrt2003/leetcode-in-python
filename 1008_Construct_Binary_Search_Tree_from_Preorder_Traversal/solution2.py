# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, 0, len(preorder) - 1)

    def dfs(self, preorder: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        node = TreeNode(preorder[l])
        idx = l + 1
        while idx < r + 1:
            if preorder[idx] > preorder[l]:
                break
            idx += 1
        node.left = self.dfs(preorder, l + 1, idx - 1)
        node.right = self.dfs(preorder, idx, r)

        return node
