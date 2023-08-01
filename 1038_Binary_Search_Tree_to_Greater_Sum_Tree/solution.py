# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        self.dfs(root)
        total = 0
        while self.nodes:
            cur_node = self.nodes.pop()
            total += cur_node.val
            cur_node.val = total

        return root

    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        self.nodes.append(node)
        if node.right:
            self.dfs(node.right)
