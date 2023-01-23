import heapq

from typing import Optional, List

class NodeInfo:
    def __init__(self, node: TreeNode = None, diff: int = None):
        self.node = node
        self.diff = diff

    def __lt__(self, other):
        if self.diff == other.diff:
            return True
        return self.diff > other.diff

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []
        self.pq: List[NodeInfo] = []
        heapq.heapify(self.pq)
        self.dfs(root, target, k)

        ans: List[int] = []
        while self.pq:
            node_info = heapq.heappop(self.pq)
            ans.append(node_info.node.val)
        return ans

    def dfs(self, node: TreeNode, target: float, k: int):
        if not node:
            return
        node_info = NodeInfo(node=node, diff=abs(target-node.val))
        heapq.heappush(self.pq, node_info)
        if len(self.pq) > k:
            heapq.heappop(self.pq)
        if node.left:
            self.dfs(node.left, target, k)
        if node.right:
            self.dfs(node.right, target, k)

