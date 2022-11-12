import collections


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        DP
        T: O(R*C*2^RC) S:O(R*C)
        Runtime: 44 ms, faster than 75.91% of Python online submissions for Unique Paths III.
        Memory Usage: 14.2 MB, less than 5.41% of Python online submissions for Unique Paths III.
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        s, e = [0, 0], [0, 0]
        avail = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] % 2 == 0:
                    avail |= (1 << (i*n+j))
                if grid[i][j] == 1:
                    s[0], s[1] = i, j

        dp = collections.defaultdict(int)

        def dfs(i, j, todo):
            if grid[i][j] == 2:
                if todo == 0:
                    return 1
                return 0
            if (i, j, todo) in dp:
                return dp[(i, j, todo)]
            tmp = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and todo & (1 << x*n+y) == (1 << x*n+y):
                    tmp += dfs(x, y, todo^(1 << x*n+y))
            dp[(i, j, todo)] = tmp
            return dp[(i, j, todo)]

        return dfs(s[0],s[1],avail)

print Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
print Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
print Solution().uniquePathsIII([[0,1],[2,0]])