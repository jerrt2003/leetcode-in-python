# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        ret = []
        while stack1 or stack2:
            nodes_value = []
            if stack1:
                while stack1:
                    node = stack1.pop(-1)
                    nodes_value.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            else:
                while stack2:
                    node = stack2.pop(-1)
                    nodes_value.append(node.val)
                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)
            ret.append(nodes_value)
        return ret
