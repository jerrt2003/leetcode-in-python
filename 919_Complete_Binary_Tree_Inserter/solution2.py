# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = collections.deque([root])

    def insert(self, val: int) -> int:
        new_node = TreeNode(val=val)

        while self.q and self.q[0].left and self.q[0].right:
            node = self.q.popleft()
            self.q.append(node.left)
            self.q.append(node.right)

        top_node = self.q[0]
        if top_node.left is None:
            top_node.left = new_node
        else:
            top_node.right = new_node

        return top_node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
