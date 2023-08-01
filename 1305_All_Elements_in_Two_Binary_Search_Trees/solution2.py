# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1, tree2 = [], []
        if root1:
            self.dfs(root1, tree1)
        if root2:
            self.dfs(root2, tree2)
        i, j, m, n = 0, 0, len(tree1), len(tree2)
        ans = []

        while i < m and j < n:
            if tree1[i] < tree2[j]:
                ans.append(tree1[i])
                i += 1
            else:
                ans.append(tree2[j])
                j += 1

        while i < m:
            ans.append(tree1[i])
            i += 1

        while j < n:
            ans.append(tree2[j])
            j += 1

        return ans

    def dfs(self, root, tree):
        if root.left:
            self.dfs(root.left, tree)
        tree += [root.val]
        if root.right:
            self.dfs(root.right, tree)
