# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.prefix = collections.defaultdict(int)
        self.prefix[0] = 1
        self.target_sum = targetSum
        self.ans = 0

        self.dfs(root, 0)

        return self.ans

    def dfs(self, node, cur_sum):
        if not node:
            return
        cur_sum += node.val
        self.ans += self.prefix[cur_sum - self.target_sum]
        self.prefix[cur_sum] += 1
        if node.left:
            self.dfs(node.left, cur_sum)
        if node.right:
            self.dfs(node.right, cur_sum)
        self.prefix[cur_sum] -= 1
        cur_sum -= node.val
