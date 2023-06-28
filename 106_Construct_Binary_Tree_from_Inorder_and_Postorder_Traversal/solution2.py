# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.val_2_idx_maps: Dict[int, int] = {}
        for i, v in enumerate(inorder):
            self.val_2_idx_maps[v] = i
        s1, e1, s2, e2 = 0, len(postorder) - 1, 0, len(inorder) - 1
        return self.helper(postorder, s1, e1, inorder, s2, e2)

    def helper(
        self,
        postorder: List[int],
        s1: int,
        e1: int,
        inorder: List[int],
        s2: int,
        e2: int,
    ) -> Optional[TreeNode]:
        if s1 > e1:
            return None
        node = TreeNode(val=postorder[e1])
        mid = self.val_2_idx_maps[node.val]
        left_tree_count = mid - s2

        node.left = self.helper(
            postorder, s1, s1 + left_tree_count - 1, inorder, s2, mid - 1
        )
        node.right = self.helper(
            postorder, s1 + left_tree_count, e1 - 1, inorder, mid + 1, e2
        )

        return node
