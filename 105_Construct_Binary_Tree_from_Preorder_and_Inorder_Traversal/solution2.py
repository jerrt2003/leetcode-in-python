# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.value_2_idx_mapping: Dict[int, int] = {}
        for i, v in enumerate(inorder):
            self.value_2_idx_mapping[v] = i
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        
        
        
    def helper(self, preorder: List[int], s1: int, e1: int, inorder: List[int], s2: int, e2: int) -> Optional[TreeNode]:
        # 為什麼要使用 s1 > e1?
        # 當前序為[1,2] 中序為[2,1]時會造成出界的情況
        if s1 > e1:
            return None
        node = TreeNode(val=preorder[s1])
        mid = self.value_2_idx_mapping[node.val]
        left_tree_node_count = mid - s2
        
        node.left = self.helper(preorder, s1+1, (s1+1) + left_tree_node_count -1, inorder, s2, mid-1)
        node.right = self.helper(preorder, (s1+1)+left_tree_node_count, e1, inorder, mid+1, e2)
        
        return node