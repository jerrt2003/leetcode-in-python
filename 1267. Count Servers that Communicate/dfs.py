class Solution(object):
    def countServers(self, grid):
        """
        DFS
        T:O(n) S:O(1)
        Runtime: 820 ms, faster than 13.25% of Python online submissions for Count Servers that Communicate.
        Memory Usage: 22.4 MB, less than 100.00% of Python online submissions for Count Servers that Communicate.
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    m = self.dfs(i, j, grid)
                    if m != 1:
                        ret += m
        return ret

    def dfs(self, i, j, grid):
        res = 1
        grid[i][j] = -1
        for y in range(len(grid[0])):
            if grid[i][y] == 1:
                res += self.dfs(i, y, grid)
        for x in range(len(grid)):
            if grid[x][j] == 1:
                res += self.dfs(x, j, grid)
        return res


# print Solution().countServers([[1,0],[0,1]])
# print Solution().countServers([[1,0],[1,1]])
assert Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4