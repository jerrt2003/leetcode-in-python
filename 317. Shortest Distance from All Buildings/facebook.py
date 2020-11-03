import collections


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]

        def bfs(q):
            cost = 1
            visit = set()
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in q and (x, y) not in visit:
                            dist[x][y] += cost
                            q.append((x, y))
                            visit.add((x, y))
                cost += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = collections.deque([(i, j)])
                    bfs(q)

        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = min(ans, dist[i][j])

        return ans

print Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])