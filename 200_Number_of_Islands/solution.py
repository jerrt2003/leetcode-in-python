from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return self.bfs(grid)
        return self.dfs(grid)

    def is_valid(self, x: int, y: int, grid: List[List[str]]) -> bool:
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] != '1':
            return False
        return True


    def bfs(self, grid: List[List[str]]) -> int:
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0' # mark node as 'visited' before put into the queue to avoid duplicate
                    island_count += 1
                    q: List[List[int]] = [[i, j]]
                    while q:
                        x, y = q.pop(0)
                        for next_x, next_y in [[x+1, y],[x-1, y],[x, y+1],[x, y-1]]:
                            if self.is_valid(next_x, next_y, grid):
                                grid[next_x][next_y] = '0'
                                q.append([next_x, next_y])

        return island_count

    def dfs(self, grid: List[List[str]]) -> int:

        def search_island(x: int, y: int) -> None:
            if self.is_valid(x, y, grid):
                grid[x][y] = '0'
                for next_x, next_y in [[x+1, y],[x-1, y],[x, y+1],[x, y-1]]:
                    search_island(next_x, next_y)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_count += 1
                    search_island(i, j)
        return island_count
