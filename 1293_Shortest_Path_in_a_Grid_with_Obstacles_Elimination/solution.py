class Solution(object):
    def shortestPath(self, grid, k):
        """
        T:O(4^mnlog(k)) S:O(mn)
        TLE
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(i, j, k, mid):
            if i == m-1 and j == n-1:
                return True
            # visit[i][j] = True
            c = grid[i][j]
            grid[i][j] = -1
            for x, y in [(i+1, j),(i, j+1),(i-1, j),(i, j-1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] != -1 and mid > 0:
                    if grid[x][y] == 0:
                        if dfs(x, y, k, mid-1):
                            grid[i][j] = c
                            return True
                    elif grid[x][y] == 1 and k > 0:
                        if dfs(x, y, k-1, mid-1):
                            grid[i][j] = c
                            return True
            grid[i][j] = c
            return False

        l, r = 0, m*n+1
        while l < r:
            mid = (l+r-1)//2
            # visit = [[False for _ in range(n)] for _ in range(m)]
            if dfs(0, 0, k, mid):
                r = mid
            else:
                l = mid+1
        return -1 if l == m*n+1 else l

# print Solution().shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
# print Solution().shortestPath([[0,1,1],[1,1,1],[1,0,0]],1)
# print Solution().shortestPath([[0,0,1,0,0],[0,1,0,1,0]],2)
print Solution().shortestPath([[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]],1)