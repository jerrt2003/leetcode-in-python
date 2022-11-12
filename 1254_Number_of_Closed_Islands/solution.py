class Solution(object):
    def closedIsland(self, grid):
        """
        DFS
        T:O(mn) S:O(1)
        Runtime: 112 ms, faster than 92.46% of Python online submissions for Number of Closed Islands.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Number of Closed Islands.
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if grid[i][j] == 1:
                return True
            if i-1 < 0 or i+1 >= len(grid) or j-1 < 0 or j+1 >= len(grid[0]):
                return False
            grid[i][j] = 1
            top = dfs(i-1, j)
            bottom = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return top and bottom and left and right

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and dfs(i, j):
                    ret += 1

        return ret

# print Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])
print Solution().closedIsland([[0,0,1,1,0,1,0,0,1,0],
                               [1,1,0,1,1,0,1,1,1,0],
                               [1,0,1,1,1,0,0,1,1,0],
                               [0,1,1,0,0,0,0,1,0,1],
                               [0,0,0,0,0,0,1,1,1,0],
                               [0,1,0,1,0,1,0,1,1,1],
                               [1,0,1,0,1,1,0,0,0,1],
                               [1,1,1,1,1,1,0,0,0,0],
                               [1,1,1,0,0,1,0,1,0,1],
                               [1,1,1,0,1,1,0,1,1,0]])