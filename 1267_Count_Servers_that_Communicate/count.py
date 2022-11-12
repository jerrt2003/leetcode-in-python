class Solution(object):
    def countServers(self, grid):
        """
        T:O(2mn) S:O(m+n)
        Runtime: 484 ms, faster than 38.55% of Python online submissions for Count Servers that Communicate.
        Memory Usage: 13.9 MB, less than 100.00% of Python online submissions for Count Servers that Communicate.
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        if m == 0 or n == 0:
            return 0

        rowSum = [0]*m
        colSum = [0]*n
        for i in range(m):
            for j in range(n):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowSum[i] > 1 or colSum[j] > 1):
                    count += 1

        return count