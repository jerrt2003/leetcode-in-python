from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST + inroder == smallest will be visited 'first'
        # create an stack and push node + color into stack
        stack: List[Tuple[TreeNode, int]] = [(root, 1)]
        while k > 0:
            node, color = stack.pop()
            if color == 0: # 只有在color == 0時 node 才算'visited'
                k -= 1 # node 'visited' k才減1
                if k == 0: 
                    return node.val
            else:
                if node.right:
                    stack.append((node.right, 1))
                stack.append((node, 0))
                if node.left:
                    stack.append((node.left, 1))