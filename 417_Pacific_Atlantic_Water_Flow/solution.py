import collections
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        visited1 = set()
        q = collections.deque([])
        m, n = len(heights), len(heights[0])
        for i in range(m):
            if (i, 0) not in visited1:
                visited1.add((i, 0))
                q.append((i, 0))
        for j in range(n):
            if (0, j) not in visited1:
                visited1.add((0, j))
                q.append((0, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    0 <= x
                    and x < m
                    and 0 <= y
                    and y < n
                    and (x, y) not in visited1
                    and heights[x][y] >= heights[i][j]
                ):
                    visited1.add((x, y))
                    q.append((x, y))

        visited2 = set()
        q = collections.deque([])
        for i in range(m):
            if (i, n - 1) not in visited2:
                q.append((i, n - 1))
                visited2.add((i, n - 1))
        for j in range(n):
            if (m - 1, j) not in visited2:
                q.append((m - 1, j))
                visited2.add((m - 1, j))

        while q:
            i, j = q.popleft()
            if (i, j) in visited1:
                ans.append([i, j])
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    0 <= x
                    and x < m
                    and 0 <= y
                    and y < n
                    and (x, y) not in visited2
                    and heights[x][y] >= heights[i][j]
                ):
                    visited2.add((x, y))
                    q.append((x, y))

        return ans
