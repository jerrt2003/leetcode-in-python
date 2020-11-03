# -*- coding: utf-8 -*-
class Solution(object):
    def minimumTotal(self, triangle):
        """
        Solution: Backtracking + DP
        Time Complexity: O(n) (n: numbers in the triangle)
        Space Complexity: O(n)
        TP:
        - for each level mark the min_dist to that number
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]: return 0
        res = triangle[0]
        for tri in triangle[1:]:
            min_dist = []
            for i in range(len(tri)):
                if i == 0:
                    min_dist.append(tri[0]+res[0])
                elif i == len(tri)-1:
                    min_dist.append(tri[-1]+res[-1])
                else:
                    min_dist.append(min(tri[i]+res[i-1], tri[i]+res[i]))
            res = min_dist
        return min(res)

nums = [[-1],[2,3],[1,-1,-3]]
print Solution().minimumTotal(nums)