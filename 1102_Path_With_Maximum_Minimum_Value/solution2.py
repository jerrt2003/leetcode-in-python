import heapq
from typing import List


class Node:
    def __init__(self, i, j, score):
        self.i = i
        self.j = j
        self.score = score

    def __lt__(self, other):
        return self.score > other.score


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [Node(0, 0, grid[0][0])]
        heapq.heapify(pq)
        visited = set()
        ans = float("inf")

        while pq:
            node = heapq.heappop(pq)
            i, j = node.i, node.j
            # 每當 pop 出一個 node，就將 ans 更新為當前 node 的 score 和 ans 中的最小值
            ans = min(ans, node.score)
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                break
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(pq, Node(x, y, grid[x][y]))

        return ans
