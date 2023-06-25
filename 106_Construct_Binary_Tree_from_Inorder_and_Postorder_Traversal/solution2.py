# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_2_idx_maps: Dict[int, int] = {}
        for i, v in enumerate(inorder):
            val_2_idx_maps[v] = i
        s1, e1, s2, e2 = 0, len(postorder)-1, 0, len(inorder)-1
        
        
    def helper(self, postorder: List[int], s1: int, e1: int, inorder: List[int], s2: int, e2: int) -> Optional[TreeNode]: