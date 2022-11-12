# -*- coding: utf-8 -*-
class Solution(object):
    def swimInWater(self, grid):
        """
        Solution: BS + Greedy
        Time Complexity: O(n^2log(n))
        Space Complexity: O(n^2)
        Perf: Runtime: 244 ms, faster than 22.22% / Memory Usage: 14.9 MB, less than 8.33%
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        def reachable(i, j, k, visited):
            if (i, j) == (m-1, m-1):
                return True
            if grid[i][j] > k:
                return False
            visited.append((i, j))
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<m and 0<=y<m and grid[x][y]<=k and (x,y) not in visited:
                    if reachable(x,y,k,visited):
                        return True
            return False

        l, r, = 0, m*m+1
        while l < r:
            mid = (l+r-1)/2
            if reachable(0,0,mid,[]):
                r = mid
            else:
                l = mid+1
        return l

assert Solution().swimInWater([[0,2],[1,3]]) == 3
assert Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16
assert Solution().swimInWater([[3,2],[0,1]]) == 3