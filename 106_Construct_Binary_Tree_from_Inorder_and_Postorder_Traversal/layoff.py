from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left -> root -> right
        # postorder: left -> right -> root
        self.inorder_value_idx_map = {v: i for i, v in enumerate(inorder)}
        return self.helper(postorder, 0, len(postorder), inorder, 0, len(inorder))


    def helper(self, postorder: List[int], s1: int, e1: int, inorder: List[int], s2: int, e2: int) -> TreeNode:
        if s1 == e1:
            return None
        root_val = postorder[e1-1]
        root = TreeNode(root_val)
        mid = self.inorder_value_idx_map[root_val]
        left_node_count = mid - s2
        root.left = self.helper(postorder, s1, s1+left_node_count, inorder, s2, mid)
        root.right = self.helper(postorder, s1+left_node_count, e1-1, inorder, mid+1, e2)
        return root