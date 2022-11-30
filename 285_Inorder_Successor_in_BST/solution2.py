from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # create stack and push root node
        # use interactive (stack) to traverse tree, if found 'p' mark it
        # then found it successor if existed
        stack: List[Tuple(TreeNode, int)] = [(root, 0)]
        found_p: bool = False
        while stack:
            node, color = stack.pop()
            if color == 1:
                if node == p:
                    found_p = True
                    continue
                if found_p:
                    return node
            else:
                if node.right: 
                    stack.append((node.right, 0))
                stack.append((node, 1))
                if node.left:
                    stack.append((node.left, 0))
        return None
            