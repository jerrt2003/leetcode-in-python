from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, inorder)
        
    

    def helper(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.helper(preorder[1:mid+1], inorder[:mid])
        root.right = self.helper(preorder[mid+1:], inorder[mid+1:])
        return root


        
        