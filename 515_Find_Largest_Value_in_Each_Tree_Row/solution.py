# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = collections.deque([root])
        while q:
            max_value = -float("inf")
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_value)

        return ans
