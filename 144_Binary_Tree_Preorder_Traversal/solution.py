from typing import List, Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret: List[int] = []
        if not root:
            return ret
        WHITE = 1
        GREY = 2
        stack: List[Tuple[int, TreeNode]] = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GREY, node))
            else:
                ret.append(node.val)
        return ret