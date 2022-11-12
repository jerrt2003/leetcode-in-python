class Solution(object):
    def numEnclaves(self, A):
        """
        T:O(mn) S:O(1)
        Runtime: 508 ms, faster than 54.93% of Python online submissions for Number of Enclaves.
        Memory Usage: 13.8 MB, less than 67.12% of Python online submissions for Number of Enclaves.
        :type A: List[List[int]]
        :rtype: int
        """
        # self.total = 0
        # for a in A:
        #     self.total += collections.Counter(a)[1]

        def dfs(i, j, grid):
            grid[i][j] = 0
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    dfs(x, y, grid)

        for i in range(len(A)):
            for j in range(len(A[0])):
                if 0 < i < len(A)-1 and 0 < j < len(A[0])-1:
                    continue
                if A[i][j] == 1:
                    dfs(i, j, A)

        return sum(sum(row) for row in A)

# print Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print Solution().numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])