import collections
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        level = 0
        max_sum = -float("inf")
        q = collections.deque([root])

        while q:
            level += 1
            level_sum = 0
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                self.ans = level

        return self.ans
