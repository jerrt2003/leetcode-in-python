# Binary Search
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = float("inf"), -float("inf")
        n = len(matrix)
        for i in range(n):
            l = min(l, min(matrix[i]))
            r = max(r, max(matrix[i]))

        r += 1

        while l < r:
            m = (l + r - 1) // 2
            if self.check(m, k, matrix):
                r = m
            else:
                l = m + 1

        return l

    def check(self, mid, k, matrix) -> bool:
        count = 0
        n = len(matrix)
        i, j = n - 1, 0
        while i > -1 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
            if count >= k:
                return True
        return count >= k
