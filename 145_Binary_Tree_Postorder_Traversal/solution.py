from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((GREY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                ret.append(node.val)

        return ret