# Heap/PriorityQ
from typing import List

import heapq


class Node:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = []
        for i in range(len(matrix)):
            q.append(Node(matrix[i][0], i, 0))

        heapq.heapify(q)
        node = None
        while k > 0:
            node = heapq.heappop(q)
            row = node.row
            col = node.col
            if col + 1 < len(matrix):
                heapq.heappush(q, Node(matrix[row][col + 1], row, col + 1))
            k -= 1

        return node.val
