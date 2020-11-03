import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        BS + Greedy
        T:O(m*nlog(n) S:O(m*m)
        Runtime: 260 ms, faster than 9.22% of Python online submissions for Swim in Rising Water.
        Memory Usage: 16.6 MB, less than 5.22% of Python online submissions for Swim in Rising Water.
        Priority Queue
        T:O(m*mlog(m) S:O(m*m)
        Runtime: 84 ms, faster than 99.29% of Python online submissions for Swim in Rising Water.
        Memory Usage: 13.2 MB, less than 67.16% of Python online submissions for Swim in Rising Water.
        :type grid: List[List[int]]
        :rtype: int
        """
        # m, n = len(grid), len(grid[0])
        # def dfs(i, j, K):
        #     if i == m-1 and j == n-1 and grid[i][j] <= K:
        #         return True
        #     if grid[i][j] > K:
        #         return False
        #     self.visit.add((i, j))
        #     for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
        #         if 0<=x<m and 0<=y<n and (x, y) not in self.visit:
        #             if dfs(x, y, K):
        #                 return True
        #     return False
        #
        # l, r = min(min(row) for row in grid), max(max(row) for row in grid)+1
        # while l < r:
        #     mid = (l+r-1)/2
        #     self.visit = set()
        #     if dfs(0, 0, mid):
        #         r = mid
        #     else:
        #         l = mid+1
        # return l
        pq, ans, visit, m = [], 0, set(), len(grid)
        heapq.heappush(pq,(grid[0][0], 0, 0))
        while pq:
            d, i, j = heapq.heappop(pq)
            ans = max(ans, d)
            if i == m-1 and j == m-1:
                return ans
            for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                if 0<=x<m and 0<=y<m and (x, y) not in visit:
                    heapq.heappush(pq,(grid[x][y], x, y))
                    visit.add((x, y))

print Solution().swimInWater([[0,2],[1,3]])
print Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])