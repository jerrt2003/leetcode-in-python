from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # postorder: left -> right -> root
        # self.preorder_value_idx_map = {v: i for i, v in enumerate(preorder)}
        self.postorder_value_idx_map = {v: i for i, v in enumerate(postorder)}
        return self.helper(preorder, 0, len(preorder), postorder, 0, len(postorder))

    def helper(self, preorder: List[int], s1, e1, postorder: List[int], s2, e2) -> TreeNode:
        if s1 == e1:
            return None
        root_val = preorder[s1]
        root = TreeNode(root_val)
        # find boundry
        left_tree_root_val = preorder[s1+1]
        postorder_mid = self.postorder_value_idx_map[left_tree_root_val]
        left_node_count = postorder_mid - s2 + 1
        root.left = self.helper(preorder, s1+1, s1+1+left_node_count, postorder, s2, postorder_mid)
        root.right = self.helper(preorder, s1+1+left_node_count, e1, postorder, postorder_mid+1, e2)
        return root
