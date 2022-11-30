from typing import List, Optional, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right
        # preorder得到根节点，然后在inorder中找到根节点的位置，它的左边就是左子树的节点，右边就是右子树的节点
        # 可以用hashmap存一個inorder value <-> idx 方便快速查找
        self.inorder_idx_map = {v:i for i, v in enumerate(inorder)}
        return self.helper(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def helper(self, preorder: List[int], s1: int, e1: int, inorder: List[int], s2: int, e2: int) -> TreeNode:
        if s1 == e1:
            return None
        # 找出root
        root_val = preorder[s1]
        root = TreeNode(root_val)
        # 找出root_val在inorder的idx
        mid = self.inorder_idx_map[root_val]
        # inorder[:mid] -> root的左子樹
        # inorder[mid+1:] -> root的右子樹
        # preorder[s1+1:(mid-s2)+s1+1] -> preorder中屬於左子樹的部分
        # preorder[(mid-s2)+s1+1:e1] -> preorder中屬於右子樹的部分
        # (mid-s2) -> 從inorder去推斷出左子樹node count
        root.left = self.helper(preorder, s1+1, (mid-s2)+s1+1, inorder, s2, mid)
        root.right = self.helper(preorder, (mid-s2)+s1+1, e1, inorder, mid+1, e2)
        return root
        
    
