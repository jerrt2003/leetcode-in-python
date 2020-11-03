import heapq


class Solution(object):
    def minCost(self, grid):
        """
        Dijkstra T:O(E+vlog(v)) S:O(v)
        T:O(E+mnlog(mn)) S:O(mn)
        Runtime: 764 ms, faster than 21.82% of Python online submissions for Minimum Cost to Make at Least One Valid Path in a Grid.
        Memory Usage: 15.6 MB, less than 100.00% of Python online submissions for Minimum Cost to Make at Least One Valid Path in a Grid.
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        pq = [(0,0,0)] # cost, i, j
        while pq:
            curr_cost, i, j = heapq.heappop(pq)
            if (i, j) == (m-1, n-1):
                return curr_cost
            if dp[i][j] != -1:
                continue
            dp[i][j] = curr_cost
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<m and 0<=y<n:
                    if ((x, y) == (i-1, j) and grid[i][j] != 4) or ((x,y)==(i+1,j) and grid[i][j]!=3) or ((x,y)==(i,j-1) and grid[i][j]!=2) or ((x,y)==(i,j+1) and grid[i][j]!=1):
                        heapq.heappush(pq,(curr_cost+1,x,y))
                    else:
                        heapq.heappush(pq,(curr_cost,x,y))

        return dp[-1][-1]

print Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])