# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.value_2_idx_maps: Dict[int, int] = {}
        for i, v in enumerate(postorder):
            self.value_2_idx_maps[v] = i
        s1, e1, s2, e2 = 0, len(preorder) - 1, 0, len(postorder) - 1
        return self.helper(preorder, s1, e1, postorder, s2, e2)

    def helper(
        self,
        preorder: List[int],
        s1: int,
        e1: int,
        postorder: List[int],
        s2: int,
        e2: int,
    ) -> Optional[TreeNode]:
        if s1 > e1:
            return None

        node = TreeNode(val=preorder[s1])
        if s1 == e1:
            return node

        left_root_val = preorder[s1 + 1]
        mid = self.value_2_idx_maps[left_root_val]
        left_tree_count = mid - s2 + 1

        node.left = self.helper(
            preorder, s1 + 1, (s1 + 1) + left_tree_count - 1, postorder, s2, mid
        )

        node.right = self.helper(
            preorder, (s1 + 1) + left_tree_count, e1, postorder, mid + 1, e2 - 1
        )

        return node
