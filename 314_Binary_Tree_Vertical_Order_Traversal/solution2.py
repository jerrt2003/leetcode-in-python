# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import List, Optional


class IndexedNode:
    def __init__(self, node, idx):
        self.node = node
        self.idx = idx


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_to_nodes = collections.defaultdict(list)
        q = [IndexedNode(root, 0)]
        while q:
            cur_node_info = q.pop(0)
            idx = cur_node_info.idx
            node = cur_node_info.node
            column_to_nodes[idx].append(node.val)
            if node.left:
                q.append(IndexedNode(node.left, idx - 1))
            if node.right:
                q.append(IndexedNode(node.right, idx + 1))

        ans = []
        for k in sorted(column_to_nodes.keys()):
            ans.append(column_to_nodes[k])

        return ans
